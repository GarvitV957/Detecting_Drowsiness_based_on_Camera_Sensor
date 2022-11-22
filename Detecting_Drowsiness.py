#Import WEB library
import streamlit.components.v1 as components
from secrets import choice
import streamlit as st
#Import necessary libraries
from datetime import datetime
import pandas as pd
import numpy as np
import cv2
from PIL import Image
import os
import time
from scipy.spatial import distance
from imutils import face_utils
import pygame #For playing sound
import dlib
import sqlite3
import Database
import pyttsx3

st.markdown("""
<div class="container" style="background-color: #33FFFF; width: 800px; ">
    <nav class="navbar navbar-expand-lg bg-light" style="background-color: #33FFFF">
      <div class="container-fluid" style="background-color: #ffffff; border: 1px solid white; opacity: 0.6;">
        <a class="navbar-brand" href="index.php"></a> <button onclick="topFunction()" id="myBtn" class="myBtn" title="Go to top"><i style="color: black;" class="fa-solid fa-bars"></i></button>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" style="color: Green; font-weight: bold; margin-right: 20px;"><img src="https://img.icons8.com/fluency-systems-filled/48/000000/about-us-male.png" style="width: 24px;"/>@--____________________ Detecting Drowsiness based on Camera Sensor _____________________--</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    </div>

""", unsafe_allow_html=True)

FRAME_WINDOW = st.image([]) #frame window

hhide_st_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hhide_st_style, unsafe_allow_html=True) #hide streamlit menu

db = Database.Database()

def main():

    col1, col2, col3 = st.columns(3) #columns
    menu = ["HOME","Signup","Login","Warnings", "Know More"] #menu
    choice = st.sidebar.selectbox("Menu", menu) #sidebar menu

    pygame.mixer.init()
    pygame.mixer.music.load('audio/warn.mp3')
    engine = pyttsx3.init()
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #capture video

    if choice == "Home" :
        st.subheader("Home")
    elif choice == "Login" :
      st.subheader("Login Section")

      username = st.sidebar.text_input("User Name")
      password = st.sidebar.text_input("Password",type='password')
      if st.sidebar.checkbox("Login"):
            db.create_usertable()
            result = db.login_user(username, password)
            if result: 
                run = st.checkbox("START / STOP") #checkbox
                if run == True:
                  
                  #Minimum threshold of eye aspect ratio below which alarm is triggerd
                  EYE_ASPECT_RATIO_THRESHOLD = 0.27
                  
                  #Minimum consecutive frames for which eye ratio is below threshold for alarm to be triggered
                  EYE_ASPECT_RATIO_CONSEC_FRAMES = 25
                  
                  #COunts no. of consecutuve frames below threshold value
                  COUNTER = 0
                  
                  #Load face cascade which will be used to draw a rectangle around detected faces.
                  face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
                  
                  #This function calculates and return eye aspect ratio
                  def eye_aspect_ratio(eye):
                      A = distance.euclidean(eye[1], eye[5])
                      B = distance.euclidean(eye[2], eye[4])
                      C = distance.euclidean(eye[0], eye[3])
                  
                      ear = (A+B) / (2*C)
                      return ear
                  
                  #Load face detector and predictor, uses dlib shape predictor file
                  detector = dlib.get_frontal_face_detector()
                  predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
                  
                  #Extract indexes of facial landmarks for the left and right eye
                  (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
                  (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']
                  
                  #Start webcam video capture
                  #video_capture = cap.read()
                  
                  #Give some time for camera to initialize(not required)
                  #time.sleep(2)

                  while(True):
                      #Read each frame and flip it, and convert to grayscale
                      ret, frame = cap.read()
                      frame = cv2.flip(frame,1)
                      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                  
                      #Detect facial points through detector function
                      faces = detector(gray, 0)
                  
                      #Detect faces through haarcascade_frontalface_default.xml
                      face_rectangle = face_cascade.detectMultiScale(gray, 1.3, 5)
                  
                      #Draw rectangle around each face detected
                      for (x,y,w,h) in face_rectangle:
                          cv2.rectangle(frame,(x,y),(x+w,y+h),(255,153,140),2)
                  
                      #Detect facial points
                      for face in faces:
                  
                          shape = predictor(gray, face)
                          shape = face_utils.shape_to_np(shape)
                  
                          #Get array of coordinates of leftEye and rightEye
                          leftEye = shape[lStart:lEnd]
                          rightEye = shape[rStart:rEnd]
                  
                          #Calculate aspect ratio of both eyes
                          leftEyeAspectRatio = eye_aspect_ratio(leftEye)
                          rightEyeAspectRatio = eye_aspect_ratio(rightEye)
                  
                          eyeAspectRatio = (leftEyeAspectRatio + rightEyeAspectRatio) / 2
                  
                          #Use hull to remove convex contour discrepencies and draw eye shape around eyes
                          leftEyeHull = cv2.convexHull(leftEye)
                          rightEyeHull = cv2.convexHull(rightEye)
                          cv2.drawContours(frame, [leftEyeHull], -1, (190, 255, 70), 1)
                          cv2.drawContours(frame, [rightEyeHull], -1, (190, 255, 70), 1)
                  
                          #Detect if eye aspect ratio is less than threshold
                          if(eyeAspectRatio < EYE_ASPECT_RATIO_THRESHOLD):
                              COUNTER += 1
                              #If no. of frames is greater than threshold frames,
                              if COUNTER >= EYE_ASPECT_RATIO_CONSEC_FRAMES:
                                  #pygame.mixer.music.play(-1)
                                  engine.say("WAKE UP!!!! Don't close your eyes")
                                  engine.runAndWait()
                                  cv2.putText(frame, "Don't close your eyes", (100,470), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
                                  #time.sleep(2)
                                  with open('Warnings.csv', 'r+') as f:
                                        now = datetime.now()
                                        myDataList = f.readlines()
                                        dtString = now.strftime('%H:%M:%S')
                                        dStr = now.strftime('%d:%m:%Y')
                                        f.writelines(f'\n{username}{dtString},{dStr}')
                          else:
                              pygame.mixer.music.stop()
                              COUNTER = 0
                  
                          FRAME_WINDOW.image(frame)
                          cv2.waitKey(1)
            
                else:
                   pass
            else:
                st.warning("Incorrect Username/Password")
        

    elif choice == "Signup" :
        st.subheader( "Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input ("Password" , type='password')
        if st.checkbox("Capture eyes"):

          #Minimum threshold of eye aspect ratio below which alarm is triggerd
                  EYE_ASPECT_RATIO_THRESHOLD = 0.27
                  
                  #Minimum consecutive frames for which eye ratio is below threshold for alarm to be triggered
                  EYE_ASPECT_RATIO_CONSEC_FRAMES = 25
                  
                  #COunts no. of consecutuve frames below threshold value
                  COUNTER = 0
                  
                  #Load face cascade which will be used to draw a rectangle around detected faces.
                  face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
                  
                  #This function calculates and return eye aspect ratio
                  def eye_aspect_ratio(eye):
                      A = distance.euclidean(eye[1], eye[5])
                      B = distance.euclidean(eye[2], eye[4])
                      C = distance.euclidean(eye[0], eye[3])
                  
                      ear = (A+B) / (2*C)
                      return ear
                  
                  #Load face detector and predictor, uses dlib shape predictor file
                  detector = dlib.get_frontal_face_detector()
                  predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
                  
                  #Extract indexes of facial landmarks for the left and right eye
                  (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
                  (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']
                  
                  #Start webcam video capture
                  #video_capture = cap.read()
                  
                  #Give some time for camera to initialize(not required)
                  #time.sleep(2)
                  
                  while(True):
                      #Read each frame and flip it, and convert to grayscale
                      ret, frame = cap.read()
                      frame = cv2.flip(frame,1)
                      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                      cv2.putText(frame, "Look into the camera for 10 second", (0,470), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2,)
                      #Detect facial points through detector function
                      faces = detector(gray, 0)
                      
                      #Detect faces through haarcascade_frontalface_default.xml
                      face_rectangle = face_cascade.detectMultiScale(gray, 1.3, 5)
                  
                      #Draw rectangle around each face detected
                      for (x,y,w,h) in face_rectangle:
                          cv2.rectangle(frame,(x,y),(x+w,y+h),(255,153,140),2)
                  
                      #Detect facial points
                      for face in faces:
                  
                          shape = predictor(gray, face)
                          shape = face_utils.shape_to_np(shape)
                  
                          #Get array of coordinates of leftEye and rightEye
                          leftEye = shape[lStart:lEnd]
                          rightEye = shape[rStart:rEnd]
                  
                          #Calculate aspect ratio of both eyes
                          leftEyeAspectRatio = eye_aspect_ratio(leftEye)
                          rightEyeAspectRatio = eye_aspect_ratio(rightEye)
                  
                          eyeAspectRatio = (leftEyeAspectRatio + rightEyeAspectRatio) / 2
                  
                          #Use hull to remove convex contour discrepencies and draw eye shape around eyes
                          leftEyeHull = cv2.convexHull(leftEye)
                          rightEyeHull = cv2.convexHull(rightEye)
                          cv2.drawContours(frame, [leftEyeHull], -1, (190, 255, 70), 1)
                          cv2.drawContours(frame, [rightEyeHull], -1, (190, 255, 70), 1)

                          FRAME_WINDOW.image(frame)
                          cv2.waitKey(1)

        if st.button("Signup"):
            db.create_usertable( )
            db.add_userdata(new_user, new_password)
            st.success("You have successfully created an valid Account")
            st.info("Go to Login Menu to login")

    #read data menu
    elif choice == 'Warnings':
        with col2:
            df = pd.read_csv('Warnings.csv')
            st.subheader("WARNINGS TIME AND DATE")
            df = pd.read_csv('Warnings.csv')
            st.write(df)
    
    elif choice == 'HOME':
        st.markdown("""
    <div class="container" style="background-color: #33FFFF00; width: 800px; ">
    <nav class="navbar navbar-expand-lg bg-light" style="background-color: #33FFFF00">
      <div class="container-fluid" style="background-color: #33FFFF">
        <a class="navbar-brand" href="index.php"></a> <button onclick="topFunction()" id="myBtn" class="myBtn" title="Go to top"><i style="color: black;" class="fa-solid fa-bars"></i></button>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" style="color: Green; font-weight: bold; margin-right: 20px;">@--____________________ Detecting Drowsiness based on Camera Sensor _____________________--</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    </div>
    
    """, unsafe_allow_html=True)
        with col1:
            st.image("DD.jpg",width=800, caption="Safety is always choise of every wise, because they doesn't close eyes, so be wise.") 
    
    elif choice == "Know More":
       st.header("Read below to understand the working of website")
       st.markdown("o- On each page you find sidebar menu on left side, from there you can nevigate to other pages.")
       st.markdown("o- First you need to go to Signup page and there you need to create account by providing username and strong password along with 10 second video of your face to capture your eyes by clicking on capture eyes checkbox, after 10 second uncheck the checkbox and click on signup button to register yourself.")
       st.markdown("o- Then to start capturing your face and eyes for drowsiness detection while driving go to login page below the sign up page and login with your username and password then click on START / STOP checkbox, this will start the camera and start capturing your eyes.")
       st.markdown("o- Remember one thing if your eyes closes greater than 70 percent of size of your eyes for more than 3 second then buzzer will start buzzing and entry for same with time, date and username is filled in warning page which is below the login page.")
       st.markdown("o- To see the warnings given to the user go to warnings page there you find name of user, time and date of every warning.")
       st.markdown("o- Below warnings page know more page is there to read about how to use this website.")
       st.markdown("o- Thank you for using this Drowsiness Detection Syatem, we will made this system more efficient and more user friendly with time.")

if __name__ == '__main__':
    main()
    