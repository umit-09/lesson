import cv2
from pyzbar import pyzbar
import qrcode
import os
import string

def generateQRCode(inputData, save_path):
    import qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=1
    )
    qr.add_data(inputData)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Remove unsupported characters from the file name
    valid_chars = string.ascii_letters + string.digits + ' _-'
    sanitized_input = ''.join(c for c in inputData if c in valid_chars)
    
    # Create the scans folder if it doesn't exist
    scans_folder = os.path.join(save_path, 'scans')
    os.makedirs(scans_folder, exist_ok=True)
    
    qr_img_path = os.path.join(scans_folder, f"qrcode_{sanitized_input}.png")
    img.save(qr_img_path)
    return qr_img_path

# Create a VideoCapture object to access the default camera
cap = cv2.VideoCapture(0)

# Set the path to the desktop folder
save_path = os.path.dirname(os.path.abspath(__file__))

# Keep track of scanned QR codes
scanned_qrcodes = set()

# Loop through frames in the video stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find QR codes in the frame
    qrcodes = pyzbar.decode(gray)

    if qrcodes:
        print(qrcodes)
        for qrcode in qrcodes:
            # Extract the data from the QR code
            data = qrcode.data.decode("utf-8")
            print("QR Code detected:", data)
            if data not in scanned_qrcodes:
                qr_img_path = generateQRCode(data, save_path)
                scanned_qrcodes.add(data)
                print("QR Code image saved to desktop:", qr_img_path)
            else:
                print("QR Code already scanned. Skipping saving.")

    # Display the video stream
    cv2.imshow('frame', frame)

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the windows
cap.release()
cv2.destroyAllWindows()
