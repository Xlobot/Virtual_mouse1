from operator import index
from pickletools import pyunicode

import cv2
import mediapipe as mp
import pyautogui
from PIL.ImageChops import screen

cap =cv2.VideoCapture(0)
Hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 60)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
    output = Hand_detector.process(rgb_frame)
    Hands = output.multi_hand_landmarks
    print(Hands)
    if Hands:
        for Hand in Hands:
            drawing_utils.draw_landmarks(frame,Hand)
            landmarks = Hand.landmark
            for id, landmarks in enumerate(landmarks):

                    x = int(landmarks.x*frame_width)
                    y = int(landmarks.y*frame_height)
                    if id == 8:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(233,0,244), thickness=-1)
                        index_x = screen_width/frame_width*x
                        index_y = screen_height/frame_height*y
                        pyautogui.moveTo(index_x, index_y)


                    if id == 4:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(233,0,244), thickness=-1)
                        thumb_x = screen_width/frame_width*x
                        thumb_y = screen_height/frame_height*y
                        if abs(index_y-thumb_y) <20:
                           pyautogui.click()
                           pyautogui.sleep(1)
    cv2.imshow('mouse', frame)
    cv2.waitKey(1)