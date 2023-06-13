import openai
import sounddevice
from scipy.io.wavfile import write
fs = 48000
sounddevice.default.device = 1
print('speak')
myrecording = sounddevice.rec(int(6*fs), samplerate=fs, channels=1, blocking=True)
sounddevice.wait()
print('stop')

write("recording.wav", fs, myrecording)

system_message = "You are a helpful voice assistant who gives short answers. You should only give longer answers if the user asks you to, or you are giving a list."
chat = [
  {"role": "system", "content": system_message}
]

audio_file = open("recording.wav", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file).text
chat.append({'role': 'user', 'content': transcript})
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=chat,
    temperature=.5,
    max_tokens=256
).choices[0].message.content
print(transcript)
print(completion)