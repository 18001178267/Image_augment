import os,glob
from PIL import Image
import os.path
import glob
import cv2 as cv
import numpy as np
'''
    下两列设置输出图片分辨率
'''
out_w=720
out_h=540

#提取目录下所有图片,更改尺寸后保存到另一目录
img_path = glob.glob("C:\\Users\\YFZX\\Desktop\\13_institute\\soil_bullet_hole\\soil_original_copy\\*.jpg")
path_save = "C:/Users/YFZX/Desktop/13_institute/soil_bullet_hole/0521test"
for file in img_path:
  #print(file)
  name = os.path.join(path_save, os.path.basename(file))
  #print(name)
  im = Image.open(file)
  im_copy=im.copy()
  im_copy.thumbnail((720,540))
  print(im_copy.format, im_copy.size, im_copy.mode)
  im_copy.save(name,'JPEG')


for file in img_path:
  save_name = os.path.join(path_save, os.path.basename(file))
  im =cv.imread(file)
  im_copy=im.copy()
  ori_h=im_copy.shape[0]
  ori_w=im_copy.shape[1]
  # 若宽度达到极限，则拼合高度mask
  if ori_w==out_w:
        if ori_h==out_h:
            pass
        else:
            gap_h=out_h-ori_h
            roi_img  = np.zeros([gap_h,720],dtype=np.uint8)
            roi_img=cv.cvtColor(roi_img,cv.COLOR_GRAY2BGR)
            img3 = np.vstack([im_copy, roi_img])
            cv.imwrite(save_name, img3)
            print(save_name,"deal done")
  #若高度达到极限，则拼合宽度mask
  if ori_h==ori_h:
        if ori_w==out_w:
            pass
        else:
            gap_w=out_w-ori_w
            roi_img  = np.zeros([540,gap_w],dtype=np.uint8)
            roi_img=cv.cvtColor(roi_img,cv.COLOR_GRAY2BGR)
            img3 = np.hstack([im_copy, roi_img])
            cv.imwrite(save_name, img3)
            print(save_name,"deal done")