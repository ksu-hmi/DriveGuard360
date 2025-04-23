## DriveGuard360: Driver Monitoring System

**DriveGuard360** is a beginner friendly python-based driver monitoring system designed to enhance road safety by detecting **drowsiness**, potential **stroke symptoms**, and signs of **driver unresponsiveness** in real-time. It includes stimulated detection logic, real-time face/eye detection (using OpenCV), and an alert logging system.

## Features:

- ✅ Menu-driven interface in terminal
- ✅ Drowsiness simulation (based on blink pattern)
- ✅ Stroke symptom simulation (based on facial cues)
- ✅ Real-time Face & Eye Detection (OpenCV)
- ✅ Alerts and logs saved to file
- ✅ Beginner-friendly modular Python code

## Purpose: 

- Early detection of medical emergencies: stroke, seizures, diabetic comas

- Security net for long haul truck drivers or overworked first responders

## Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

Or install OpenCV manually:

```bash
pip install opencv-python
```

---

##  How to Run

Clone or download this repo, then run:

```bash
python main.py
```

Follow the terminal prompts to test each feature.


##  Face & Eye Detection (Optional Feature that I'm still working through)

To test real-time webcam detection:

1. Ensure a webcam is available.
2. Download Haar Cascades and place in a `models/` folder:
   - [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
   - [haarcascade_eye.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)

3. Run the detection module:

```bash
python face_eye_detection.py
```

> Press `q` to close the webcam window.

---

##  File Structure

```
DriveGuard360/
│
├── main.py                  # Runs the app menu
├── alerts.py                # Alert handler
├── logs.py                  # Logging function
├── drowsiness_check.py      # Simulates drowsiness detection
├── stroke_check.py          # Simulates stroke detection
├── face_eye_detection.py    # OpenCV-based eye/face detection
├── requirements.txt         # Python packages list
├── README.md                # Current document
└── log.txt                  # Alert history 
```

##  Developed by

**Purity Varist, BSN, RN**

---

## Disclaimer:

This project is for educational purposes only. Do not use as a vehicle safety mechanism or medical safety device.


## Future Improvements:

I would like to incorporate smart device integration for vital sign monitoring and real time ECG integration. Once an emergency is detected or activated this data could be shared with first responders within a radius via cloud network as well. 



