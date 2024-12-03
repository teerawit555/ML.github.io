// ฟังก์ชันสำหรับการเก็บข้อมูลใบหน้า
function collectFaces() {
    const userId = document.getElementById('user_id').value;  // ดึงค่าจากฟอร์มกรอก user_id

    // ตรวจสอบว่า user_id ถูกกรอกหรือยัง
    if (!userId) {
        alert("Please enter a user ID.");
        return;
    }

    fetch('/collect_faces', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_id: userId,  // ส่ง user_id ไป
        })
    })
    .then(response => response.json())
    .then(data => {
        // แสดงข้อความที่ได้รับจาก Flask API
        const statusElement = document.getElementById('status-message');
        statusElement.innerHTML = data.message;  // ข้อความที่ Flask ตอบกลับ
        statusElement.style.color = 'green'; // สีข้อความ

        // ล้างข้อความหลังจาก 5 วินาที
        setTimeout(() => {
            statusElement.innerHTML = ''; 
        }, 5000);
    })
    .catch(error => {
        console.error('Error:', error);
        const statusElement = document.getElementById('status-message');
        statusElement.innerHTML = "Error during face collection. Please try again.";
        statusElement.style.color = 'red'; // สีข้อความสำหรับข้อผิดพลาด
    });
}

// ฟังก์ชันสำหรับการฝึกโมเดล
function trainModel() {
    fetch('/train', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        console.log(data);  // ดูข้อมูลที่ได้จาก Flask ใน console

        const statusElement = document.getElementById('status-message');
        
        if (data.error) {
            statusElement.innerHTML = data.error;
            statusElement.style.color = 'red';
        } else if (data.message) {
            statusElement.innerHTML = data.message;
            statusElement.style.color = 'green';
        } else {
            statusElement.innerHTML = "Unknown response format.";
            statusElement.style.color = 'red';
        }

        setTimeout(() => {
            statusElement.innerHTML = '';
        }, 5000);
    })
    .catch(error => {
        console.error('Error:', error);
        const statusElement = document.getElementById('status-message');
        statusElement.innerHTML = "Error during training. Please try again.";
        statusElement.style.color = 'red';
    });
}

// ฟังก์ชันสำหรับการเข้าสู่ระบบด้วยใบหน้า
function loginFace() {
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        // แสดงข้อความที่ได้รับจาก Flask API
        const statusElement = document.getElementById('status-message');
        statusElement.innerHTML = data.message;  // ข้อความที่ Flask ตอบกลับ
        statusElement.style.color = 'green'; // สีข้อความ

        // ล้างข้อความหลังจาก 5 วินาที
        setTimeout(() => {
            statusElement.innerHTML = ''; 
        }, 5000);
    })
    .catch(error => {
        console.error('Error:', error);
        const statusElement = document.getElementById('status-message');
        statusElement.innerHTML = "Error during login. Please try again.";
        statusElement.style.color = 'red'; // สีข้อความสำหรับข้อผิดพลาด
    });
}
