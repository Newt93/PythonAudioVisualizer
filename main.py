import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100
CHANNELS = 1

# Initialize the audio buffer
audio_buffer = np.zeros(SAMPLE_RATE)

# Define the callback function
def audio_callback(indata, frames, time, status):
    global audio_buffer
    audio_buffer = np.append(audio_buffer, indata[:,0])

# Start the audio stream
stream = sd.InputStream(callback=audio_callback, channels=CHANNELS, samplerate=SAMPLE_RATE)
stream.start()

# Plot the audio buffer
plt.plot(audio_buffer)
plt.show()
