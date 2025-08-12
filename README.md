#😴 DriveAlert
Real-Time Driver Drowsiness and Yawn Detection System

DriveAlert is a real-time drowsiness and fatigue detection system designed to monitor a driver's face using a webcam. The system uses computer vision to analyze key facial landmarks for signs of fatigue, such as prolonged eye closure and yawning, and provides an immediate audible warning to prevent potential accidents.

***

## 💡 Features
* **Real-time Drowsiness Detection**: Monitors the user's eyes to detect blinking and prolonged eye closure.
* **Yawning Detection**: Identifies yawning by analyzing the distance between the upper and lower lip.
* **Audible Alerts**: Provides voice feedback via a text-to-speech engine to warn the driver.
* **Performance Monitoring**: Displays real-time Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR) values.

***

## 🛠️ Tech Stack
* **Python**: Main programming language.
* **OpenCV**: For video stream processing.
* **Mediapipe**: For robust facial landmark detection.
* **NumPy**: For efficient numerical computations.
* **pyttsx3**: For text-to-speech alerts.

***

## 🚀 Installation
1.  **Clone the repository:**
    ```bash
    git clone [your-repository-url]
    cd DriveAlert
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

***

## 🏃 Usage
Run the main script from your terminal:
```bash
python main.py

he application will open your webcam. Press q to exit.

👀 Demo
<p align="center">
<img src="demos/DriveAlert_DemoImage_1.png" alt="A screenshot showing the 'DROWSINESS ALERT!'" width="600"/>
</p>
<p align="center">
<i>A screenshot showing the 'DROWSINESS ALERT!' in action.</i>
</p>

<p align="center">
<img src="demos/DriveAlert_DemoImage_2.png" alt="A screenshot showing the 'YAWN ALERT!'" width="600"/>
</p>
<p align="center">
<i>A screenshot showing the 'YAWN ALERT!' in action.</i>
</p>

A short video demonstration of the application:
