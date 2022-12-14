import cv2
import os
import shutil

width = 28
height = 28
dim = (width, height)
i = 0
j = 0
k = 0
index = input('Input the index of file: ')
img_dir = 'E:\\train\\' + index
for f in os.listdir(img_dir):
    img_path = os.path.join(img_dir, f)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    i = i + 1
    if f.split('.')[len(f.split('.')) - 1] != 'jpg' or isinstance(img, type(None)):
        print('False')
        os.remove(img_path)
        j += 1
        continue
    print('Original Dimensions : ', img.shape)
    if img.shape == (28, 28) or img.shape == (28, 28, 3):
        print("True")
        k = k + 1
print('Check on directory: ', img_dir)
print('Total: ', i)
print('Invalid file: ', j)
print('Valid file: ', k)
cv2.waitKey(0)
cv2.destroyAllWindows()
