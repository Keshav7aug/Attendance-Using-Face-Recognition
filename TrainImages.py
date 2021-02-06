import cv2,sys,os,time
import tkinter as tk
import numpy as np
from openpyxl import load_workbook,Workbook
from tkinter import ttk
from datetime import date
haar_file = face_classifier=r'/home/keshav/my_ten/venv/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)
width,height = (130,100)
def save_img_from_img():
    datasets = 'datasets'
    people = os.listdir('train')
    students = [(i.split(',')) for i in people]
    #print('p=',people)
    for _,i in enumerate(people):
        sub_data = "{}__{}".format(students[_][0],students[_][1])
        path = os.path.join(datasets,sub_data)
        if not os.path.isdir(path):
            os.mkdir(path)
        all_pics = os.listdir('train/{}'.format(i))
        count = 0
        for j in all_pics:
            im = cv2.imread('train/{}/{}'.format(i,j))
            gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.3,4)
            #print(faces)
            for (x,y,w,h) in faces:
                count+=1
                cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
                face = gray[y:y+h,x:x+w]
                #face_resize = cv2.resize(face,(width,height))
                cv2.imwrite('% s/%  s.png'%(path,count),face)
def save_img(name,enrol_no):
    datasets = 'datasets'
    sub_data = "{}__{}".format(name,enrol_no)
    path = os.path.join(datasets,sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)
    webcam = cv2.VideoCapture('video_2.mp4')
    count = 1
    while count<150:
        (_,im) = webcam.read()
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,4)
        #print(faces)
        for (x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
            face = gray[y:y+h,x:x+w]
            face_resize = cv2.resize(face,(width,height))
            cv2.imwrite('% s/%  s.png'%(path,count),face_resize)
            count+=1
        cv2.imshow(sub_data,im)
        key = cv2.waitKey(10)
        if key == 27:
            break
    webcam.release()
    cv2.destroyAllWindows()
save_img('Russell Peters','31215602717')
#name=input("Enter Name")
#Enrol=input("Enter Enrollment Number")
#save_img(name,Enrol)
# save_img_from_img()