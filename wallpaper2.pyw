import cv2
import time
import ctypes
import glob
import os.path
import random

def get_random_mp4(previous_mp4):
    files = glob.glob(os.path.join(dir, '*.mp4'))
    mp4_name = random.choice(files)
    while mp4_name == previous_mp4:
        mp4_name = random.choice(files)
    return mp4_name

def get_frames(mp4_name):
    mp4_name = mp4_name.replace('.\\', '')
    print(f"{mp4_name=}")
    vidcap = cv2.VideoCapture(mp4_name)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
    return count

print(time.time())
dir = '.'
files = glob.glob(os.path.join(dir, '*.mp4'))
print(files)
timer = time.time() - 60
count = 0
mp4_file = ''
while True:
    while time.time() - timer < 60:
        for i in range(count):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, f"C:\\Users\\gtraw\\OneDrive\\Pulpit\\wallpapers\\frame{i}.jpg" , 0)
            time.sleep(0.08)
    mp4_file = get_random_mp4(mp4_file)
    count = get_frames(mp4_file)
    timer = time.time()