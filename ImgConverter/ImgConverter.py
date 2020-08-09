import cv2
import os

while True:
    image = input('Input image name your want to convert, eg：1.jpg. Your image: ')
    if os.path.exists(image):
        index1 = image.rfind('/')
        if index1 == -1:
            index1 = image.rfind('\\')
        index2 = image.find('.')
        fileName = image[index1 + 1: index2]
        break
    else:
        print("Your file doesn't exists!")
while True:
    factorStr = input('Input your conversion factor (0~255, white->black), eg：125. Your factor: ')
    factor = int(factorStr)
    if factor < 0 or factor > 255:
        print("Your factor is out of range, please input again.")
    else:
        break

print("Converting~")
img = cv2.imread(image)
# cv2.imshow('before', img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
row, col = gray.shape
for i in range(row):
    for j in range(col):
        if gray[i][j] >= factor:
            gray[i][j] = 255
        else:
            gray[i][j] = 0

# cv2.imshow('after',gray)

# kernel = np.ones((3,3),np.uint8)  
# dilation = cv2.dilate(img,kernel,iterations = 1)
# cv2.imwrite('dilation.jpg',dilation)
# cv2.imshow('dil_img', dilation)

cv2.imwrite('new_' + fileName + factorStr + '.jpg', gray)
print("Save as " + 'new_' + fileName + '.jpg')
if cv2.waitKey() == 27:
    cv2.destroyAllWindows()