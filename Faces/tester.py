import cv2
import numpy as np
import os, subprocess

# Load classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(image_path):
    faces_array = []  # list of file locations to store for cropped facess
    image = cv2.imread(image_path)

    # Convert the image to grayscale and detect
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop through each detected face and crop 
    for i, (x, y, w, h) in enumerate(faces):
        # Crop the face 
        face = image[y:y+h, x:x+w]
        face_filename = f"C:/Users/ccamn/Desktop/Facial recognition/Faces/face_{i+1}.jpg"
        cv2.imwrite(face_filename, face)  # Save face image
        faces_array.append(face_filename)  # Store the path of the cropped face

    return faces_array

def compare_with_template(image, cropped_face_path):
    cropped_face = cv2.imread(cropped_face_path)
    # Convert both images to grayscale 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_cropped_face = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2GRAY)

    # Apply template matching
    result = cv2.matchTemplate(gray_image, gray_cropped_face, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    return max_val, max_loc

# Provide paths
image_path = 'c:/Users/ccamn/Desktop/Facial recognition/Faces/obama4.jpg'
FaceToDetect = 'c:/Users/ccamn/Desktop/Facial recognition/Faces/obama3.jpg'

# Detect faces and get list of file paths for cropped faces

# Load the image to detect faces (FaceToDetect)
image = cv2.imread(FaceToDetect)
for filename in os.listdir('C:/Users/ccamn/Desktop/Facial recognition/Faces/TrainingData'):
    faces = detect_faces(filename) # training faces to compare with of obama 
    # Compare each cropped face with the image to detect
    for idx, cropped_face_path in enumerate(faces):
        match_score, match_location = compare_with_template(image, cropped_face_path)

        print(f"Comparing with face {idx+1} - Match Score: {match_score}")
        print(f"Match Location: {match_location}")

        # If the match score is above a certain threshold, consider it a match
        threshold = 0.7  # You can adjust this threshold based on your needs
        if match_score >= threshold:
            print(f"Face {idx+1} matched successfully!")
            
            # Optionally, draw a rectangle around the matched area
            cropped_face = cv2.imread(cropped_face_path)
            h, w = cropped_face.shape[:2]
            #cv2.rectangle(cropped_face, match_location, (match_location[0] + w, match_location[1] + h), (0, 255, 0), 2)
            #cv2.imshow(f"Matched Face {idx+1}", cropped_face)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
        else:
            print(f"Face {idx+1} did not match.")
