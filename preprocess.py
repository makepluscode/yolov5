from glob import glob
img_list = glob('/home/bginess/yolov5/dataset/export/images/*.jpg')
print(len(img_list)) #2971

from sklearn.model_selection import train_test_split
train_img_list, val_img_list = train_test_split(img_list, test_size=0.2, random_state=2000) 
print(len(train_img_list), len(val_img_list))  #2376 595

# create txt files
with open('/home/bginess/yolov5/dataset/train.txt', 'w') as f:
  f.write('\n'.join(train_img_list) + '\n')
with open('/home/bginess/yolov5/dataset/val.txt', 'w') as f:
  f.write('\n'.join(val_img_list) + '\n')

import yaml
with open('/home/bginess/yolov5/dataset/data.yaml', 'r') as f:
  data = yaml.load(f)
print(data)
 
data['train'] = '/home/bginess/yolov5/dataset/train.txt'
data['val'] = '/home/bginess/yolov5/dataset/val.txt'
 
with open('/home/bginess/yolov5/dataset/data.yaml', 'w') as f:
  yaml.dump(data, f)

print(data)
