import schedule
from time import sleep
import numpy as np
import cv2
from PIL import ImageGrab
import csv

def pil2cv(image):
    ''' PIL型 -> OpenCV型 '''
    new_image = np.array(image, dtype=np.uint8)
    if new_image.ndim == 2:  # モノクロ
        print('モノクロ')
        pass
    elif new_image.shape[2] == 3:  # カラー
        print('カラー')
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:  # 透過
        print('透過')
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image



def get_screenshot():
    img = ImageGrab.grab()
    new_img = pil2cv(img)
    cv2.imwrite('new_img.jpg', new_img)
    
    
from ultralytics import YOLO

# load pretrained model.
model = YOLO(model="yolov8n.pt")

# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]


def predictImage():
    source = "./new_img.jpg"

    results = model.predict(source,save=True)
    boxes = results[0].boxes
    personNum = 0
    for box in boxes:
        # class name
        cls = int(box.cls[0])            
        if classNames[cls] == "person":
            personNum+=1
    return personNum

def task():
    print("タスク実行中")
    get_screenshot()
    personNum = predictImage()
    with open("person_num.csv","a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([personNum])
        

schedule.every(30).seconds.do(task)

try:
    while True:
        schedule.run_pending() # 指定時間が来てたら実行、まだなら何もしない 
        sleep(1) # 待ち
except KeyboardInterrupt:
    print("end")
    