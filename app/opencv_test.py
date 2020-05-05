import cv2
import numpy as np
import torch
from pathlib import Path
from app.scripts.fastai_helper import load_posix_learner

model_path = Path(r'..\local\models\num_workers0.pkl')
learner = load_posix_learner(model_path)

def classify(img):
    global learner
    #img = np.moveaxis(img, -1, 0)
    prediction = learner.predict(img)
    print(prediction)

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

new_frame = True
while rval:
    if new_frame:
        cv2.imshow("preview", frame)
        new_frame = False
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    elif key==ord('s'):
        rval, frame = vc.read()
        new_frame = True
        classify(frame)

vc.release()
cv2.destroyWindow("preview")