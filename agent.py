import cv2
import os
from datetime import datetime as dt
import requests
# imported the opensource library OpenCV , OS , datetime etc.  

print("--- Fortify Agent Started ---")

cap = cv2.VideoCapture(0) 
# cv2.videoCapture(0) --> inbuilt function of cv2 lib to capture the video using webcame - (0) indicates default 
# camera 


if not cap.isOpened():
    print("Camera Sensor: FAILED TO INITIALIZE. (index -1)")
    exit()
else:
    print("Camera Sensor: INITIALIZED (Index 0)")
# basic if else statments to check the access of camera 

return_1 , frame = cap.read()
# .read function returns True/False and one single frame captured by webcam

if return_1 != 1:
    print("Capture Status: FAILED")
    exit()

timestamp = dt.now().strftime("%Y-%m-%d_%H-%M-%S") # buitin function of datetime, %Y - year , %d = date
filename = f"footage_{timestamp}.jpg" 

folder_name = "ALL_footages"
if not os.path.exists(folder_name):  
    # used os module to create a folder/directory
    os.mkdir(folder_name)

filepath = os.path.join(folder_name,filename)
# used builtin function .path.join to join two strings pointer a path 

cv2.imwrite(filepath,frame)
# implemented .imwrite to create a file at filepath , which included frame 




SERVER_URL = "http://127.0.0.1:2000/uploads"

with open(filepath, "rb") as img_file:
    files = {
        "img": img_file
    }

    response = requests.post(SERVER_URL, files=files)

print("Server Response:", response.status_code)
print("Server Data:", response.json())


print("Capture Status: SUCCESS")
print("Local Storage:", filepath)
# final Statements 

cap.release()
# released webcam so that it can be used somewhere else. 
cv2.destroyAllWindows()





