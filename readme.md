# **PROJECT: SMART ATTENDANCE AI**

## **Project Members:**
1. Hero Bhai
2. DON
3. Uncle John

---

## **Problem Statement:**
Traditional attendance systems are prone to fraud, such as students proxying attendance through friends or false ID punching. Our project eliminates these issues by leveraging facial recognition technology.

---

## **Project Overview:**
SMART Attendance AI is a facial recognition-based system that accurately detects and verifies students' attendance in real-time. Built using Python, OpenCV, and a K-Nearest Neighbors (KNN) classifier, this system ensures efficient and secure attendance management.

### **Key Features:**
- Real-time face detection and recognition.
- Prevents proxy attendance through ID cards or manual logs.
- User-friendly and lightweight application.

---

## **Directory Structure:**
- **readme.md**: Project overview and documentation.
- **AddFace.py**: Script to register new faces in the database.
- **test.py**: Script for testing the face recognition system.
- **data/**: Contains essential project files:
  - `haarcascade_frontalface_default.xml`: Pre-trained face detection model.
  - `faces_data.pkl`: Encoded face data.
  - `names.pkl`: Registered user names.
- **Attendance/**: Stores attendance logs in `.csv` format.
- **poetry.lock / pyproject.toml / .venv**: Dependency and environment management files.

---

## **How It Works:**

1. **Face Detection:**
   - Utilizes the `haarcascade_frontalface_default.xml` model, a pre-trained Haar cascade classifier, for real-time face detection.
   - This classifier identifies facial features using Haar-like features.

2. **Face Recognition:**
   - Employs a KNN classifier trained on registered faces.
   - Matches detected faces against the database and logs attendance.

3. **Attendance Logs:**
   - Stores attendance data in `.csv` files for easy access and analysis.

---

## **FAQs:**

### **1. What is Haar Cascade Classifier?**
The Haar cascade classifier, used in this project, is a machine learning-based object detection method. It identifies facial features by applying pre-trained Haar-like features.

### **2. How do I register a new user?**
Run `AddFace.py` and follow the prompts to capture and register a new user's face.

### **3. How do I take attendance/recognize face?**
Run `test.py` and press ‘o’ to take attendance or ‘q’ to quit the app.

### **4. Where can I find attendance records?**
Attendance logs are stored in the `Attendance/` folder as `.csv` files, named by the date.

### **5. How is this project licensed?**
We use a Creative Commons License for the Haar Cascade model (`haarcascade_frontalface_default.xml`), originally developed by Rainer Lienhart.

---

## **Acknowledgments:**
A special thanks to [Chando](https://github.com/Chando0185/) for their support through providing the basic idea for creating such facial recognition-based apps. Their contribution has greatly helped in building the foundation for this project.

---

For more details, refer to the **code files** and explore the directory!

