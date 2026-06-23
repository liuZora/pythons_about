import onnxruntime
import numpy as np
import cv2
import os
import time


class unet_onnx():
    def __init__(self, onnx_path, classes_list, draw_box=True, box_w=0, box_h=0, contour_area=0, d_thresh=0):
        # 创建一个会话  类似于pytorch创建模型
        # providers = ['TensorrtExecutionProvider', 'CUDAExecutionProvider', 'CPUExecutionProvider']
        providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
        self.ort_session = onnxruntime.InferenceSession(onnx_path, providers=providers)
        # print(self.ort_session.get_outputs()[0])  # 输出结果  [1, 36288, 9]
        # print(self.ort_session.get_inputs()[0])  # 输入形状  [1, 3, 576, 1024]
        n, c, self.IMG_HEIGHT, self.IMG_WIDTH = self.ort_session.get_inputs()[0].shape  # 输入形状 [n, c, height, width]

        self.classes_list = classes_list
        self.color_list = [[0, 0, 0], [0, 0, 255], [0, 255, 0], [255, 0, 0], [255, 255, 0], [255, 0, 255],
                           [0, 255, 255]]

        self.draw_box = draw_box  # 是否画成box，contour
        self.box_w = box_w  # 筛选框的阈值
        self.box_h = box_h
        self.contour_area = contour_area  # 筛选框的面积
        self.d_thresh = d_thresh  # 偏移量像素值阈值

    def detect(self, img):
        images = img.copy()

        l_x1, l_y1, l_x2, l_y2 = 154, 222, 854, 1072  # 700*850  w,h
        r_x1, r_y1, r_x2, r_y2 = 1699, 120, 2399, 970  # 700*850

        l_img = images[l_y1:l_y2, l_x1:l_x2, :]  # 裁剪出两张图
        r_img = images[r_y1:r_y2, r_x1:r_x2, :]

        img_list = [l_img, r_img]
        point_list = [np.array([l_x1, l_y1]), np.array([r_x1, r_y1])]

        result_list = []
        classes_list = []
        for i in range(len(img_list)):
            draw_ng_ok = ""
            # 预处理, resize加黑边，换颜色通道，归一化
            real_img, scale, bottom, right = self.scale_normal(img_list[i])

            # 侦测
            ort_inputs = {self.ort_session.get_inputs()[0].name: real_img}
            mask_out_feature = self.ort_session.run(None, ort_inputs)[0]  # [n, classes, 416, 416]

            # 产生掩码图
            mask_out_ = np.argmax(mask_out_feature, axis=1)  # [416, 416] 掩码图
            n1, h1, w1 = mask_out_.shape
            mask_out = mask_out_[:, 0:h1 - bottom, 0:w1 - right]

            # 查看缺陷类别 碎裂，显示结果
            result, classes_list_out, images = self.draw_result(mask_out[0], images, scale, point=point_list[i])
            # 计算上下盖板的距离
            d = self.up_down(mask_out[0], scale, images, point=point_list[i])
            # d = self.up_down(mask_out[0], scale, point=point_list[i])
            if d > self.d_thresh:
                result = False
                # d左右偏移量
                classes_list_out.append(f"pianyi_{i + 1}_{round(d, 2)}")
                draw_ng_ok = "_ng"

            cv2.putText(images, f"pianyi_{i + 1}_{round(d, 2)}{draw_ng_ok}", (1800, 1800 + 55 * (i + 1)),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)  # 写类别

            result_list.append(result)
            classes_list.extend(classes_list_out)

        result = min(result_list)
        classes_list_out = classes_list

        return result, classes_list_out, images

    def draw_result(self, mask_out, image, scale, point):
        result = True  # 没缺陷
        classes_list_out = []  # 有缺陷框的类别
        for i in range(3, len(self.classes_list)):  # 查看碎裂的缺陷
            mask_out_copy = mask_out.copy()
            mask_bool = mask_out_copy != i
            mask_out_copy[mask_bool] = 0

            contours, _ = cv2.findContours(np.uint8(mask_out_copy), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) == 0:  # 没有分割出来
                continue
            # result = False  # 有缺陷
            for j in range(len(contours)):  # 循环每个轮廓
                # print(self.classes_list[i])
                contour = (contours[j] / scale).astype(int)
                contour += point
                area = cv2.contourArea(contour)
                contour = contour.squeeze(1)

                label = self.classes_list[i]
                classes_list_out.append(label)

                x1, y1, x2, y2 = np.min(contour[:, 0]), np.min(contour[:, 1]), np.max(contour[:, 0]), np.max(
                    contour[:, 1])
                box_w_out = x2 - x1
                box_h_out = y2 - y1

                if box_w_out < self.box_w or box_h_out < self.box_h or area < self.contour_area:
                    continue

                result = False  # 有缺陷
                if self.draw_box:  # 画框
                    cv2.rectangle(image, (x1, y1), (x2, y2), color=self.color_list[i], thickness=1)
                else:  # 画轮廓
                    cv2.drawContours(image, [contour], 0, color=self.color_list[i], thickness=1)

                cv2.putText(image, self.classes_list[i] + f"_{area}", (x1, y1 - 7), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            self.color_list[i],
                            3)  # 写类别

        return result, classes_list_out, image

    # 计算上下盖板的距离
    def up_down(self, mask_out, scale, image, point):
        points_up = np.array([])
        points_down = np.array([])
        for i in range(1, 3):  # 查看up和down是否偏移
            mask_out_copy = mask_out.copy()
            mask_bool = mask_out_copy != i
            mask_out_copy[mask_bool] = 0

            contours, _ = cv2.findContours(np.uint8(mask_out_copy), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

            if len(contours) == 0:  # 没有分割出来
                continue

            # 找到up、down的最大轮廓
            contour = contours[np.argmax([len(contour) for contour in contours])]

            contour = (contour / scale).astype(int)
            contour += point
            rect = cv2.minAreaRect(contour)
            box = np.int32(cv2.boxPoints(rect))  # 最小矩形 四个点的坐标  (4, 2)

            cv2.drawContours(image, [box], -1, (0, 255, 0), 2)  # 画轮廓

            sort_box = self.sort_points(box)  # 左下、左上、右上、右下，顺时针排列
            # print(sort_box)
            # print(i)
            if i == 1:  # 上盖板
                points_up = sort_box[1:3, :]

            elif i == 2:
                points_down = sort_box[1:3, :]
                x1, y1, x2, y2 = points_down.reshape(-1)
                k = (y1 - y2) / (x1 - x2 + 1e-10)
                b = (y2 * x1 - y1 * x2) / (x1 - x2 + 1e-10)

        # plt.imshow(image)
        # plt.show()
        if points_up.shape[0] == 0 or points_down.shape[0] == 0:
            d = 1e10
            return d

        x1, y1, x2, y2 = points_up.reshape(-1)
        d1 = np.abs(k * x1 - y1 + b) / np.power(np.sum(k * k + 1), 1 / 2)
        d2 = np.abs(k * x2 - y2 + b) / np.power(np.sum(k * k + 1), 1 / 2)
        d = (d1 + d2) / 2

        return d

    def sort_points(self, pts):
        # 按顺时针顺序对矩形点进行排序
        sort_x = pts[np.argsort(pts[:, 0]), :]

        Left = sort_x[:2, :]
        Right = sort_x[2:, :]
        # Left sort
        Left = Left[np.argsort(Left[:, 1])[::-1], :]
        # Right sort
        Right = Right[np.argsort(Right[:, 1]), :]

        return np.concatenate((Left, Right), axis=0)

    def scale_normal(self, image):
        scale = min(self.IMG_HEIGHT / image.shape[0], self.IMG_WIDTH / image.shape[1])
        real_img_ = cv2.resize(image, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)  # (416, 311, 3)

        bottom = self.IMG_HEIGHT - real_img_.shape[0]
        right = self.IMG_WIDTH - real_img_.shape[1]

        real_img = cv2.copyMakeBorder(real_img_, 0, bottom, 0, right, cv2.BORDER_CONSTANT, value=0)  # (416, 416, 3)
        real_img = cv2.cvtColor(real_img, cv2.COLOR_BGR2RGB)

        real_img = real_img.transpose(2, 0, 1)  # hwc --> chw
        real_img = real_img.astype(np.float32)  # 转为浮点型+

        img = real_img / 255.  # 归一化到[0-1]

        # img = (img - np.array([0.485, 0.456, 0.406])[..., None, None]) / np.array([0.229, 0.224, 0.225])[..., None, None]

        img[0, :, :] = (img[0, :, :] - 0.485) / 0.229
        img[1, :, :] = (img[1, :, :] - 0.456) / 0.224
        img[2, :, :] = (img[2, :, :] - 0.406) / 0.225

        img = img[None]

        return img, scale, bottom, right


if __name__ == '__main__':
    # 固定裁剪图像的一部分或几部分进行检测，然后结果计算到原图
    import matplotlib.pyplot as plt

    classes_list = ["background", "up", "down", "suilie"]  # 6个关键点
    onnx_path = r"weight/u2net_p_20220928.onnx"

    # images_path = r"/Users/houtianyu/Desktop/my/my_code/project/kunci/data/all_data/ok12"
    images_path = r"D:\my_program\project\kunci-20220906\train_data\train_data\1018现场图\2\2\NG"
    # images_path = r"D:\my_program\project\kunci-20220906\train_data\train_data\suilie\盖板碎裂2"
    # images_path = r"D:\my_program\project\kunci-20220906\train_data\all_data\2\Data_85962\盖板偏移"

    # 面积筛选去掉小的  # d_thresh 偏移量阈值像素值
    detect = unet_onnx(onnx_path, classes_list, draw_box=False, contour_area=800, d_thresh=20)
    for img_name in os.listdir(images_path):
        print(img_name)
        img_name = r"20221018161211+63000mm.jpg"
        image_path = os.path.join(images_path, img_name)
        # image_path = r"D:\my_program\project\kunci-20220906\train_data\test_img\Image_20220919124741324.jpg"
        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), 1)  # h,w,c

        result, classes_list_out, image_out = detect.detect(image)

        # t1 = time.time()
        # for i in range(100):
        #     result, classes_list_out, image_out = detect.detect(image)
        # t2 = time.time()
        # print(f"time:{round((t2 - t1) / 100, 4)}s")

        print(result)
        print(classes_list_out)
        print("=================")

        # if not result:
        plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title("image")
        plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(image_out, cv2.COLOR_BGR2RGB)), plt.title("out")
        plt.show()
