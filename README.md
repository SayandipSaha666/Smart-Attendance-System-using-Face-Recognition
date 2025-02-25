# Smart Attendance System Using Face Recognition

## Overview
The **Smart Attendance System** is an automated system that uses **Face Recognition** to mark attendance efficiently. This system employs the **OpenCV** library for face detection using a webcam, and it generates encodings of given images to extract facial features. The attendance data is stored in **Firebase**, enabling real-time updates and enforcing daily attendance limits.

## Features
- **Face Detection:** Utilizes OpenCV to detect faces using a webcam.
- **Encoding Generator:** Extracts features from images and creates face encodings.
- **Real-Time Database:** Firebase is used to store and update attendance records instantly.
- **Daily Attendance Restriction:** Limits attendance to once per day per individual.
- **Automated Tracking:** Eliminates manual attendance marking and reduces errors.

## Technologies Used
- **Python**
- **OpenCV** (for face detection and recognition)
- **dlib** (for facial feature extraction)
- **NumPy & Pandas** (for data handling)
- **Firebase Realtime Database** (for storing attendance records)
- **Pyrebase** (for integrating Firebase with Python)

## Installation & Setup
### Prerequisites
Ensure you have Python installed. You can download it from [Python's official website](https://www.python.org/downloads/).

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/smart-attendance-system.git
cd smart-attendance-system
```

### Step 2: Install Required Libraries
Install the dependencies using pip:
```bash
pip install opencv-python numpy dlib pandas pyrebase4
```

### Step 3: Configure Firebase
1. Create a Firebase project on [Firebase Console](https://console.firebase.google.com/).
2. Enable **Realtime Database**.
3. Generate a `config.json` file with Firebase credentials and place it in the project directory.

### Step 4: Run the System
Execute the main script to start the attendance system:
```bash
python main.py
```

## Working Mechanism
1. **Face Detection:** The system captures a live video feed from the webcam and detects faces using OpenCV.
2. **Feature Extraction:** It processes images and creates unique encodings for each individual.
3. **Attendance Logging:** When a recognized face is detected, the attendance is marked and stored in Firebase.
4. **Database Update:** The database updates in real-time, preventing duplicate entries beyond the daily limit.

## Project Structure
```
smart-attendance-system/
│── dataset/                 # Stores images for training
│── encodings/               # Stores encoded face data
│── firebase/                # Firebase configuration files
│── main.py                  # Main script for running the attendance system
│── requirements.txt          # Required dependencies
│── README.md                 # Project Documentation
```

## Future Enhancements
- Integrate with RFID or QR-based authentication for additional security.
- Implement mobile notifications for real-time attendance updates.
- Deploy as a cloud-based web application for remote access.

## Contributors
- **Sayandip Saha** (sahasbhs2022@gmail.com)
- **Murtaza Hassan** (https://github.com/murtazahassan)

## License
This project is licensed under the **MIT License**. Feel free to modify and use it as needed.

---

For any issues or suggestions, please open an issue in the [GitHub Repository](https://github.com/SayandipSaha666/Smart-Attendance-System-using-Face-A).

