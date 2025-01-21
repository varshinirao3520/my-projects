import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import cv2
import shutil
import time
import imutils

li = ['Apple___Apple_scab\n\n\nPesticides:\nBonide Sulfur Plant Fungicide\nrganocide\nBonide Orchard Spray', 'Apple___Black_rot\n\n\nPesticides:\nPhysan 20\nNEEM oil\nCopper sprays\nOrchard Spray', 'Apple___Cedar_apple_rust\n\n\nPesticides:\nSERENADE Garden\nOrchard Spray\nSulfur Plant Fungicide',
      'Apple___healthy', 'Blueberry___healthy', 'Cherry___Powdery_mildew\n\n\nPesticides:\norganic compost\nNeem oil and PM Wash\nZero Tolerance Fungicide',
      'Cherry___healthy', 'Corn_(maize)___Cercospora_leaf_spot\n\n\nPesticides:\nsulfur sprays\ncopper-based fungicides\nGarden Dust',
      'Corn_(maize)___Common_rust\n\n\nPesticides:\nSERENADE Garden\nOrchard Spray\nSulfur Plant Fungicide', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
      'Grape___Black_rot\n\n\nPesticides:\nPhysan 20\nNEEM oil\nCopper sprays\nOrchard Spray', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight',
      'Grape___healthy', 'Orange___Haunglongbing', 'Peach___Bacterial_spot  \n\n\nPesticides:\nAtrazine\nDDT\nEndosulfan',
      'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight\n\n\nPesticides:\nFontelis\nEndura, Lance WDG\nCabrio\nReason',
      'Potato___Late_blight\n\n\nPesticides:\ncopper based fungicide\nOrganocide\nLiquid Copper', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
      'Squash___Powdery_mildew\n\n\nPesticides:\norganic compost\nNeem oil and PM Wash\nZero Tolerance Fungicide', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
      'Tomato___Early_blight\n\n\nPesticides:\nFontelis\nEndura, Lance WDG\nCabrio\nReason', 'Tomato___Late_blight\n\n\nPesticides:\ncopper based fungicide\nOrganocide\nLiquid Copper', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
      'Tomato___Spider_mites', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus\n\n\nPesticides:\nsulfur or copper-based fungicides\nGarden Dust\norganic fertilizers high in nitrogen\nLiquid Copper',
      'Tomato___Tomato_mosaic_virus\n\n\nPesticides:\nSafer Soap, Bon-Neem\nHarvest-Guard row cover\nleast-toxic herbicides\nAllDown', 'Tomato___healthy']


classifier = load_model('PLANT_MODEL.hdf5')

diseasename = None

root = tk.Tk()
root.title("Plant_Leaf")

root.geometry("800x600")
root.configure(background ="white")

title = tk.Label(text="Select An Image To Process", background = "white", fg="Brown", font=("", 15))
title.grid(row=0, column=2, padx=10, pady = 10)


def exit():
        root.destroy()

def clear():
        cv2.destroyAllWindows()
        disease = tk.Label(text='                                                                   \n\n\n\n\n', background="white",
                               fg="Black", font=("", 20))
        disease.grid(column=3, row=3, padx=10, pady=10)
        
def cap_process():
        maxid = 0
        image_path = path
        img = cv2.imread(image_path)
        imputimg = imutils.resize(img, width=300, height=300)
        cv2.imshow('original',imputimg)
        img = imutils.resize(img, width=120, height=120)
        original = img.copy()
        neworiginal = img.copy()

        #Calculating number of pixels with shade of white(p) to check if exclusion of these pixels is required or not (if more than a fixed %) in order to differentiate the white background or white patches in image caused by flash, if present.
        p = 0 
        for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                        B = img[i][j][0]
                        G = img[i][j][1]
                        R = img[i][j][2]
                        if (B > 110 and G > 110 and R > 110):
                                p += 1
                                
        #finding the % of pixels in shade of white
        totalpixels = img.shape[0]*img.shape[1]
        per_white = 100 * p/totalpixels

        #excluding all the pixels with colour close to white if they are more than 10% in the image
        if per_white > 10:
                img[i][j] = [200,200,200]
                #cv2.imshow('color change', img)


        #Guassian blur
        blur1 = cv2.GaussianBlur(img,(3,3),1)


        #mean-shift algo
        newimg = np.zeros((img.shape[0], img.shape[1],3),np.uint8)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER , 10 ,1.0)

        img = cv2.pyrMeanShiftFiltering(blur1, 20, 30, newimg, 0, criteria)
        #cv2.imshow('means shift image',img)


        #Guassian blur
        blur = cv2.GaussianBlur(img,(11,11),1)

        #Canny-edge detection
        canny = cv2.Canny(blur, 160, 290)

        canny = cv2.cvtColor(canny,cv2.COLOR_GRAY2BGR)

        #contour to find leafs
        bordered = cv2.cvtColor(canny,cv2.COLOR_BGR2GRAY)
        contours,hierarchy = cv2.findContours(bordered, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        maxC = 0
        for x in range(len(contours)):													#if take max or one less than max then will not work in
                if len(contours[x]) > maxC:													# pictures with zoomed leaf images
                        maxC = len(contours[x])
                        maxid = x

        perimeter = cv2.arcLength(contours[maxid],True)
        #print perimeter
        Tarea = cv2.contourArea(contours[maxid])
        cv2.drawContours(neworiginal,contours[maxid],-1,(0,0,255))
        #cv2.imshow('Contour',neworiginal)
        #cv2.imwrite('Contour complete leaf.jpg',neworiginal)



        #Creating rectangular roi around contour
        height, width, _ = canny.shape
        min_x, min_y = width, height
        max_x = max_y = 0
        frame = canny.copy()

        # computes the bounding box for the contour, and draws it on the frame,
        for contour, hier in zip(contours, hierarchy):
                (x,y,w,h) = cv2.boundingRect(contours[maxid])
                min_x, max_x = min(x, min_x), max(x+w, max_x)
                min_y, max_y = min(y, min_y), max(y+h, max_y)
                if w > 80 and h > 80:
                        roi = img[y:y+h , x:x+w]
                        originalroi = original[y:y+h , x:x+w]
                        
        if (max_x - min_x > 0 and max_y - min_y > 0):
                roi = img[min_y:max_y , min_x:max_x]	
                originalroi = original[min_y:max_y , min_x:max_x]

        #cv2.imshow('ROI', frame)
        #cv2.imshow('rectangle ROI', roi)
        img = roi


        #Changing colour-space
        #imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        imghls = cv2.cvtColor(roi, cv2.COLOR_BGR2HLS)
        #cv2.imshow('HLS', imghls)
        imghls[np.where((imghls==[30,200,2]).all(axis=2))] = [0,200,0]
        #cv2.imshow('new HLS', imghls)

        #Only hue channel
        huehls = imghls[:,:,0]
        #cv2.imshow('img_hue hls',huehls)
        #ret, huehls = cv2.threshold(huehls,2,255,cv2.THRESH_BINARY)

        huehls[np.where(huehls==[0])] = [35]
        #cv2.imshow('img_hue with my mask',huehls)


        #Thresholding on hue image
        ret, thresh = cv2.threshold(huehls,28,255,cv2.THRESH_BINARY_INV)
        #cv2.imshow('thresh', thresh)


        #Masking thresholded image from original image
        mask = cv2.bitwise_and(originalroi,originalroi,mask = thresh)
        masked = imutils.resize(mask, width=300, height=300)
        cv2.imshow('masked out img',masked)


        #Finding contours for all infected regions
        contours,heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        Infarea = 0
        for x in range(len(contours)):
                cv2.drawContours(originalroi,contours[x],-1,(0,0,255))
                #cv2.imshow('Contour masked',originalroi)
                
                #Calculating area of infected region
                Infarea += cv2.contourArea(contours[x])

        if Infarea > Tarea:
                Tarea = img.shape[0]*img.shape[1]

        #Finding the percentage of infection in the leaf


        try:
                per = 100 * Infarea/Tarea
        except ZeroDivisionError:
                per = 0
                
        per = round(per,2)

        print (f'Infected area:{Infarea}')
        print (f'Percentage of infection region:{per}')

        fiimg = imutils.resize(original, width=300, height=300)
        cv2.imshow('final',fiimg)
        disease = tk.Label(text='Infected area:' + str(per), background="white",
                        fg="Black", font=("", 15))
        disease.grid(column=3, row=3, padx=10, pady=10)
        button4 = tk.Button(text="clear", command=clear)
        button4.grid(row=6, column=2, padx=10, pady = 10)
        button5 = tk.Button(text="Exit", command=exit)
        button5.grid(row=7, column=2, padx=10, pady = 10)
        
def analysis():
    image_path = path
    new_img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(new_img)
    img = np.expand_dims(img, axis=0)
    img = img/255

    print("Following is our prediction:")
    prediction = classifier.predict(img)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)
    d = prediction.flatten()
    j = d.max()
    for index,item in enumerate(d):
        if item == j:
            class_name = li[index]
    print(class_name)
    diseasename = class_name
    disease = tk.Label(text='Status: ' + diseasename, background="white",
                               fg="Black", font=("", 15))
    disease.grid(column=3, row=3, padx=10, pady=10)
    button3 = tk.Button(text="Clear", command=clear)
    button3.grid(row=6, column=2, padx=10, pady = 10)
    button4 = tk.Button(text="Exit", command=exit)
    button4.grid(row=7, column=2, padx=10, pady = 10)

def openphoto():
    global path
    path=askopenfilename(filetypes=[("Image File",'')])
    im = Image.open(path)
    tkimage = ImageTk.PhotoImage(im)
    myvar=tk.Label(root,image = tkimage, height="224", width="224")
    myvar.image = tkimage
    myvar.place(x=1, y=0)
    myvar.grid(row=3, column=2 , padx=10, pady = 10)
    button2 = tk.Button(text="Analyse Image", command=analysis)
    button2.grid(row=4, column=2, padx=10, pady = 10)
    button7 = tk.Button(text="Process Image", command=cap_process)
    button7.grid(row=5, column=2, padx=10, pady = 10) 

def capture():
    global path
    cam = cv2.VideoCapture(0)
    time.sleep(0.5)
    ret, img = cam.read()
    captured = cv2.imwrite("./Captured_images/Captured.jpg", img)
    cam.release()
    path = "./Captured_images/Captured.jpg"
    frame = cv2.imread(path)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    cv2image = imutils.resize(cv2image, width=250)
    img = Image.fromarray(cv2image)
    tkimage = ImageTk.PhotoImage(img)
    myvar=tk.Label(root,image = tkimage, height="224", width="224")
    myvar.image = tkimage
    myvar.place(x=1, y=0)
    myvar.grid(row=3, column=2 , padx=10, pady = 10)
    button2 = tk.Button(text="Analyse Image", command=analysis)
    button2.grid(row=4, column=2, padx=10, pady = 10)
    button7 = tk.Button(text="Process Image", command=cap_process)
    button7.grid(row=5, column=2, padx=10, pady = 10)    

button1 = tk.Button(text="Select Image", command = openphoto)
button1.grid(row=1, column=2, padx=10, pady = 10)

capbut = tk.Button(text="Capture", command = capture)
capbut.grid(row=2, column=2, padx=10, pady = 10)

root.mainloop()
