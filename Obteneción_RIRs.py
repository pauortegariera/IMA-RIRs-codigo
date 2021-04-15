# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import scipy.io.wavfile
from matplotlib import pyplot as plt
import soundfile as sf


# LECTURA DE REGISTRO SONORO Y GENERACIÓN DE RIRs:

audio,fs = sf.read("/Users/paulaortega/Desktop/TP IMA - RIRS/prueba.wav") # Lectura del registro sonoro.
t= np.arange(len(audio))/fs # Tiempo de duración del archivo.

# creación del ssweep

w1=2*np.pi*20; # Frecuencia angular inicial
w2=2*np.pi*20000; # Frecuencia angular final
K=(w1/np.log(w2/w1))*t; # Parámetros para la correcta generación del barrido.
L=t/np.log(w2/w1);
y=np.sin(K*((np.exp(t/L))-np.ones((1,len(t))))); #Barrido

w=(K/L)*np.exp(t/L); # Parámetros para la correcta generación del filtro inverso.
m=w1/(2*np.pi*w);
k=m*np.fliplr(y);
k=k/max(abs(k));





fig,ax =plt.subplots()
ax.plot(t,k)
ax.set(xlabel='Tiempo(s)', ylabel='Amplitud')
plt.show()

