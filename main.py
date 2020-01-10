import librosa
import librosa.display

a, sr = librosa.load('1.wav')
librosa.display.waveplot(a, sr=sr)

import matplotlib.pyplot as plt
plt.show()