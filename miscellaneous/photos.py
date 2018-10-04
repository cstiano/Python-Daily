import os
import sys
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
	path = root.split(os.sep)
	for file in files:
		if file[-4:] == ".nii":
os.system("med2image -i %s/%s -d ./out/%s/%s -o img --outputFileType png --reslice" %(str(root), str(file), path[1], path[2]))