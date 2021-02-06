import cv2
import numpy as np
import json
import os
haar_file = face_classifier=r'/home/keshav/my_ten/venv/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)
width,height = (130,100)
def opener(name):
    name="model_files/{}".format(name)
    try:
        f = open(name)
        D=json.load(f)
    except:
        D={}
    return D

def saver(data,name):
    with open('model_files/{}.json'.format(name), 'w') as f:
        json.dump(data, f)

def train(iD):
    oldiD = iD
    model = cv2.face.LBPHFaceRecognizer_create()
    datasets = 'datasets'
    images,labels,names,enrol,iD = ([],[],{},{},iD)
    for name in os.listdir(datasets):
        path="{}/{}".format(datasets,name)
        names[iD]=name.split('__')[0]
        enrol[iD]=name.split('__')[1]
        for pic in os.listdir(path):
            #print(pic)
            images.append(cv2.imread("{}/{}".format(path,pic),0))
            labels.append(iD)
        iD+=1
    if iD == oldiD:
        return iD,names,enrol
    images,labels = [np.array(lis) for lis in (images,labels)]
    try:
        model.read('model_files/model.XML')
    except Exception as E:
        print(E)
    model.update(images,labels)
    model.write('model_files/model.XML')
    return iD,names,enrol
names = opener('names.json')
enrol=opener('enrol.json')
oldiD = len(names)
oldiD,newNames,newEnrol=train(oldiD)

names.update(newNames)
enrol.update(newEnrol)
saver(names,'names')
saver(enrol,'enrol')
print('done')