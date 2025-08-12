#😴 DriveAlert
Real-Time Driver Drowsiness and Yawn Detection System


DriveAlert is a real-time drowsiness and fatigue detection system designed to monitor a driver's face using a webcam. The system uses computer vision to analyze key facial landmarks for signs of fatigue, such as prolonged eye closure and yawning, and provides an immediate audible warning to prevent potential accidents.

## 💡 Features
* **Real-time Drowsiness Detection**: Monitors the user's eyes to detect blinking and prolonged eye closure.
* **Yawning Detection**: Identifies yawning by analyzing the distance between the upper and lower lip.
* **Audible Alerts**: Provides voice feedback with the help of a text-to-speech engine to warn the driver.
* **Performance Monitoring**: Displays real-time Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR) values for debugging.

## 🛠️ Tech Stack
* **Python**: The main programming language for the application logic.
* **OpenCV (`cv2`)**: For capturing and processing the video stream from the webcam.
* **Mediapipe**: For robust and accurate facial landmark detection.
* **NumPy**: For efficient numerical computations and vector operations.
* **pyttsx3**: For generating text-to-speech alerts.

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/saichethana28/DriveAlert.git](https://github.com/saichethana28/DriveAlert.git)
    cd DriveAlert
    ```

2.  **Create a `requirements.txt` file:**
    In your terminal, navigate to the project directory and run the following command to generate a list of dependencies:
    ```bash
    pip freeze > requirements.txt
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃 Usage
Run the main script from your terminal:
```bash
python main.py
