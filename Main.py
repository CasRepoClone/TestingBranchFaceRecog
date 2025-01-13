import cv2
import face_recognition
import numpy as np

# Load an image of the known faces
known_face_encodings = []
known_face_names = []

# Load a sample image for each person
# Add a known face (for example, a picture of yourself or a friend)
image_of_person_1 = face_recognition.load_image_file("person_1.jpg")
encoding_of_person_1 = face_recognition.face_encodings(image_of_person_1)[0]
known_face_encodings.append(encoding_of_person_1)
known_face_names.append("Person 1")

# You can add more people like this (repeat for other images of other people)
image_of_person_2 = face_recognition.load_image_file("person_2.jpg")
encoding_of_person_2 = face_recognition.face_encodings(image_of_person_2)[0]
known_face_encodings.append(encoding_of_person_2)
known_face_names.append("Person 2")

# Start capturing video
video_capture = cv2.VideoCapture(0)  # Use 0 for the default webcam

while True:
    # Capture each frame from the webcam
    ret, frame = video_capture.read()

    # Convert the image from BGR to RGB (Face recognition uses RGB)
    rgb_frame = frame[:, :, ::-1]

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"  # Default if no match is found

        # If there's a match, use the known name
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle around the face and add a label
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit the loop when the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
video_capture.release()
cv2.destroyAllWindows()
