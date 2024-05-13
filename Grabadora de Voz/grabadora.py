import sounddevice as sd
import scipy.signal as signal
import numpy as np

#Definición de parametros para grabar la voz
frecuencia_muestreo = 44100
duracion = 5

#Grabar la voz
print("Grabando...")
entrada_audio = sd.rec(int(duracion * frecuencia_muestreo), samplerate = frecuencia_muestreo, channels = 1, dtype = np.float32)
sd.wait()

frecuencia_corte_bajo = 4000
b, a = signal.butter(4, frecuencia_corte_bajo/(frecuencia_muestreo/2), "low")
filtered_audio = signal.lfilter(b, a, entrada_audio)

print("Audio original...")
sd.play(entrada_audio, samplerate = frecuencia_muestreo)
sd.wait()

print("Audio filtrado...")
sd.play(filtered_audio, samplerate = frecuencia_muestreo)
