import cv2 as cv
import numpy as np
import os
import datetime

# โหลดโมเดลตรวจจับใบหน้า
face_model = cv.CascadeClassifier('face-detect-model.xml')

# ฟังก์ชันเก็บข้อมูลใบหน้าของผู้ใช้
def collect_faces(user_id):
    faces = []
    labels = []
    cap = cv.VideoCapture(0)
    count = 0
    
     # แปลง user_id ให้เป็น int32 ก่อนใส่ใน labels
    try:
        user_id = np.int32(user_id)  # แปลง user_id ให้เป็น int32
    except ValueError:
        print("Invalid user ID!")
        return [], []
    
    while True:
        ret, img = cap.read()
        if not ret:
            break
        
        gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces_detected = face_model.detectMultiScale(gray_scale)
        
        for (x, y, w, h) in faces_detected:
            face = gray_scale[y:y+h, x:x+w]
            faces.append(face)
            labels.append(user_id)
            count += 1
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        cv.imshow("Collecting faces", img)
        
        # หยุดเมื่อเก็บข้อมูลครบ
        if count >= 30:
            break
    
    cap.release()
    cv.destroyAllWindows()

    return faces, labels

# ฟังก์ชันฝึกสอนโมเดลการจำแนกใบหน้า
def train_face_recognizer(faces, labels):
    face_recognizer = cv.face.LBPHFaceRecognizer_create()

    #labels จะเป็น list ของหมายเลขที่เป็นตัวเลข เช่น [123, 123, 123, 124, 124, 125, ...] ซึ่งเป็นหมายเลข user ID
    # แปลง labels ให้เป็น np.array ที่มีชนิดข้อมูลเป็น int32 ซึ่งทำให้สามารถทำการคำนวณและจัดการข้อมูลได้ง่ายขึ้น
    labels = np.array(labels, dtype=np.int32)

    # เรียกใช้ฟังก์ชัน train
    face_recognizer.train(faces, labels)

    # บันทึกโมเดล
    face_recognizer.save('face_data/face_recognizer.yml')
    print("Training completed and model saved!")

# ฟังก์ชันสำหรับตรวจจับใบหน้าและยืนยันตัวตน
def face_login():
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read('face_data/face_recognizer.yml')
    
    cap = cv.VideoCapture(0)
    
    while True:
        ret, img = cap.read()
        if not ret:
            break

        gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_model.detectMultiScale(gray_scale)

        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            
            # ตัดใบหน้า
            face = gray_scale[y:y+h, x:x+w]
            
            # ทำการทำนาย
            label, confidence = face_recognizer.predict(face)
            
            if confidence < 100: #โมเดลมั่นใจว่าใบหน้านี้เป็นของบุคคลที่ฝึกมา
                cv.putText(img, f"User {label} authenticated", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                cv.putText(img, "Unknown Face", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        cv.imshow("Face Login", img)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

# ฟังก์ชันหลัก
def main():
    while True:
        print("1. Collect Faces for Training")
        print("2. Train Face Recognizer")
        print("3. Login with Face Recognition")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            user_id = input("Enter your user ID: ")
            faces, labels = collect_faces(user_id)
            print(f"Collected {len(faces)} faces for user {user_id}")
        
        elif choice == '2':
            if len(faces) > 0:
                train_face_recognizer(faces, labels)
            else:
                print("No faces collected yet. Collect faces first.")
        
        elif choice == '3':
            face_login()
            print("Login successful")
        
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
