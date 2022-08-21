def facerecog():
    # import libraries
    import cv2
    import face_recognition
    import numpy as np
    import recog

    # Get a reference to webcam 
    video_capture = cv2.VideoCapture(0)

    # Initialize variables
    face_locations = []
    writer = None
    count = 0

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)

        # Display the results
        for top, right, bottom, left in face_locations:
            # Draw a box around the face
            cv2.rectangle(frame, (left-5, top-60), (right+5, bottom+5), (0, 0, 255), 2)

        count+=1

        if face_locations!=[] and count%10==0:
            img_path = 'images/frame'+str(count+1)+".jpg"
            cv2.imwrite(img_path,frame)

            result = recog.face_match(img_path,'data2.pt')

            if result[1]>1.0:
                print("No match")
            else:
                print('Face matched with: ',result[0], 'With distance: ',result[1])
                
        
        cv2.imshow("Footage",frame)
        
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
        # Display the resulting image
        # if writer is None:
        #     fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        #     writer = cv2.VideoWriter('processed.avi', fourcc, 30, (frame.shape[1], frame.shape[0]), True)
        
        print(count)

    # writer.release()
    video_capture.release()

if __name__ == '__main__':
    facerecog()