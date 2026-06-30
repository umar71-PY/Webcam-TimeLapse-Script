# AutoCapture: Hardware Automation & Time-Lapse Tool 📸

A robust, cross-platform Python automation script that securely interfaces with the system's primary webcam to capture time-lapse images at regular intervals. 

## ⚙️ How It Works (Technical Workflow)

This script is divided into four main functional blocks:

1. **Cross-Platform Directory Management:** 
   Uses `os.path.expanduser("~")` to dynamically locate the current user's home directory. It automatically creates an `AutoCaptures` folder inside the `Documents` directory, ensuring compatibility across Windows, macOS, and Linux without hardcoding paths.
2. **Hardware Interfacing & Locking:** 
   Utilizes OpenCV (`cv2.VideoCapture(0)`) to request and lock the primary webcam hardware. It includes validation checks to gracefully exit if the camera is unavailable or lacks permission.
3. **Chronological File Generation:** 
   Runs an infinite loop that captures a frame every 10 seconds. Each image is saved with a unique, down-to-the-second timestamp using the `datetime` module (e.g., `pic_2026-06-30_21-45-12.jpg`) to prevent data overwriting.
4. **Graceful Shutdown & Security:** 
   Wrapped entirely in a `try-except-finally` block. Upon detecting a `KeyboardInterrupt` (Ctrl+C), the script forcefully executes `cap.release()`. This ensures the camera hardware lock is released and the webcam indicator LED is turned off, preventing background resource leaks or privacy breaches.

## 🛠️ Prerequisites

Before running the script, ensure you have Python 3.x installed along with the OpenCV library.

You can install the required library using pip:
```bash
pip install opencv-python



Disclaimer
For Educational Purposes Only: This project was created to demonstrate operating system path handling, Python automation, and hardware-level security implications. It should only be executed on authorized personal devices
