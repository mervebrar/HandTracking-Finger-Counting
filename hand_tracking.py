import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHand= mp.solutions.hands

hands=mpHand.Hands()

mpDraw= mp.solutions.drawing_utils

pTime=0
cTime=0


while True:
    success, img = cap.read()
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results= hands.process(imgRGB)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHand.HAND_CONNECTIONS)

            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c =img.shape

                cx, cy = int(lm.x*w), int(lm.y*h)

                #wrist
                if id== 4 :
                    cv2.circle(img,(cx,cy), 9,(255,0,0), cv2.FILLED, )

    #fps
    cTime= time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,"FPS: " + str(int(fps)), (75,150), cv2.FONT_HERSHEY_PLAIN,8,(255,0,50))
    cv2.imshow("img", img)
    cv2.waitKey(1)


