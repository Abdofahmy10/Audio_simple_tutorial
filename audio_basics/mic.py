import wave 
import pyaudio


format = pyaudio.paInt16
sample_rate = 3200
channels = 1
frames_per_buffer = 16000

audio = pyaudio.PyAudio()

stream = audio.open(
   format=format,
   channels=channels,
   rate=sample_rate,
   input=True,
   frames_per_buffer=frames_per_buffer
)

print("start  recording...")

frames = []
seconds = 20
for i in range(0, int(sample_rate / frames_per_buffer * seconds)):
    data = stream.read(frames_per_buffer)
    frames.append(data)

print("end recording...")

stream.stop_stream()
stream.close()
audio.terminate()


wf = wave.open("sample_2.wav", 'wb')
wf.setnchannels(channels)
wf.setsampwidth(audio.get_sample_size(format))
wf.setframerate(sample_rate)
wf.writeframes(b''.join(frames))
wf.close()