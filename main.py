import os
import cv2

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in an image
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Directory containing the images
directory = './images/'  # Replace with the actual path to the directory

# Create the output directory if it doesn't exist
output_directory = './faces/'  # Replace with the actual path to the output directory
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each image in the directory
for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(directory, filename)
        image = cv2.imread(image_path)

        # Detect faces in the current image
        detected_faces = detect_faces(image)

        # Draw green bounding boxes on the detected faces
        for i, (x, y, w, h) in enumerate(detected_faces):
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Save the image with green bounding boxes
        result_filename = f"result_{filename}"
        result_path = os.path.join(output_directory, result_filename)
        cv2.imwrite(result_path, image)
