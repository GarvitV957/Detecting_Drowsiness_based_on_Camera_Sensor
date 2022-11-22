# Detecting_Drowsiness_based_on_Camera_Sensor

Fatigue is a safety problem that has not yet been deeply tackled mainly because of its nature. Fatigue, in general, is very difficult to measure or observe unlike alcohol and drugs, which have clear key indicators and tests that are available easily. Probably, the best solutions to this problem are awareness about fatigue-related accidents and promoting drivers to admit fatigue when needed. The former is hard and much more expensive to achieve, and the latter is not possible without the former as driving for long hours is very lucrative.

So, to tackle this problem, we have made an application which uses a camera sensor to take snaps of a driver driving a vehicle and gives him/her an alert signal in the real time. This application detects drowsiness of a driver based on the eye aspect ratio and whenever this ratio goes below some certain threshold, application gives an alerting sound.

![image](https://user-images.githubusercontent.com/79044490/202811431-77a6fa76-693d-4a55-aa3c-16ededd10d11.png)

There are many products out there that provide the measure of fatigue level in the drivers which are implemented in many vehicles. The driver drowsiness detection system provides the similar functionality but with better results and additional benefits. Also, it alerts the user on reaching a certain saturation point of the drowsiness measure.

## Hardware Requirements
WEBCAM and LAPTOP with basic hardware


## Features of Application

This application detects drowsiness of a driver based on the eye aspect ratio and whenever this ratio goes below some certain threshold, application gives an alerting sound. So, our application is supposed to work in such a way that a user can register and login such that the system can determine the base eye-aspect-ratio of a person signed-in (as the eye aspect ratio for alertness and drowsiness depends on person to person).

Here are the features of our application tested by our team members showing different aspects of the Drowsiness Detection System:

1.	Home Page: It has several pages which includes Home, Sign-up, Login, Warnings and Know more.

![1](https://user-images.githubusercontent.com/79044490/202721074-288ebc3c-f494-4fcf-96f9-4e794bd5183c.png)

2.	Overview of Sign-up/Login page for user: When a user signs up for the first time, he/she must take his/her snap in the camera so that the eye aspect ratio of that can be saved in the database for future reference when that person comes afterwards.

![4](https://user-images.githubusercontent.com/79044490/202721207-f6be1737-4ed7-4c77-957f-5adbaed6f601.png)
![3](https://user-images.githubusercontent.com/79044490/202721166-f35ad40f-dc3e-4b89-82b0-f82b1b54a4be.png)

After successful sign-up, user has to login into the system, and must select the STRART/STOP check box to start the process.

![7](https://user-images.githubusercontent.com/79044490/202721298-b68df2be-a20c-43b9-a004-813bb97aedb3.png)

3.	Whenever a user feels drowsy or sleepy, the camera detects by capturing the eye aspect ratio, that is, whenever user’s eyes close greater than 70% of size of user’s eyes for more than 25 frames, the buzzer will start buzzing.

![8](https://user-images.githubusercontent.com/79044490/202721321-93087610-f67b-47a7-a955-974742619132.png)

4.	Whenever the alerting/buzzer sound is played, entry for time, e and Username is filled in Warning page. Later, if user wants to see the time of warnings, the user can go to warning page and can find time, date of every warning of a user.

![9](https://user-images.githubusercontent.com/79044490/202721343-3d4971ea-d7c3-468c-bc72-005fbf9e0bff.png)

 
 ## Requirements

    dlib==19.24.0
    imutils==0.5.3
    numpy==1.18.5
    opencv_python==4.3.0.36
    pandas==1.0.5
    Pillow==9.3.0
    pygame==2.1.2
    scipy==1.5.1
    streamlit==1.9.2

Use `pip install -r requirements.txt`to install the given requirements.

![image](https://user-images.githubusercontent.com/79044490/202812172-41c62f89-ed68-42da-9300-1f1fdc609a23.png)


## Below are the steps of Installation:

To run this website on local system, need to follow the below steps one after the other.
1.	First of all clone (https://github.com/Pranav-Programmer/Detecting_Drowsiness_based_on_Camera_Sensor) this GitHub repository on the local system by using (git clone https://github.com/Pranav-Programmer/Detecting_Drowsiness_based_on_Camera_Sensor) this command, if there is any difficulty to run the command on local system then just download the zip file from GitHub and extract it into any empty folder.

2.	Once the repository gets cloned or extracted then next step is to install python on local system, just download python file suitable for your system from this (https://www.python.org/downloads/ ) link.

3.	After the installation of python, we need to install anaconda to run the streamlit library on our local system. So, download it according to your system from (https://www.anaconda.com/products/distribution) this links. 

4.	After that we need to install all the python library on our local system. Go to (https://cmake.org/download/) this link and download cmake file for your system and install it after that and give it a path after installation. There is a requirements.txt file in project repository, just run (pip install -r requirements.txt) in the same project folder where project repository is cloned or extracted this will install all the required python library in local system.

5.	Once you done all this, run this project by using (streamlit run Detecting_Drowsiness.py) this this command. This command run this project on browser, and it generates one network link which can be send to other to run the same website while your connected with network.

Run this project using:

    streamlit run drowsiness_detect.py
    
## Below are the steps of Working:

![10](https://user-images.githubusercontent.com/79044490/202721371-8e731d9f-3e41-42e5-961d-9ee3534e3605.png)

##    Conclusion

It completely meets the objectives and requirements of the system. The framework has achieved an unfaltering state where all the bugs have been disposed of. The framework cognizant clients who are familiar with the framework and comprehend its focal points and the fact that it takes care of the issue of stressing out for individuals having fatigue-related issues to inform them about the drowsiness level while driving.

The model can be improved incrementally by using other parameters like blink rate, yawning, state of the car, etc. If all these parameters are used it can improve the accuracy by a lot. 

We plan to further work on the project by adding a sensor to track the heart rate in order to prevent accidents caused due to sudden heart attacks to drivers. 

Same model and techniques can be used for various other uses like Netflix and other streaming services can detect when the user is asleep and stop the video accordingly. It can also be used in application that prevents user from sleeping.

 ## contributors

    Pranav Dharme
    Garvit Verma
    Dev Prajapat	
    Devansh Agrawal
    Ujjawal Khadanga
    Akhil Dekarla
    Shreesha
