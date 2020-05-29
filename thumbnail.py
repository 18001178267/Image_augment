import os,glob
from PIL import Image
import os.path
import glob


#提取目录下所有图片,更改尺寸后保存到另一目录
img_path = glob.glob("C:\\Users\\YFZX\\Desktop\\13_institute\\1.jpg")
path_save = "C:\\Users\\YFZX\\Desktop\\"
for file in img_path:
  #print(file)
  name = os.path.join(path_save, os.path.basename(file))
  #print(name)
  im = Image.open(file)
  im_copy=im.copy()
  im_copy.thumbnail((720,540))
  print(im_copy.format, im_copy.size, im_copy.mode)
  im_copy.save(name,'JPEG')