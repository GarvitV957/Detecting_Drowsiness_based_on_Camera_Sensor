# Detecting_Drowsiness_based_on_Camera_Sensor





This program is used to detect drowsiness for any given person. In this program we check how long a person's eyes have been closed for. If the eyes have been closed for a long period i.e. beyond a certain threshold value, the program will alert the user by playing an alarm sound.

## Files
 - **Detects face and eye from a single image**

 - **Detects face and eye in a webcam feed by user**
 
 ![1](https://user-images.githubusercontent.com/79044490/198834999-d9aa86b0-5c76-4a65-a919-bc47f97dc8fb.png)
 
 - **drowsiness_detect.py**- This script detects if person is drowsy or not using webcam video feed

![2](https://user-images.githubusercontent.com/79044490/198835007-c5864d21-78d6-4024-ae65-9caa0a04d6c7.png)


 
 ## Requirements
 
IMPORTANT

    numpy==1.15.2
    dlib==19.16.0
    pygame==1.9.4
    imutils==0.5.1
    opencv_python==3.4.3.18
    streamlit
    secrets
    datetime
    pandas
    PIL
    image
    scipy
    imutils
    pygame

Use `pip install -r requirements.txt`to install the given requirements.

## Usage

### Drowsiness Detection
Run script using:

    streamlit run drowsiness_detect.py
