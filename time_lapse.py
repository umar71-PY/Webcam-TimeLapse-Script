import cv2
import os
import time
from datetime import datetime

home_dir = os.path.expanduser("~")
folder_name = "AutoCaptures"
save_path = os.path.join(home_dir, "Documents", folder_name)

if not os.path.exists(save_path):
    os.makedirs(save_path)
    print(f"[+] Created new directory: {save_path}")
else:
    print(f"[*] Directory already exists: {save_path}")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("[-] Error: Unable to access the camera. Please check connections and permissions.")
    exit()

print("\n[>>] Camera initialized successfully. Capturing an image every 10 seconds.")
print("[!] Press 'Ctrl + C' in the terminal to terminate the script safely.\n")

try:
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("[-] Error: Failed to capture frame from the camera.")
            break

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"pic_{timestamp}.jpg"
        full_file_path = os.path.join(save_path, file_name)

        cv2.imwrite(full_file_path, frame)
        print(f"[+] Image successfully captured and saved: {file_name}")

        time.sleep(10)

except KeyboardInterrupt:
    print("\n[!] KeyboardInterrupt detected. Initiating safe shutdown sequence...")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("[*] Camera hardware released safely. Process terminated.")
