
from linkedin_api import Linkedin
import requests
from deepface import DeepFace
import cv2
import mediapipe as mp
import numpy as np
from transformers import pipeline
from transformers import ViTFeatureExtractor, ViTForImageClassification
import furl
api = Linkedin("ansu@trymph.com","asterbyte")
f=furl.furl("https://www.linkedin.com/in/insha-lamia-0b4111233/")
len=(str(f.path).split("/"))
username=(len[2])
data=(api.get_profile(username))
firstname=data['firstName']
lastname=data['lastName']
name=str(firstname+' '+lastname)
f1=data['displayPictureUrl']
f2=data['img_800_800']
img_url=str(f1+f2)
response = requests.get(img_url)
if response.status_code:
    fp = open(name, 'wb')
    fp.write(response.content)
    fp.close()
model = ViTForImageClassification.from_pretrained('nateraw/vit-age-classifier')
transforms = ViTFeatureExtractor.from_pretrained('nateraw/vit-age-classifier')
classifier = pipeline("image-classification", model="nateraw/vit-age-classifier")
# img= "/home/shalu/PycharmProjects/deep/insha.jpeg"
s= classifier(name)
#print(s[0])
age= s[0]['label']
# print("Age is",age)
print(s[0]['label'])

obj = DeepFace.analyze(img_path = name,
        actions = ['emotion'])

# print(obj)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

image = cv2.imread(name)
# convert to hsv
lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
    # To improve performance
image.flags.writeable = False
    # Get the result
results = face_mesh.process(image)
    # To improve performance
image.flags.writeable = True
    # Convert the color space from RGB to BGR
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
img_h, img_w, img_c = image.shape
face_3d = []
face_2d = []
if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        for idx, lm in enumerate(face_landmarks.landmark):
            if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                if idx == 1:
                    nose_2d = (lm.x * img_w, lm.y * img_h)
                    nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 8000)
                x, y = int(lm.x * img_w), int(lm.y * img_h)
                    # Get the 2D Coordinates
                face_2d.append([x, y])
                    # Get the 3D Coordinates
                face_3d.append([x, y, lm.z])
                    # Convert it to the NumPy array
        face_2d = np.array(face_2d, dtype=np.float64)
            # Convert it to the NumPy array
        face_3d = np.array(face_3d, dtype=np.float64)
            # The camera matrix
        focal_length = 1 * img_w
        cam_matrix = np.array([[focal_length, 0, img_h / 2],
                                   [0, focal_length, img_w / 2],
                                   [0, 0, 1]])
            # The Distance Matrix
        dist_matrix = np.zeros((4, 1), dtype=np.float64)
            # Solve PnP
        success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)
            # Get rotational matrix
        rmat, jac = cv2.Rodrigues(rot_vec)
            # Get angles
        angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)
            # Get the y rotation degree
        x = angles[0] * 360
        y = angles[1] * 360
            # print(y)
            # See where the user's head tilting
        if y < -10:
            text = "Looking Left"
            print("Not proper profile look. For better linkedin profile, Body must be straight forward")
        elif y > 10:
            text = "Looking Right"
        elif x < -10:
            text = "Looking Down"
        else:
            text = "Forward"
        cv2.putText(image, text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # print("Body posture:",text)
        print(obj['dominant_emotion'], "\n","Body posture:", text)


