import cv2
import sys
import numpy as np
import time
from PIL import Image

th = 15000  # 差分画像の閾値

def main():
    URL = sys.argv[1]
    s_video = cv2.VideoCapture(URL)
    ret, bg = s_video.read()
    bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

    while True:
        ret, frame = s_video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        mask = cv2.absdiff(gray, bg)
        mask[mask < 15] = 0
        # print(np.sum(mask))
        if th < np.sum(mask):
            pil_img = Image.fromarray(frame)
            pil_img.save('jpg/'+str(int(time.time()))+'_'+str(np.sum(mask))+'.jpg')
            ret, bg = s_video.read()
            bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
            time.sleep(0.5)

if __name__ == "__main__":
    main()
