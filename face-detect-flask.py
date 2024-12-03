from flask import Flask, render_template, request, jsonify
import cv2 as cv
import numpy as np

app = Flask(__name__)

# โหลดโมเดลตรวจจับใบหน้า
face_model = cv.CascadeClassifier('face-detect-model.xml')

# ตัวแปร global สำหรับเก็บข้อมูล
faces = []
labels = []

# ฟังก์ชันเก็บข้อมูลใบหน้าของผู้ใช้
def collect_faces(user_id):
    global faces, labels  # ใช้ตัวแปร global
    cap = cv.VideoCapture(0)
    count = 0
    try:
        user_id = np.int32(user_id)
    except ValueError:
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
        
        if count >= 30:
            break
    
    cap.release()
    cv.destroyAllWindows()

    return faces, labels

# ฟังก์ชันฝึกสอนโมเดลการจำแนกใบหน้า
def train_face_recognizer():
    global faces, labels  # ใช้ตัวแปร global
    if len(faces) == 0 or len(labels) == 0:
        return "No faces or labels to train with.", 400

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    labels = np.array(labels, dtype=np.int32)
    face_recognizer.train(faces, labels)
    face_recognizer.save('face_data/face_recognizer.yml')
    return "Training completed and model saved!", 200

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
            face = gray_scale[y:y+h, x:x+w]
            label, confidence = face_recognizer.predict(face)
            
            if confidence < 100:
                cv.putText(img, f"User {label} authenticated", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                cv.putText(img, "Unknown Face", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        cv.imshow("Face Login", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

@app.route('/')
def index():
    return render_template('index.html')  # ส่งไฟล์ index.html

@app.route('/collect_faces', methods=['POST'])
def collect_faces_api():
    user_id = request.json.get('user_id')
    faces, labels = collect_faces(user_id)
    if faces:
        return jsonify({"message": f"Collected {len(faces)} faces for user {user_id}"}), 200
    else:
        return jsonify({"error": "Failed to collect faces"}), 500

@app.route('/train', methods=['POST'])
def train_api():
    message, status_code = train_face_recognizer()  # เรียกใช้ฟังก์ชันฝึกสอนโมเดล
    return jsonify({"message": message}), status_code  # ส่งข้อความตอบกลับ

@app.route('/login', methods=['POST'])
def login_api():
    face_login()
    return jsonify({"message": "Login complete"}), 200

if __name__ == '__main__':
    app.run(debug=True)
