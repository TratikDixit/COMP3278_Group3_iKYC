import urllib
import numpy as np
import mysql.connector
import cv2
import pyttsx3
import pickle
from datetime import datetime
import sys
import os


def main():
    # dictionary that returns user data or error message
    return_dict = {'success' : False,
                   'message' : 'Could not recognize face, please try again or create a new account if you are a new '
                               'user '
                   }
    # 1 Create database connection
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="Lamcy#108", database="facerecognition")
    date = datetime.utcnow()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cursor = myconn.cursor()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # 2 Load recognize and read label from model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("../FaceRecognition/train.yml")

    labels = {"person_name": 1}
    with open("../FaceRecognition/labels.pickle", "rb") as f:
        labels = pickle.load(f)
        labels = {v: k for k, v in labels.items()}
    print(labels)
    # create text to speech
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 175)

    # Define camera and detect face
    face_cascade = cv2.CascadeClassifier('../FaceRecognition/haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    # 3 Open the camera and start face recognition
    max_iterations = 50
    iterations = 0
    while iterations < max_iterations:
        success = False
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=3)

        for (x, y, w, h) in faces:
            #print(x, w, y, h)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = recognizer.predict(roi_gray)

            # 3.1 If the face is recognized
            if conf >= 30:
                success = True
                # print(id_)
                # print(labels[id_])
                font = cv2.QT_FONT_NORMAL
                id = 0
                id += 1
                name = labels[id_]
                current_name = name
                color = (255, 0, 0)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

                # Find the customer's information in the database.
                select = "SELECT first_name, middle_name, last_name FROM " \
                         "Customer WHERE username='%s'" % (
                             name)
                name = cursor.execute(select)
                result = cursor.fetchall()
                data = "error"

                for x in result:
                    data = x

                # If the customer's information is not found in the database
                if data == "error":
                    return_dict = {
                        'success': False,
                        'message': f"The customer {current_name} is NOT FOUND in the database. Please create a new "
                                   f"account "
                    }

                # If the customer's information is found in the database
                else:
                    """
                    Implement useful functions here.
                    
    
                    """

                    # add extra return values and SQL statements to customize welcome message and load the data
                    return_dict = {
                        'success': True,
                        'name' : current_name,
                        'cur_date' : date
                    }

                    # engine.runAndWait()


            # 3.2 If the face is unrecognized
            else:
                color = (255, 0, 0)
                stroke = 2
                font = cv2.QT_FONT_NORMAL
                cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
                return_dict = {
                    'success' : False,
                    'message' : 'Face is unrecognized'

                }
                # engine.runAndWait()

        cv2.imshow('iKYC System', frame)
        k = cv2.waitKey(20) & 0xff
        if k == ord('q'):
            break
        iterations += 1
        if success:
            break
    cap.release()
    cv2.destroyAllWindows()
    return return_dict

if __name__ == '__main__':
    main()
