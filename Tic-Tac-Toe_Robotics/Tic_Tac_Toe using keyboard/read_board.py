from utlis import *

pathImage = 'board.png'
heightImg = 450
widthImg = 450

# Prepare the Image

img = cv2.imread(pathImage)
img = cv2.resize(img,(widthImg,heightImg)) #resize to square
imgBlank = np.zeros((heightImg,widthImg,3), np.uint8) # create a blank image
imgThreshold = preProcess(img)

# Find all the contours

imgContours = img.copy() #display Purpose
imgBigContour = img.copy() #display Purpose
contours, hierarchy = cv2.findContours(imgThreshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgContours, contours, -1, (0,255,0),3)

# Find the biggest Contour
biggest, maxArea = biggestContour(contours)   
print(biggest)
# if biggest.size != 0:
#     biggest = reorder(biggest)
#     cv2.drawContours(imgBigContour, biggest, -1, (0,255,0),10)
#     pts1 = np.float32(biggest)
#     pts2 = np.float32([0, 0], [widthImg,0],[0,heightImg],[widthImg,heightImg])
#     matrix = cv2.getPerspectiveTransform(pts1,pts2)
#     imgWrapColored = cv2.warpPerspective(img,matrix,(widthImg, heightImg))

imageArray = ([img,imgThreshold,imgContours,imgBlank],
            [imgBlank, imgBlank, imgBlank, imgBlank])
stackedImage = stackImages(1,imageArray)
cv2.imshow('Stacked Images',stackedImage)

cv2.waitKey(0)
cv2.destroyAllWindows()