# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:05:18 2022

@author: PC
"""

import os
import json
from PIL import Image
class converter():
    def __init__(self, path):
        self.path = path
        self.img_id = 0
        self.amn_id = 0
        self.images = []
        self.annotations = []


    def getImage(self, img_path):
        name = img_path.split("/")[-1].split('.')[0]
        img = Image.open(f'/home/noman/datanew/private_test_set_1/test_set_1/images/{name}.jpg')
        w, h = img.size
        return {
            "file_name":f'{name}.jpg',
            "id":self.img_id,
            "width":w,
            "height":h
        }, img
# 0 0.403906 0.479514 0.0445312 0.0618056 0.90625
    def getAnn(self, detections, img_id, img:Image):
        data = detections.split(' ')
        if len(data)<2:
            return {
            "image_id": img_id,
            "bbox": [
                0,
                0,
                0,
                0
            ],
            "category_id":0,
            "id": 0,
            "confidence": 0
        }
        print(data)
        _class = int(data[0])
        x = float(data[1])*1280
        y = float(data[2])*720
        w = float(data[3])*1280 
        h = float(data[4])*720 
        acc = data[5]
        return {
            "image_id": img_id,
            "bbox": [
                x-w/2,
                y-h/2,
                w,
                h
            ],
            "category_id": _class+1,
            "id": self.amn_id,
            "confidence": float(acc)
        }

    def saveAnn(self, detections, img_id, img):
        self.annotations.append(self.getAnn(detections, img_id, img))
        self.amn_id += 1
    
    def saveImg(self, img):
        img_tag , img = self.getImage(img)
        self.images.append(img_tag)
        self.img_id += 1
    def process(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                img_path = os.path.join(root, file)
                img = self.saveImg(img_path)
                with open(img_path, 'r') as f: data = f.readlines()
                for detections in data:
                    self.saveAnn(detections, self.img_id-1, img)

    def dump(self):
        with open('/home/noman/yolov5x/mansoor_5.json', 'w') as f: json.dump({
            'images':self.images,
            "annotations" :self.annotations,
            'categories':[
                {"supercategory": "none", "id": 1, "name": "Car"}, 
                {"supercategory": "none", "id": 2, "name": "Truck"}, 
                {"supercategory": "none", "id": 3, "name": "StopSign"}, 
                {"supercategory": "none", "id": 4, "name": "traffic_lights"}]
        }, f, indent=0)
if __name__ == '__main__':
    _converter = converter('runs/detect/exp5/labels')
    _converter.process()
    _converter.dump()
    print(_converter.amn_id)
