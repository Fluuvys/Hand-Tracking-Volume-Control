# Hand-Tracking-Volume-Control 🎛️🖐️  

A Python-based project to control system volume using real-time hand tracking and gestures. This application combines the power of **OpenCV**, **Mediapipe**, and **PyCaw** to create a seamless and interactive experience for controlling audio settings.

---

## 🚀 Features  

- **Hand Gesture Volume Control**: Adjust the volume by moving your thumb and index finger closer or farther apart.  
- **Visual Indicators**: Real-time circles, lines, and a dynamic volume bar provide intuitive visual feedback.  
- **Advanced Gesture Handling**: Use the pinky gesture for precise volume locking and control.  
- **Smooth Volume Adjustment**: Utilizes interpolation for responsive and fluid controls.

---

## 🛠️ Technologies Used  

- **[Python](https://www.python.org/)**  
- **[OpenCV](https://opencv.org/)**: For real-time image processing.  
- **[Mediapipe](https://google.github.io/mediapipe/solutions/hands.html)**: To detect and track hand landmarks.  
- **[PyCaw](https://github.com/AndreMiras/pycaw)**: To interface with system audio controls.  
- **Numpy**: For efficient numerical operations.  

---

## 🔧 How It Works  

1. **Hand Detection**: Mediapipe processes the webcam feed and identifies hand landmarks in real-time.  
2. **Distance Measurement**: Calculates the distance between the thumb (landmark 4) and index finger (landmark 8).  
3. **Volume Mapping**: The distance is interpolated to match the system's volume range (-65 dB to 0 dB).  
4. **Gesture Controls**:  
   - Adjust volume dynamically by varying the distance between fingers.  
   - Use the pinky gesture to lock and set precise volume levels.

---

## 🖥️ Setup and Installation  

### Prerequisites  

- Python 3.7 up to 3.12  
- A webcam  

### Installation  

1. Clone this repository:  
   ```bash
   git clone [https://github.com/Fluuvys/Hand-Tracking-Volume-Control.git]
   cd Hand-Tracking-Volume-Control
