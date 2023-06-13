import sounddevice
from scipy.io.wavfile import write
print(sounddevice.query_devices())
fs = 48000
sounddevice.default.device = 1
myrecording = sounddevice.rec(int(3*fs), samplerate=fs, channels=1, blocking=True)
sounddevice.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", fs, myrecording)