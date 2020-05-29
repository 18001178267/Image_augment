'''
只需修改三处，第一第二处改成对应的文件夹目录，
第三处改成对应的文件名，这里是train.csv
os.chdir('D:\\python3\\models-master\\research\\object_detection\\images\\train')
path = 'D:\\python3\\models-master\\research\\object_detection\\images\\train'
xml_df.to_csv('train.csv', index=None)
'''
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

os.chdir('C:\\Users\\YFZX\\Desktop\\13_institute\\soil_bullet_hole\\modeling\\test_xml\\')
path = 'C:\\Users\\YFZX\\Desktop\\13_institute\\soil_bullet_hole\\modeling\\test_xml\\'

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '\\*.xml'):
        tree = ET.parse(xml_file)
        #print(tree)
        root = tree.getroot()
        #hh=root.findall('object')
        #print(hh[0][0].text)
        #print(root.find('size')[0])
        for member in root.findall('object'):
            #print(member,member[0].text)
            try:
                value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            except:
                pass
            #print(value)
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    image_path = path
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('test.csv', index=None)
    print('Successfully converted xml to csv.')


main()