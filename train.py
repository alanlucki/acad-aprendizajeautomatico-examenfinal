import os
import librosa
import ffmpy
import time
import subprocess
import numpy as np
import pandas as pd
import wave
import contextlib
#import pyaudio
import xlsxwriter
import math  
    
from shutil import rmtree
from pytube import YouTube

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [20, 10]

pathSrc = 'src/'

def transformMpegToWav(filename):
    os.system(str('ffmpeg -i {}.mpeg {}.wav').format(filename,filename) )

def segmentFile(samples,fileName):
    '''
    Funcion que segmenta los audios de acuerdo a la cantidad de frames y los
    guarda de acuerdo a la siguiente etiqueta:
    - ##_###_{segmento}.wav
    '''
    duration = 0
    transformMpegToWav(pathSrc + filename)
    origen = pathSrc + fileName +'.wav'

    with contextlib.closing(wave.open(origen,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    for i in range(0, samples):        
        destino = pathSrc + fileName + '/' + fileName +'_'+ '{0}'.format(str(i + 1).zfill(3))
        print(destino)
        tiempo_inici = i * (duration/samples)
        str_inci = ''
        if int(tiempo_inici) <= 10:
            str_inci = '0' + str(int(tiempo_inici))
        else:
            str_inci = str(int(tiempo_inici))
        str_duracion = ""
        if int((duration/samples)) > 9:
            str_duracion = str(int((duration/samples)))
        else:
            str_duracion = '0' + str(int((duration/samples)))    
        os.system(str('ffmpeg -ss 00:00:' + str_inci +' -t 00:00:' + str_duracion + ' -i {} -acodec pcm_s16le -ar 44000 {}.wav').format(origen,destino) )
        
segmentFile(360,'rpp_01') 