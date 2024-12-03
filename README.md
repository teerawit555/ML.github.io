<a name="readme-top"></a>

<br />
<div align="center">
    <h1>Face Recognition System</h1>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

โปรแกรม **Face Recognition System** ใช้เทคโนโลยีการรู้จำใบหน้า (Face Recognition) เพื่อตรวจจับและยืนยันตัวตนของผู้ใช้ โดยสามารถเก็บข้อมูลใบหน้าของผู้ใช้แต่ละคนแล้วฝึกโมเดลเพื่อจำแนกใบหน้าในภายหลังได้ ระบบประกอบด้วย 3 ฟังก์ชันหลัก:

1. **Collect Faces** - เก็บข้อมูลใบหน้าของผู้ใช้จากกล้องเว็บแคม
2. **Train Model** - ฝึกโมเดลการรู้จำใบหน้าจากข้อมูลที่เก็บ
3. **Face Login** - ใช้โมเดลที่ฝึกแล้วเพื่อยืนยันตัวตนผู้ใช้

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation

เพื่อติดตั้งโปรแกรม **Face Recognition System** ทำตามขั้นตอนดังนี้:

1. ติดตั้ง Python [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. ติดตั้ง OpenCV สำหรับ Python
   ```sh
   pip install opencv-python opencv-contrib-python
   
3. ติดตั้ง Flask สำหรับการพัฒนาเว็บแอป
   ```sh
   pip install flask
4. Clone repository
   ```sh
   git clone https://github.com/teerawit555/FaceRecognition.git

## การรันโปรแกรม
1. เปิด terminal และเข้าไปที่โฟลเดอร์โปรเจกต์
2. รันคำสั่งเพื่อเริ่มโปรแกรม Flask
   ```sh
   python face-detect-flask.py
3. โปรแกรมจะรันในโหมด development และคุณสามารถเข้าไปที่ http://127.0.0.1:5000 ในเบราว์เซอร์เพื่อใช้งานระบบ
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## วิธีการใช้งาน
1. Collect Faces การเก็บข้อมูลใบหน้า:
 - กดปุ่ม "Collect Faces"
 - ระบบจะใช้กล้องเว็บแคมเพื่อเก็บข้อมูลใบหน้าของคุณ
 - กรอก user_id (หมายเลขผู้ใช้) และกด "เริ่มเก็บข้อมูล"
 - ระบบจะเก็บใบหน้าของคุณอย่างน้อย 30 ภาพ

2. Train Model การฝึกโมเดล:
 - กดปุ่ม "Train Model"
 - ระบบจะฝึกโมเดลการจำแนกใบหน้าจากข้อมูลที่เก็บไว้และบันทึกโมเดลในไฟล์ face_data/face_recognizer.yml

3. Face Login การยืนยันตัวตน:
 - กดปุ่ม "Login"
 - ระบบจะใช้กล้องเว็บแคมเพื่อถ่ายภาพใบหน้าแล้วเปรียบเทียบกับข้อมูลที่ฝึกไว้
 - หากตรงกับใบหน้าที่มีในฐานข้อมูล จะแสดงข้อความ "User {label} authenticated"
 - หากไม่ตรง จะแสดงข้อความ "Unknown Face"
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## วิธีการทำงานของโปรแกรม

1. Collect Faces:
 - ระบบจะเปิดกล้องเว็บแคมและเริ่มเก็บภาพใบหน้าของผู้ใช้
 - ระบบจะตรวจจับใบหน้าในภาพและบันทึกข้อมูลใบหน้าพร้อมกับ user_id
2. Train Model:
 - โมเดลการรู้จำใบหน้าจะถูกฝึกจากข้อมูลที่เก็บไว้
 - เมื่อฝึกเสร็จ โมเดลจะถูกบันทึกลงในไฟล์ face_data/face_recognizer.yml เพื่อใช้งานในอนาคต
3. Face Login:
 - ระบบจะเปิดกล้องเว็บแคมอีกครั้งเพื่อถ่ายภาพใบหน้าผู้ใช้
 - หากมีการจับคู่ใบหน้าในฐานข้อมูล ระบบจะแสดงข้อความยืนยันตัวตน
 - หากไม่ตรง ระบบจะแสดงข้อความว่า "Unknown Face"
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- FRONTEND -->

## ขั้นตอนการทำงานของโปรแกรม
1. เริ่มต้นโปรแกรมและรอการเปิดกล้องเว็บแคม
2 .เก็บภาพใบหน้าของผู้ใช้โดยใช้กล้อง
3. ฝึกโมเดลด้วยข้อมูลใบหน้า
4. ใช้โมเดลที่ฝึกแล้วเพื่อตรวจสอบและยืนยันตัวตนของผู้ใช้
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- FRONTEND -->

## เมื่อกดใช้งานโปรแกรม
1. เปิดกล้องเว็บแคมเพื่อเก็บข้อมูลใบหน้า
2. กรอก user_id และเริ่มเก็บข้อมูล
3. ฝึกโมเดลหลังจากเก็บข้อมูล
4. ใช้กล้องตรวจสอบใบหน้าผู้ใช้และยืนยันตัวตน
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- FRONTEND -->


