import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(filename="output.wav", duration=5, fs=44100):
    print("🎙️ Recording started...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    write(filename, fs, recording)  # Save as WAV file
    print(f"✅ Recording saved to {os.path.abspath(filename)}")
