from ultralytics import YOLO
import cv2
import math
import random
import json

classNames = ['Bisconni Chocolate Chip Cookies 46.8gm', 'Coca Cola Can 250ml', 'Colgate Maximum Cavity Protection 75gm',
        'Fanta 250ml', 'Fresher Guava Nectar 500ml', 'Fruita Vitals Red Grapes 200ml',
        'Islamabad Tea 238gm', 'Kolson Slanty Jalapeno 18gm', 'Kurkure Chutney Chaska 62gm',
        'LU Candi Biscuit 60gm', 'LU Oreo Biscuit 19gm', 'LU Prince Biscuit 55.2gm',
        'Lays Masala 34gm', 'Lays Wavy Mexican Chili 34gm', 'Lifebuoy Total Protect Soap 96gm',
        'Lipton Yellow Label Tea 95gm', 'Meezan Ultra Rich Tea 190gm', 'Peek Freans Sooper Biscuit 13.2gm',
        'Safeguard Bar Soap Pure White 175gm', 'Shezan Apple 250ml', 'Sunsilk Shampoo Soft - Smooth 160ml',
        'Super Crisp BBQ 30gm', 'Supreme Tea 95gm', 'Tapal Danedar 95gm', 'Vaseline Healthy White Lotion 100ml']

#cap = cv2.VideoCapture("coba.jpg")

model = YOLO("C:\\xampp\\htdocs\\retail-checkout-price-detection\\yolo\\best.pt")


array = []
img = cv2.imread("C:\\xampp\\htdocs\\retail-checkout-price-detection\\yolo\\tes.jpg")

scale_percent = 60 # percent of original size
#width = int(img.shape[1] * scale_percent / 100)
#height = int(img.shape[0] * scale_percent / 100)
width = int(640)
height = int(640)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

results = model(resized, show = False)
for r in results:
    boxes = r.boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        #print(x1, y1, x2, y2)

        color1 = random.randrange(128, 255)
        color2 = random.randrange(128, 255)
        color3 = random.randrange(128, 255)

        cv2.rectangle(resized,(x1,y1),(x2,y2),(color1,color2, color3),3)

        conf = math.ceil((box.conf[0]*100))/100

        cls = int(box.cls[0])

        cv2.putText(img=resized, text=f'{classNames[cls]} {conf}', org=(max(0,x1), max(35,y1)-5),
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.5, color=(color1, color2, color3), thickness=2)
        array.append(classNames[cls])

harga = 0
for r in array:
    if (r == "Lifebuoy Total Protect Soap 96gm"):
        harga += 25000
    elif (r == "Fanta 250ml"):
        harga += 50000
    else:
        harga += 100000

#print(array)
json_string = json.dumps(array)
print(json.dumps(array))

# cv2.putText(img=img, text=f'Total Harga : {harga}', org=(50, 50),
#             fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 255, 0), thickness=3)

#cv2.imshow("Image",img)
cv2.imwrite("C:\\xampp\\htdocs\\retail-checkout-price-detection\\yolo\\hasil.jpg", resized)
cv2.waitKey(0)

