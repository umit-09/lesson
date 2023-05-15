import cv2
from pyzbar import pyzbar
import qrcode
from PIL import Image
import os

def generateQRCode(inputData):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=1)
    qr.add_data(inputData)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    qr_img_path = os.path.join(desktop_path, f"qrcode_{data}.png")
    img.save(qr_img_path)

# Create a VideoCapture object to access the default camera
cap = cv2.VideoCapture(0)

# Set the path to the desktop folder
desktop_path = os.path.expanduser("~/Desktop")

# Loop through frames in the video stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find QR codes in the frame
    qrcodes = pyzbar.decode(gray)

    if qrcodes != []:
        print(qrcodes)
        for qrcode in qrcodes:
            # Extract the data from the QR code
            data = qrcode.data.decode("utf-8")
            text = str(data)
            print("QR Code detected: ", text)
            generateQRCode(text)
            print("QR Code image saved to desktop.")

        # Display the video stream
    cv2.imshow('frame', frame)

        # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the windows
cap.release()
cv2.destroyAllWindows()
