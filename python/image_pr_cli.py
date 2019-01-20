import cv2
import numpy as np
import scipy.misc
import socket as sc
x=cv2.videoCapture(0)
r,photo=x.read()
cv2.waitKey()
cv2.destroyAllWindows()
scipy.misc.imsave("mac.jpg",photo)
f=open(mac.jpg,"rb")
sc.socket()
sc.send(f.read(),('192.168.43.163',3333)