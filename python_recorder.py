import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

frequency = 41100
duration = int(input("how much time you want to record(sec): "))
print("Recording....., start speaking")
ourvoice  = sd.rec(int(duration*frequency),samplerate =  frequency, channels=2)
sd.wait()

write("myrecording" , frequency, ourvoice )
