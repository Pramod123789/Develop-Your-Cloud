import cv2
import os
import time
import uuid
from cvzone.HandTrackingModule import HandDetector

def ec2():
    os.system("aws ec2 run-instances --image-id ami-057752b3f1d6c4d6c --instance-type t2.micro")
    os.system("start msedge https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Instances:")
    time.sleep(3)
def s3(UUID):
    x = str(UUID)
    os.system(f"aws s3 mb s3://mybucket123{x} --region ap-south-1")
    os.system("start msedge https://s3.console.aws.amazon.com/s3/home?region=ap-south-1")
    time.sleep(3)



def hand():
    Handmodel = HandDetector(maxHands=1)
    cap = cv2.VideoCapture(0)
    while True:
        UUID  = uuid.uuid1().int
        status, photo = cap.read()
        hand,image = Handmodel.findHands(photo)
        cv2.imshow("myphoto", image)
        if hand:
            fingers = Handmodel.fingersUp(hand[0])
            if fingers == [0,1,1,0,0]:
                ec2()
            if fingers == [0,1,1,1,0]:
                s3(UUID)
            if fingers == [1,0,0,0,0]:
                os.system("start msedge https://chat.openai.com/")
                time.sleep(3)
            if fingers == [1,1,0,0,0]:
                break
        if cv2.waitKey(1) == 13:
            break
    cv2.destroyAllWindows()
    cap.release()
