import cv2
import numpy as np
import pyautogui

from moviepy.video.io.VideoFileClip import VideoFileClip


screen_size = pyautogui.size()

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_record.avi", fourcc, 50.0, screen_size)

try:
    while True:
        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        out.write(frame)

        if cv2.waitKey(1) == ord("q"):
            break

finally:
    out.release()
    cv2.destroyAllWindows()
    correct_fps = 50
    clip = VideoFileClip("screen_record.avi")
    clip.write_videofile("screen_record_fixed.mp4", fps=correct_fps, codec='libx264')
