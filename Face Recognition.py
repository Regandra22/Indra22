import cv2 
kamera  = cv2.VideoCapture(0)
while True:
    mulai, bingkai = kamera.read()
    cv2.imshow('kameraku',bingkai)
    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break 
kamera.release
cv2.destroyAllWindows()
