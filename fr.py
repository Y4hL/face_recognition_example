# import the libraries
import os
import face_recognition

# make a list of all the available images
images = os.listdir('images')

known_faces = os.listdir('known')

try:
    for i in known_faces:
        print("Analyzing '" + i + "'...")
        try:
            # load your image
            image_to_be_matched = face_recognition.load_image_file('known/' + i)

            # encoded the loaded image into a feature vector
            image_to_be_matched_encoded = face_recognition.face_encodings(
                image_to_be_matched)[0]
        except FileNotFound:
            print(i + " is not a file")
            continue

        # iterate over each image
        for image in images:
            try:
                print("comparing " + i + " to " + image )
                # load the image
                current_image = face_recognition.load_image_file("images/" + image)
                # encode the loaded image into a feature vector
                current_image_encoded = face_recognition.face_encodings(current_image)[0]
                # match your image with the image and check if it matches
                result = face_recognition.compare_faces(
                    [image_to_be_matched_encoded], current_image_encoded)
                # check if it was a match
                if result[0] == True:
                    print("Matched: " + image)
                else:
                    print ("Not matched: " + image)
            except IndexError:
                print("Not matched: " + image)
except MemoryError:
    
    print("You Ran Out of Memory, on low end devices it is not recommended to compare to multiple pictures")
    
