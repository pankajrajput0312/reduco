#!/usr/bin/env python
# coding: utf-8

# In[12]:


import cv2
import os
import numpy as np
import pandas as pd
import datetime
from weather_api import get_weather_data
from weight_detection import detect_weight
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials


# In[13]:


def get_date_time():
    x = datetime.datetime.now()
    x= str(x)
    date = x.split(" ")[0]
    time = x.split(" ")[1].split(".")[0]
    return (date,time)


# In[4]:


def vegetable_name(image):
    credentials = ApiKeyCredentials(in_headers = {"Prediction-Key":"bf595a2cb1854d988a1f9d26834cd4e2"})
    predictor =  CustomVisionPredictionClient("https://pankaj.cognitiveservices.azure.com/", credentials)
    cv2.imwrite('capture.png', image)
    with open("./capture.png", mode ='rb') as captured_image:
        # print("load image... and predict ")
        results = predictor.classify_image("c22b7174-dd80-457b-829e-4d05496aee33", "Iteration3", captured_image)
        vegetable = ""
        maxm_percentage = 0.0
        for prediction in results.predictions:
            if(prediction.probability> maxm_percentage):
                vegetable = prediction.tag_name
                maxm_percentage = prediction.probability
            # print("\t" + prediction.tag_name +": {0:.2f}%".format(prediction.probability * 100))
    return vegetable


# In[5]:


def update_file(vegetable, weight):
    '''
        write code for 
        1. check which csv for loading if no csv mske on that day we need to make another csv file and 
            start updating all in that csv file in new column
        
    
    '''
    from csv import writer
    minm_temp, maxm_temp, pressure, humidity, weather_desc, wind_spd = get_weather_data()
    date,time = get_date_time()
    # List 
    List=[date, time, vegetable, weight, minm_temp, maxm_temp, pressure, humidity, weather_desc, wind_spd]

  
    csv_file_name = str(date)+".csv"
    save_path = "./prediction_dataset/"+csv_file_name
    with open(save_path, 'a') as f_object:

        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)

        #Close the file object
        f_object.close()  
    # print("likh_diya")
    return


# In[11]:


import cv2

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
ret, image = camera.read()
if(ret == False):
    print("break")

vegetable_name = vegetable_name(image)
weight = detect_weight(image)
update_file(vegetable_name, weight)
camera.release()


# In[ ]:




