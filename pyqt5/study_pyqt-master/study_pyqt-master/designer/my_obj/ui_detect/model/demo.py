import os
import numpy as np
import cv2
from side_img_crop import unet_onnx as unet_side
from front_pianyi import unet_onnx as unet_pianyi
from front_img import yolo_onnx
import matplotlib.pyplot as plt


class Demo():
    def __init__(self):
        classes_list = ["background", "up", "down", "suilie"]
        onnx_path = r"weight/u2net_p_20220928.onnx"
        # 面积筛选去掉小的  # d_thresh 盖板偏移量阈值像素值
        self.side_detect = unet_side(onnx_path, classes_list, draw_box=False, contour_area=800, d_thresh=20)

        classes_list = ["background", "jiao", "xian"]
        onnx_path = r"weight/u2net_p_107_epoch_20220930_pianyi.onnx"
        #  scale_thresh是线偏移距离边缘的比例阈值  dabian_thresh打扁宽度阈值
        self.pianyi_detect = unet_pianyi(onnx_path, classes_list, draw_box=False, scale_thresh=0.3, dabian_thresh=85)

        clas_names = ["ng"]  # 端银断线、发黑、锡包铝、引线断线
        onnx_path = r"weight/best.onnx"
        self.front_detect = yolo_onnx(onnx_path, clas_names, conf_thres=0.30, box_w=0, box_h=0)

    def side_img(self, image):
        # 侧盖板，返回true/false，缺陷类别，偏移量，图像
        result, classes_list_out, image_out = self.side_detect.detect(image)

        return result, classes_list_out, image_out

    def front_img(self, image):
        # 打扁过大和线偏移
        result, classes_list_out, image_out = self.pianyi_detect.detect(image)
        if result:  # 正面线没有偏移继续检测焊接不良，否则不检测
            # 正面焊接不良
            # 返回值n张图，取第一张 [[result, out_label, out_img]]
            result, classes_list_out, image_out = self.front_detect.detect(image)[0]

        return result, classes_list_out, image_out


if __name__ == '__main__':
    images_path = r"D:\my_program\project\kunci-20220906\train_data\all_data\2\Data_85962\盖板偏移"
    # images_path = r"D:\my_program\project\kunci-20220906\train_data\all_data\1\引线断线"

    demo = Demo()
    for img_name in os.listdir(images_path):
        if img_name.split(".")[-1] != "jpg":
            continue
        image_path = os.path.join(images_path, img_name)
        # image_path = r"D:\my_program\project\kunci-20220906\train_data\test_img\Image_20220919124741324.jpg"
        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), 1)  # h,w,c

        # 检测侧边图
        result_side, classes_list_out, image_out = demo.side_img(image)
        # 检测正面图
        # result_front, classes_list_out, image_out = demo.front_img(image)

        print(result_side)
        # print(result_front)
        print(classes_list_out)

        plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title("image")
        plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(image_out, cv2.COLOR_BGR2RGB)), plt.title("out")
        plt.show()
