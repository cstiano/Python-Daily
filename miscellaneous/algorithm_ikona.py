import numpy as np 
import os
import pywt 
import cv2
import mahotas
import matplotlib.pyplot as plt

folder_path = "/home/cristiano/Documentos/DataScienceBowl/Sample_PNG/0a0c32c9e08cc2ea76a71649de56be6d/"
img_list = os.listdir(folder_path)
img_list.sort()
init = (len(img_list)/2) - (len(img_list)/8)
end = (len(img_list)/2) + (len(img_list)/8)
count = 1

for elem in img_list[init:end]:
	img = cv2.imread(folder_path+elem)
	img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	coeffs = pywt.dwt2(img, 'db8')
	cA, (cH,cV,cD) = coeffs
	apro_zer = mahotas.features.zernike_moments(cA,128)
	hor_zer = mahotas.features.zernike_moments(cH,128)
	ver_zer = mahotas.features.zernike_moments(cV,128)
	dia_zer = mahotas.features.zernike_moments(cD,128)
	print ("vector %d \n" % count)

	vec_res = (apro_zer.tolist())+(hor_zer.tolist())+(ver_zer.tolist())+(dia_zer.tolist())
	# print cH
	# print cV
	suma = np.sum([cV,cH,cD], axis=0)
	# print suma
	# fig, ax = plt.subplots()
	up_mat = np.concatenate((cA, cH), axis = 1)
	down_mat = np.concatenate((cV, cD), axis = 1)
	sum_mat = np.concatenate((up_mat, down_mat), axis = 0)

	sum_zer = mahotas.features.zernike_moments(sum_mat,362.04)
	# print sum_zer.tolist()
	# plt.imshow(sum_mat)
	# plt.show()
	print apro_zer.tolist()
	print hor_zer.tolist()
	print ver_zer.tolist()
	print dia_zer.tolist()
	if(count>5):
		break
	count+=1
	print len(img.tolist()), len(cH.tolist())

# print (os.listdir(folder_path))