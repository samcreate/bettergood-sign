import alsaaudio as aa
import wave
from struct import unpack
import numpy as np


spectrum  = [1,1,1,3,3,3,2,2]
matrix    = [0,0,0,0,0,0,0,0]
power     = []
weighting = [2,8,8,16,16,32,32,64] 

# Audio setup
wavfile = wave.open('buzz.wav','r')
sample_rate = wavfile.getframerate()
no_channels = wavfile.getnchannels()
chunk       = 4096 # Use a multiple of 8

# ALSA
output = aa.PCM(aa.PCM_PLAYBACK, aa.PCM_NORMAL)
output.setchannels(no_channels)
output.setrate(sample_rate)
output.setformat(aa.PCM_FORMAT_S16_LE)
output.setperiodsize(chunk)

# Return power array index corresponding to a particular frequency
def piff(val):
   return int(2*chunk*val/sample_rate)
   
def calculate_levels(data, chunk,sample_rate):
   global matrix

   # Convert raw data (ASCII string) to numpy array
   data = unpack("%dh"%(len(data)/2),data)
   data = np.array(data, dtype='h')

   # Apply FFT - real data
   fourier=np.fft.rfft(data)
   # Remove last element in array to make it the same size as chunk
   fourier=np.delete(fourier,len(fourier)-1)
   # Find average 'amplitude' for specific frequency ranges in Hz
   power = np.abs(fourier)   
   matrix[0]= int(np.mean(power[piff(0)    :piff(156):1]))
   matrix[1]= int(np.mean(power[piff(156)  :piff(313):1]))
   matrix[2]= int(np.mean(power[piff(313)  :piff(625):1]))
   matrix[3]= int(np.mean(power[piff(625)  :piff(1250):1]))
   matrix[4]= int(np.mean(power[piff(1250) :piff(2500):1]))
   matrix[5]= int(np.mean(power[piff(2500) :piff(5000):1]))
   matrix[6]= int(np.mean(power[piff(5000) :piff(10000):1]))
   matrix[7]= int(np.mean(power[piff(10000):piff(20000):1]))

   # Tidy up column values for the LED matrix
   matrix=np.divide(np.multiply(matrix,weighting),1000000)
   # Set floor at 0 and ceiling at 8 for LED matrix
   matrix=matrix.clip(0,8)
   return matrix


# Start reading .wav file  
data = wavfile.readframes(chunk)
# Loop while audio data present
while data!='':
   output.write(data)   
   matrix=calculate_levels(data, chunk,sample_rate)
   for y in range (0,8):
       for x in range(0, matrix[y]):
          print(x,y)
         #   display.set_pixel(x, y, spectrum[x])
   data = wavfile.readframes(chunk)
   
