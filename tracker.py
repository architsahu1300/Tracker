import cv2
import time


tracker = cv2.TrackerCSRT_create()
cap = cv2.VideoCapture(0)
# TRACKER INITIALIZATION
success, frame = cap.read()
bbox = cv2.selectROI("Tracking",frame, False)
tracker.init(frame, bbox)
def drawBox(img,i):
    x, y, w, h = i
    cv2.rectangle(img, (x, y), ((x + 1), (y + 1)), (255, 0, 255), 10, 3 )
pos=  []
while True:

    timer = cv2.getTickCount()
    success, img = cap.read()
    img1 = cv2.flip(img, 180)
    success, bbox = tracker.update(img1)
    pos.append((int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])))
    for i in pos:
        drawBox(img1,i)
    cv2.imshow("Tracking", img1)
    if cv2.waitKey(1) & 0xff == ord('q'):
       break