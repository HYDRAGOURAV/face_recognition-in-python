import cv2

Face_capture = cv2.CascadeClassifier("C:/Users/GOURAV PAWANKAR/AppData/Roaming/Python/Python312/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)

while True:
    ret, Video_data = video_cap.read()
    col = cv2.cvtColor(Video_data,cv2.COLOR_RGB2GRAY)
    Faces = Face_capture.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags= cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in Faces:
        cv2.rectangle(Video_data, (x,y), (x+w,y+h), (0,255,0),2)

    cv2.imshow("video_Live",Video_data)
    if cv2.waitKey(10)==ord("a"):
        break
video_cap.release()

# Press a for exit Program 
# i Give My Own File Path in This Program You Can change The Path According to Your System 