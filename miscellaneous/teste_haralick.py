import cv2
import mahotas

img = cv2.imread("/media/cristiano/SAMSUNG/Kaggle/test/0.jpg")
r,g,b = cv2.split(img)

rad = img.shape[0]/2
r_haralick = mahotas.features.haralick(r,rad)
g_haralick = mahotas.features.haralick(g,rad)
b_haralick = mahotas.features.haralick(b,rad)

l = []
for i in r_haralick.tolist()+g_haralick.tolist()+b_haralick.tolist():
	l = l + i



print l
print len(l)