import numpy as np
import cv2
from PIL import ImageGrab

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

if __name__=="__main__":
    get_screenshot()