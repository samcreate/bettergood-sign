"""Usage:
    amplitudes WAV_FILE

    Returns the (linear) amplitude of the signal inside the wav file, sample by sample.
"""
from __future__ import division
from pygame import mixer

import scipy.io.wavfile

mixer.init()
buzz = mixer.Sound('buzz.wav')

MAX_WAV16_AMP = 10  # = 2**15-1  # because wav16 is signed (wav8 isn't)


rate, amp_arr = scipy.io.wavfile.read('buzz.wav')

buzz.play()

for amp in (amp_arr / MAX_WAV16_AMP):
    if(amp[0] >220):
        print(amp)