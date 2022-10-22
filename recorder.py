import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import cv2
import os
import time
from git import Repo


path="/home/abdou/recorder"


def voice_record():
    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 5

    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("./recording0.wav", freq, recording)

    # Convert the NumPy array to audio file
    wv.write("./recording1.wav", recording, freq, sampwidth=2)

def video_record():
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    writer = cv2.VideoWriter(f'{path}basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))
    cap.release()
    writer.release()
    cv2.destroyAllWindows()


def pusher():
    os.system("cd /home/abdou/recorder && ls")

def play_sound():
    pass


def manager():
    pass



def alarm(manager):
    #8h
    st=time.time()
    time.sleep(5)
    et=time.time()
    t_s= et - st
    t_m= t_s / 60
    t_h= t_m / 60
    while t_h < 8:
        manager()
    else:
        play_sound()






pusher()
r=Repo(path)
print(r)