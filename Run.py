from sklearn.neighbors import KNeighborsClassifier

import cv2
import pickle
import csv
import time
from datetime import datetime
import os

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
with open('data/faces_data.pkl', 'rb') as f:
        faces = pickle.load(f)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(faces,names)

imgBackground=cv2.imread('AppBackground1.png')
start_x, start_y = 21, 175
end_x, end_y = 602, 564


COLUMN_NAME= ['NAME', 'TIME']

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    #frame = cv2.GaussianBlur(frame, (21, 21), 0)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1,-1)
        output= knn.predict(resized_img)
        ts=time.time()
        date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp=datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        file_exist=os.path.isfile('Attendance/'+ date + '.csv')

        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
        cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
        cv2.putText(frame, str(output[0]), (x,y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)
        attendance=[str(output[0]), str(timestamp)]
    imgBackground[start_y:end_y, start_x:end_x] = cv2.resize(frame, (end_x - start_x, end_y - start_y))
    cv2.imshow("frame", imgBackground)
    k = cv2.waitKey(1)
    if k == ord('q'):
        print(f"App Closed!")
        break
    elif k == ord('o'):
          if file_exist:
                with open("Attendance/" + date + ".csv", '+a', newline='') as csvfile:
                      writer=csv.writer(csvfile)
                      writer.writerow(attendance)
                csvfile.close()
                print(f"{output[0]}, your Attendance Added Sucesfully!")
          else:
                with open("Attendance/" + date + ".csv", '+a',  newline='') as csvfile:
                      writer=csv.writer(csvfile)
                      writer.writerow(COLUMN_NAME)
                      writer.writerow(attendance)
                csvfile.close()
                print(f"{output[0]}, your Attendance Added Sucesfully!")
                

          break
    

video.release()
cv2.destroyAllWindows()
