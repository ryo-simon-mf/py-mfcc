import matplotlib.pyplot as plt
import librosa
import librosa.display

# a, sr = librosa.load('1.wav')
# librosa.display.waveplot(a, sr=sr)

# import matplotlib.pyplot as plt
# plt.show()

x, fs = librosa.load('53.wav', sr=44100)
librosa.display.waveplot(x, sr=fs, color='blue')

mfccs = librosa.feature.mfcc(x, sr=fs)

librosa.display.specshow(mfccs, sr=fs, x_axis='time')
plt.colorbar()
plt.show()