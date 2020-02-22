# -*- coding: utf-8 -*-

'''
PYTHON CODE TO CONVERT .XML FILES TO .TXT FILES AT ONCE
'''

#import necessary packages
from xml.dom import minidom
import os
import glob

#add your class names and its index such as 0, 1, 2, etc
class_names={}
class_names["accessory"] =0
class_names["top"]       =1
class_names["bottom"]    =2
class_names["bag"]       =3
class_names["shoes"]     =4

#this converts the coordinates in xml format to yolo format. This function computes the mathematical operations of x,y,w,h
def convert_coordinates(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

#computes the convertion of .xml to .txt and writes the .txt files
def convert_xml2yolo( class_names ):

    for fname in glob.glob("*.xml"):  #give the folder name in which .xml files are present
        
        xmldoc = minidom.parse(fname)
        
        fname_out = (fname[:-4]+'.txt')  #format in which .txt files should be present

        with open(fname_out, "w") as f:  #writing of .txt format
  
            itemlist = xmldoc.getElementsByTagName('object')
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)  #The firstChild property returns the first child node of the selected element.
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)

            for item in itemlist:
                # get class label
                classid =  (item.getElementsByTagName('name')[0]).firstChild.data
                if classid in class_names:
                    label_str = str(class_names[classid])
                else:
                    label_str = "-1"
                    print ("warning: label '%s' not in class_names table" % classid)

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width,height), b)
                #print(bb)

                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

        print ("wrote %s" % fname_out)



def main():
    convert_xml2yolo( class_names )


if __name__ == '__main__':
    main()