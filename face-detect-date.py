import cv2 as cv
import datetime

cap = cv.VideoCapture(0)
face_model = cv.CascadeClassifier('face-detect-model.xml')

while True:
    ret, img = cap.read()
    if not ret:
        break
    
    gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_model.detectMultiScale(gray_scale, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        
        # บันทึกภาพเมื่อพบใบหน้า
        face_img = img[y:y+h, x:x+w]
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        cv.imwrite(f"face_{timestamp}.jpg", face_img)
    
    cv.imshow('Face Detection', img)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
