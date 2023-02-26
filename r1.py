import cv2
import numpy as np
import os
import pandas as pd
import datetime,time

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainertrainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

id = 1


names = ['none','sathya', 'ram', 'nandha', 'Virat']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
df=pd.DataFrame({"Name":"sathya","attendance":"Absent"},index=[0])
df1=pd.DataFrame({"Name":"ram","attendance":"Absent"},index=[1])
df2=pd.DataFrame({"Name":"dhiwin","attendance":"Absent"},index=[2])
df3=pd.DataFrame({"Name":"Rohit","attendance":"Absent"},index=[3])
x=1
while True:

    ret, img =cam.read()
    #img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    
    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])        
                

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            id1 = names[id]
            confidence = "  {0}%".format(round(100 - confidence))            
                                    
        else:
            id1 = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        cv2.putText(img, str(id1), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        if(id1=="sathya"):
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            df=pd.DataFrame({"Name":"sathya","attendance":"Present","time":timeStamp},index=[0])
            
        if(id1=="Ram"):
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            df1=pd.DataFrame({"Name":"ram","attendance":"Present","time":timeStamp},index=[1])
        if(id1=="dhiwin"):
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            df2=pd.DataFrame({"Name":"dhiwin","attendance":"Present","time":timeStamp},index=[2])
          
        if(id1=="Rohit"):
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            df3=pd.DataFrame({"Name":"Rohit","attendance":"Present","time":timeStamp},index=[3])
        else:
            m=0
               
        
    
    cv2.imshow('camera',img)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
dft=pd.concat([df,df1,df2,df3])
print(dft)
cam.release()
cv2.destroyAllWindows()
ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
Hour, Minute, Second = timeStamp.split(":")
fileName = "Attendance"+os.sep+"Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
dft.to_csv(fileName,index=False)
print("file saved")
import yagmail
import os
import datetime
sub = "Attendance Report for " + str(date)
"""# mail information
yag = yagmail.SMTP("nandhakumar220602@gmail.com","nandha@2206")

# sent the mail
yag.send(
    to=["nandhakumar11214@gmail.com","ibrahimrasith@gmail.com"],
    subject="Attendance for "+date, # email subject
    contents="Attendance for "+date,  # email body
    attachments= fileName  # file attached
)
print("Email Sent!")"""
a=dft[dft["attendance"]=="Absent"]
b=a["Name"]
c=b.values.tolist()
def mails(name,mail):
    yag = yagmail.SMTP("nandhakumar220602@gmail.com","nandha@2206")
    yag.send(
        to=mail,
        subject="Notification for absent on "+date, # email subject
        contents=name+" Notification mail to alert you are absent today,date: "+date,  # email body
        )
    
if 'Ibrahim' in c :
    mails("ibrahim","ibrahimrasith@gmail.com")
    print("absent mail sent to Ibrahim")
if 'Nandha' in c :
    mails("Nandha","nandhakumar11214@gmail.com")
    print("absent mail sent to Nandha")
if 'Virat' in c :
    print("absent mail sent to Virat")
if 'Rohit' in c :
    print("absent mail sent to Rohit")


        








    
