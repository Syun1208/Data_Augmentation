import cv2
import os
import time

width = 28
height = 28
dim = (width, height)
i = 0
j = 0
k = 0
img_dir0 = 'E:\\mnist\\train\\9'
for f in os.listdir(img_dir0):
    img_path = os.path.join(img_dir0, f)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ', img.shape)
    i = i + 1
    if img_path.split('.')[1] != 'jpg':
        print('False')
        j += 1
        continue
    elif img.shape == (28, 28) or img.shape == (28, 28, 3):
        print("True")
        k = k + 1
print('Check on directory: ', img_dir0)
print('Total: ', i)
print('Invalid file: ', j)
print('Valid file: ', k)
cv2.waitKey(0)
cv2.destroyAllWindows()