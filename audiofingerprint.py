

"""Plots
Time in MS Vs Amplitude in DB of a input wav signal
"""

import numpy
import matplotlib.pyplot as plt
import pylab
from scipy.io import wavfile
from scipy.fftpack import fft


myAudio = '/home/admin1/Desktop/cat.wav'


samplingFreq, mySound = wavfile.read(myAudio)


mySoundDataType = mySound.dtype



mySound = mySound / (2.**15)



mySoundShape = mySound.shape
samplePoints = float(mySound.shape[0])

signalDuration =  mySound.shape[0] / samplingFreq


mySoundOneChannel = mySound[:,0]




timeArray = numpy.arange(0, samplePoints, 1)


timeArray = timeArray / samplingFreq


timeArray = timeArray * 1000

plt.plot(timeArray, mySoundOneChannel, color='G')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.show()

mySoundLength = len(mySound)


fftArray = fft(mySoundOneChannel)

numUniquePoints = int(numpy.ceil((mySoundLength + 1) / 2.0))
fftArray = fftArray[0:numUniquePoints]

fftArray = abs(fftArray)

fftArray = fftArray / float(mySoundLength)

fftArray = fftArray **2

if mySoundLength % 2 > 0:
    fftArray[1:len(fftArray)] = fftArray[1:len(fftArray)] * 2

else: 
    fftArray[1:len(fftArray) -1] = fftArray[1:len(fftArray) -1] * 2  

freqArray = numpy.arange(0, numUniquePoints, 1.0) * (samplingFreq / mySoundLength);


plt.plot(freqArray/1000, 10 * numpy.log10 (fftArray), color='B')
plt.xlabel('Frequency (Khz)')
plt.ylabel('Power (dB)')
plt.show()


freqArrayLength = len(freqArray)
print("freqArrayLength =", freqArrayLength)
numpy.savetxt("freqData.txt", freqArray, fmt='%6.2f')


print("fftArray length =", len(fftArray))
numpy.savetxt("fftData.txt", fftArray)
