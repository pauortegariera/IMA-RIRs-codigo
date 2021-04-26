import numpy as np
import scipy.io.wavfile 
from scipy import signal
from matplotlib import pyplot as plt
import soundfile as sf

# lectura del .wav

audio,fs = sf.read("/Users/Miguel Pelella/.spyder-py3/prueba.wav") # Lectura del registro sonoro.
t = np.arange(len(audio))/fs # Tiempo de duración del archivo.
T = t[len(t)-1]

# creación del sweep

w1 = 2*np.pi*20; # Frecuencia angular inicial
w2 = 2*np.pi*20000; # Frecuencia angular final
K = (w1/np.log(w2/w1))*T; # Parámetros para la correcta generación del barrido.
L = T/np.log(w2/w1);
y = np.sin(K*((np.exp(t/L))-1)); #Barrido

# modulacion

w = (K/L)*np.exp(t/L); # Parámetros para la correcta generación del filtro inverso.
m = w1/(2*np.pi*w);

# filtro invertido

tInvertido = np.flip(t)
yInvertido = np.sin(K*((np.exp(tInvertido/L))-1)); #Barrido
k = m*yInvertido;
k = k/max(abs(k));

# obtencion de IR

audioEspectro = np.fft.fft(audio)
kEspectro = np.fft.fft(k)
IR = audioEspectro*kEspectro

"""
En este caso el archivo de audio ya es una IR por eso da cualquier cosa el producto. 
Pero si fuese la toma de un Sweep, daria bien. 
"""

# filtrado 1/3

nyquistRate = 44100
factor = np.power(2,1.0/6.0)
centerFrequency_Hz = np.array([39, 50, 63, 79, 99, 125, 157, 198, 250, 315, 
397, 500, 630, 794, 1000, 1260, 1588, 2000, 2520, 3176, 4000, 5040, 6352, 8000, 10080, 
12704, 16000])
lowerCutoffFrequency_Hz=centerFrequency_Hz/factor;
upperCutoffFrequency_Hz=centerFrequency_Hz*factor;
filteredSpeech = []
for lower,upper in zip(lowerCutoffFrequency_Hz, upperCutoffFrequency_Hz):
    b, a = signal.butter( N=3, Wn=np.array([ lower, 
    upper])/nyquistRate, btype='bandpass', analog=False, 
    output='ba');
    filteredSpeech.append(signal.filtfilt(b, a, audio))


    
"""
filteredSpeechFFT= np.fft.fft(filteredSpeech)
plt.plot(t,filteredSpeechFFT)
plt.show()
plt.plot(t,audioEspectro)
plt.show()

# grafico

plt.plot(t,k)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Filtro Invertido')
plt.show()
"""