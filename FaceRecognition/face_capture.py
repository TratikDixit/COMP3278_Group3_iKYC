import cv2
import os
import pickle
import FaceRecognition.train as train
import mysql.connector

faceCascade = cv2.CascadeClassifier('../FaceRecognition/haarcascade/haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

# Specify the `user_name` and `NUM_IMGS` here.
def main(details):
    myconn = mysql.connector.connect(host="localhost", user="root", passwd="Lamcy#108", database="facerecognition")
    cursor = myconn.cursor()

    user_name = details["username"]
    password = details["password"]
    first_name = details["firstName"]
    middle_name = details["middleName"]
    last_name = details["lastName"]
    telegram_chat_id = details["telegramChatID"]

    NUM_IMGS = 20
    if not os.path.exists('../data/{}'.format(user_name)):
        os.mkdir('../data/{}'.format(user_name))

    cnt = 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (80, 50)
    fontScale = 1
    fontColor = (102, 102, 225)
    lineType = 2

    # Open camera
    while cnt <= NUM_IMGS:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        msg = "Saving {}'s Face Data [{}/{}]".format(user_name, cnt, NUM_IMGS)
        cv2.putText(frame, msg,
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    lineType)


        # Display the resulting frame
        cv2.imshow('Video', frame)
        # Store the captured images in `data/Jack`
        cv2.imwrite("../data/{}/{}{:03d}.jpg".format(user_name, user_name, cnt), frame)
        cnt += 1

        key = cv2.waitKey(100)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
    train.main()

    #add user to database
    insert = "INSERT INTO `Customer` VALUES ('%s', '%s', '%s', '%s', '%s', 'Welcome!', '%s');"
    name = cursor.execute(insert%(user_name, password, first_name, middle_name, last_name, telegram_chat_id))
    myconn.commit()
