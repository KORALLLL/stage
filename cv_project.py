import cv2
import numpy as np
import cvlib as cv
from cvlib.object_detection import draw_bbox


cap = cv2.VideoCapture('C:/Users/Kirill/Videos/detected.mp4')
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
videoOut = cv2.VideoWriter('vid2.avi', cv2.VideoWriter_fourcc(*"MJPG"), 20, (w,h))
label=[]

for i in range(10):
    s, img =cap.read()
    if s == True:
        videoOut.write(img)
        cv2.waitKey(16)

    box1, label1, count1 = cv.detect_common_objects(img)
    for i in range(len(label1)):
        if label1[i]!='person':
            if label1[i] not in label:
                label.append(label1[i])
            else:
                if label1.count(label1[i])==label.count(label1[i]):
                    pass
                else:
                    label.append(label1[i])
print(label)
    


while True:
    flag=0
    ret, img = cap.read()
    if ret == False:
        break


    box_t, label_t, count_t = cv.detect_common_objects(img)
    b, l, c = [], [], []

    

    for i in range(len(label_t)):
        if label_t[i]!='person' and label_t[i]!='chair' and label_t[i]!='dining table':
            if label_t[i] not in label:
                b.append(box_t[i])
                l.append(label_t[i])
                c.append(count_t[i])
                flag=1
                break
    output = draw_bbox(img, b, l, c)
    if flag==1:
        cv2.putText(output, 'WARNING. POSSIBLY LOST ITEM', (10,100), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 5)
    
    if ret == True:
        videoOut.write(output)
    cv2.imshow('test', output)

    if cv2.waitKey(16) & 0xFF== ord('q'):
        break


cap.release()
videoOut.release()
cv2.destroyAllWindows()


