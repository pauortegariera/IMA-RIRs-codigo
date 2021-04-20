import numpy as np
import scipy.io.wavfile 
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

# filtrado 



# grafico

plt.plot(t,k)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Filtro Invertido')
plt.show()