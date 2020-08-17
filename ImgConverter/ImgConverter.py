import cv2
import os
import sys

# print(str(sys.argv[0]))
# print(len(sys.argv))


def convertImage(arv, anImage, factor):
    fileName = getFileName(arv)
    print("Converting~", arv)
    img = cv2.imread(anImage)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    row, col = gray.shape
    for i in range(row):
        for j in range(col):
            if gray[i][j] >= factor:
                gray[i][j] = 255
            else:
                gray[i][j] = 0

    cv2.imwrite('new_' + fileName + str(factor) + '.jpg', gray)
    print("Save as " + 'new_' + fileName + '.jpg')
    if cv2.waitKey() == 27:
        cv2.destroyAllWindows()


def getFileName(imageName):
    if os.path.exists(imageName):
        index1 = imageName.rfind('/')
        if index1 == -1:
            index1 = imageName.rfind('\\')
        index2 = imageName.find('.')
        fileName = imageName[index1 + 1: index2]
        return fileName
    else:
        print("Your file doesn't exists!")
        return ""


if len(sys.argv) > 1:
    factor = 125
    factor_index = -1
    for i in range(1, len(sys.argv)):
        if str(sys.argv[i]) == "-f":
            if int(sys.argv[i+1]) < 0 or int(sys.argv[i+1]) > 255:
                print("Your factor is out of range[0, 255], set to default 100.")
            else:
                factor = int(sys.argv[i+1])
                factor_index = i

    for i in range(1,len(sys.argv)):
        if i == factor_index or i == factor_index + 1:
            continue
        if os.path.exists(sys.argv[i]):
            convertImage(str(sys.argv[i]), sys.argv[i], factor)
        else:
            print("File", str(sys.argv[i]), " doesn't exists!")
else:
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
    convertImage(image, image, factor)



# print("Converting~")
# img = cv2.imread(image)
# # cv2.imshow('before', img)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# row, col = gray.shape
# for i in range(row):
#     for j in range(col):
#         if gray[i][j] >= factor:
#             gray[i][j] = 255
#         else:
#             gray[i][j] = 0
#
# # cv2.imshow('after',gray)
#
# # kernel = np.ones((3,3),np.uint8)
# # dilation = cv2.dilate(img,kernel,iterations = 1)
# # cv2.imwrite('dilation.jpg',dilation)
# # cv2.imshow('dil_img', dilation)
#
# cv2.imwrite('new_' + fileName + factorStr + '.jpg', gray)
# print("Save as " + 'new_' + fileName + '.jpg')
# if cv2.waitKey() == 27:
#     cv2.destroyAllWindows()