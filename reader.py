import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.compat.v1 import ConfigProto, InteractiveSession

config=ConfigProto()
config.gpu_options.allow_growth=True
session=InteractiveSession(config=config)

m=load_model("detect.h5")
cap=cv2.VideoCapture(2)
while True:
    ret, frame=cap.read()
    f=cv2.resize(frame,(96,96))
    f=cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    f=cv2.cvtColor(f, cv2.COLOR_GRAY2BGR)
    f=np.reshape(f,(1,96,96,3))
    f=preprocess_input(f)
    print(np.argmax(m.predict(f)))
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()