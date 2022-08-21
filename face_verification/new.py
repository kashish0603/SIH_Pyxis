<<<<<<< HEAD
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from torchvision import datasets
from torch.utils.data import DataLoader
from PIL import Image
import os
=======
>>>>>>> 2d5ade31f65880a6688555c4dc01b04853f1d186
def facerecog():
    # import libraries
    import cv2
    import face_recognition
    import numpy as np

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

<<<<<<< HEAD
            result = face_match(img_path,'pytorch_face_recognition//data2.pt')
=======
            result = face_match(img_path,'FaceRec2//pytorch_face_recognition//data2.pt')
>>>>>>> 2d5ade31f65880a6688555c4dc01b04853f1d186

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

def face_match(img_path, data_path): # img_path= location of photo, data_path= location of data.pt 
<<<<<<< HEAD

=======
    from facenet_pytorch import MTCNN, InceptionResnetV1
    import torch
    from torchvision import datasets
    from torch.utils.data import DataLoader
    from PIL import Image
    import os
>>>>>>> 2d5ade31f65880a6688555c4dc01b04853f1d186

    mtcnn = MTCNN(image_size=240, margin=0, min_face_size=20)
    resnet = InceptionResnetV1(pretrained='vggface2').eval()
    
    # getting embedding matrix of the given img
    img = Image.open(img_path)
    face, prob = mtcnn(img, return_prob=True) # returns cropped face and probability
    emb = resnet(face.unsqueeze(0)).detach() # detech is to make required gradient false
    
    saved_data = torch.load(data_path) # loading data.pt file
    embedding_list = saved_data[0] # getting embedding data
    name_list = saved_data[1] # getting list of names
    dist_list = [] # list of matched distances, minimum distance is used to identify the person
    
    for idx, emb_db in enumerate(embedding_list):
        dist = torch.dist(emb, emb_db).item()
        dist_list.append(dist)
        
    idx_min = dist_list.index(min(dist_list))
    # return (name_list[idx_min], min(dist_list))
    result = (name_list[-1], dist_list[-5])

    os.remove(img_path)

    return result
<<<<<<< HEAD
=======

if __name__ == '__main__':
    facerecog()
>>>>>>> 2d5ade31f65880a6688555c4dc01b04853f1d186
