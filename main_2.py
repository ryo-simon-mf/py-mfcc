import librosa
import librosa.display

a, fs = librosa.load('1.wav')
librosa.display.waveplot(a, sr=sr)

import matplotlib.pyplot as plt
plt.show()

mfccs = librosa.feature.mfcc(a, sr=fs)

librosa.display.specshow(mfccs, sr=fs, a_axis='time')
plt.colorbar()