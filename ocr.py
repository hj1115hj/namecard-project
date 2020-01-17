import cv2, numpy as np
import time
from matplotlib import pyplot as plt



def imshow(tit, image) :
    plt.title(tit)    
    if len(image.shape) == 3 :
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    else :
        plt.imshow(image, cmap="gray")
    plt.show()

def ocr(file):
    frame = cv2.imread(file)
    roi = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray_blur = cv2.medianBlur(gray, 9)

    thr, mask = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    #침식후 팽창
    opened = cv2.morphologyEx(mask,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

                            ,iterations =10) 


    cont_img = opened.copy()
    contours, _ = cv2.findContours(cont_img, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    peri = cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,0.02* peri, True)
    frame_copy = frame.copy()
    arr = []
    for a in approx:
        arr.append(list(a[0]))

    pts1= [[0,0],[0,0],[0,0],[0,0]]
    arr=sorted(arr, key=lambda arr: [arr[0],arr[1]]) 
    pts1[0]=arr[0]
    pts1[2] = arr[1]
    pts1[1] = arr[2]
    pts1[3] = arr[3]
    pts1 =np.float32(pts1)
   

    height, width = frame.shape[:2]
    #print(height, width)

    pts2 =np.float32([[0,0], [width,0], [0,height],[width,height]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    #print(M)
    img_result = cv2.warpPerspective(frame,M,(width,height))
    cv2.imwrite("result_out2.jpg",img_result)

    gray=cv2.imread("result_out2.jpg",cv2.IMREAD_GRAYSCALE)
    #print(gray.shape)
    gray = cv2.medianBlur(gray, 5)
    out = cv2.adaptiveThreshold(gray,255,
                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY,21,2)
    #imshow('binary',out)
    cv2.imwrite('result_print.jpg',out)
    
    return "result_print.jpg"

