import cv2 as cv

# เปิดกล้อง
cap = cv.VideoCapture(0)

# โหลดโมเดลตรวจจับใบหน้า
face_model = cv.CascadeClassifier('face-detect-model.xml')

while True:
    ret, img = cap.read()
    if not ret:
        break
    
    gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_model.detectMultiScale(gray_scale, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    
    # แสดงผลในหน้าต่าง
    cv.imshow('Face Detection', img)

    # กด 'q' เพื่อออกจากโปรแกรม
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
