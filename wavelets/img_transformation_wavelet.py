import numpy as np 
import pywt
import cv2
import matplotlib.pyplot as plt
import pylab

img_path = "/home/cristiano/Documentos/DataScienceBowl/Sample_PNG/0a0c32c9e08cc2ea76a71649de56be6d/-215.910004.png"
# img = cv2.imread('/home/cristiano/Imagens/cris.jpg', cv2.)
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# data = np.ones((4,4), dtype = np.float64)
coeffs = pywt.dwt2(img, 'db1')
cA, (cH,cV,cD) = coeffs

print cH.tolist()

# fig, ax = plt.subplots()
# ax.imshow(cV)
# pylab.imsave('Diagonal.png', cD)
# ax.axis('off')
# plt.show()