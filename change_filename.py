import xml.dom.minidom
import os
path='C:\\Users\\YFZX\\Desktop\\13_institute\\soil_bullet_hole\\modeling\\test_xml\\' # xml文件存放路径
sv_path='C:\\Users\\YFZX\\Desktop\\13_institute\\soil_bullet_hole\\modeling\\test_cg_xml\\' # 修改后的xml文件存放路径
files = os.listdir(path)

for xmlFile in files:
    dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  # 打开xml文件，送到dom解析
    root = dom.documentElement  # 得到文档元素对象
    names = root.getElementsByTagName('filename')
    a, b = os.path.splitext(xmlFile)  # 分离出文件名a
    #print(a)
    for n in names:
        n.firstChild.data = a + '.jpg'
    with open(os.path.join(sv_path, xmlFile), 'w') as fh:
        dom.writexml(fh)
