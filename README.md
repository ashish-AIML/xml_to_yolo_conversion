# Convertion of XML files to YOLO format

This is summary readme for convertion of .xml files to .txt files, i.e., YOLO format


Run [xml_to_yolo_convert](xml_to_yolo_convert.py) to automatically convert `.xml` files to `.txt` files at once

You can paste your folder name in which `.xml` files are present in the code snippet `for fname in glob.glob("*.xml"):` and run it

The corresponding `.txt` files are created and saved in the same folder in which `.xml` files are found


Add your class names and it's corresponding index values as follows:
```
class_names={}
class_names["accessory"] =0
class_names["top"]       =1
class_names["bottom"]    =2
class_names["bag"]       =3
class_names["shoes"]     =4
```


---
## License & Copyright

@ Teric-AI Team

***
