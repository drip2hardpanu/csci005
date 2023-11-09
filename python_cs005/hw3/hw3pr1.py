# CS5 Gold, Lab 3
# Filename: hw3pr1.py
# Name:
# Problem description: Lab 3 problem, "Sounds Good!"

import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  # needed long ago
# if you are having trouble, comment out the above line...



# a function to get started with a reminder
# about list comprehensions...
def three_ize(L):
    """three_ize is the motto of the green CS 5 alien.
       It's also a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [3 * x for x in L]
    return LC



# Function to write #1:  scale
def scale(L, scale_factor):
    SC = [scale_factor*x for x in L]
    return SC


# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [3 * L[i] for i in range(N)]
    return LC



# Function to write #2:  add_2
def add_2(L,M):
    N=min(len(L), len(M))
    AT = [L[i] + M[i] for i in range(N)]
    return AT

# Function to write #3:  add_3
def add_3(L, M, P):
    N = min(len(L), len(M), len(P))
    AT = [L[i] + M[i] + P[i] for i in range(N)]
    return AT

# Function to write #4:  add_scale_2
def add_scale_2(L, M, L_scale, M_scale):
    N = min(len(L), len(M))
    lsc = float(L_scale)
    msc = float(M_scale)
    AT = [L[i]*lsc + M[i]*msc for i in range(N)]
    return AT

# Helper function:  randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x

# Function to write #5:  replace_some
def replace_some(L, chance_of_replacing):
    N = len(L)
    SC = [randomize(L[i], chance_of_replacing) for i in range(N)]
    return SC

#
# below are functions that relate to sound-processing ...
#


# a function to make sure everything is working
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# The example changeSpeed function
def changeSpeed(filename, newsr):
    """changeSpeed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    # we don't really need this line, but for consistency...
    newsr = newsr             # from the input! (not needed, a reminder!) 
    newsamps = samps          # same samples as before
    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'



def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'

# Sound function to write #1:  reverse

def reverse(filename):
    """reverse reverses the audio
       Argument: filename
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    newsamps = samps[::-1]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'

# Sound function to write #2:  volume

def volume(filename, scale_factor):
    """volume scales the volume of the audiofile
       Argument: filename, the scale factor desired
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    N = len(samps)
    newsamps = [samps[i]*scale_factor for i in range(N)]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'


# Sound function to write #3:  static

def static(filename, probability_of_static):
    """static adds static to the audio file
       Argument: filename, probability of static
       Result: no return value, but
               this creates the sound file 'out.wav' (which has static)
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    N = len(samps)
    newsamps = replace_some(samps, probability_of_static)
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'

# Sound function to write #4:  overlay
def overlay(filename1, filename2):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sounds...")
    play(filename1)
    play(filename2)

    samps1, sr1 = readwav(filename1)   # get samps and sr from the file!
    samps2, sr2 = readwav(filename2)

    N = min(len(filename1), len(filename2))

    newsamps = add_scale_2(samps1, samps2, .5, .5)
    newsr = (sr1+sr2)//2               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'

def overlaywinput(filename1, filename2, file1vol, file2vol):
    """overlay w input adds an overlay that can take percentage input to determine how loud each file is in relation to eachother
       Argument: filename, the name of the original file, file1volume, file2volume
       file1vol and file2vol must be less than 1
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sounds...")
    play(filename1)
    play(filename2)

    samps1, sr1 = readwav(filename1)   # get samps and sr from the file!
    samps2, sr2 = readwav(filename2)

    print("Computing new sound...")
 
    N = min(len(filename1), len(filename2))

    newsamps = add_scale_2(samps1, samps2, file1vol, file2vol)
    newsr = (sr1+sr2)//2               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'

# Sound function to write #5:  echo

def echo(filename, time_delay):
    """echo adds an echo
       Argument: filename, time_delay
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
               'out.wav' will add an echo proportional to time_delay to the sound
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("Computing new sound...")

    echosamps = [0]*(int(sr)*int(time_delay)) + samps
    mainsamps = samps + [0]*(int(sr)*int(time_delay))

    write_wav([mainsamps, sr], "out1.wav") 
    write_wav([echosamps, sr], "out2.wav") 

    overlaywinput('out1.wav','out2.wav', .66, .33)


# Helper function for generating pure tones
def gen_pure_tone(freq, seconds):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    # we get to pick our own sampling rate, sr
    sr = 22050
    # how many data samples to create
    nsamples = int(seconds*sr) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sr   # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    
    # now, create the sound!
    samps = [a*math.sin(f*n*freq) for n in range(nsamples)]
    sr = sr   # not needed, but a reminder
    return [samps,sr]


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Generating tone...")
    samps, sr = gen_pure_tone(freq, time_in_seconds)

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Writing out the sound data...")
    write_wav([samps, sr], "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')

# Sound function to write #6:  chord

def add_scale_3(L, M, F, L_scale, M_scale, F_scale):
    """add_scale 3 (L, M, F, L_scale, M_scale, F_scale
        Allows you to take three things and mix them accordingly
    """
    N = min(len(L), len(M), len(F))
    lsc = float(L_scale)
    msc = float(M_scale)
    fsc = float(F_scale)
    AT = [L[i]*lsc + M[i]*msc + F[i]*fsc for i in range(N)]
    return AT

def chord(f1, f2, f3, time_in_seconds):
    "plays a chord for a duration of time given three frequencies and the time in seconds"
    samps1, sr1 = gen_pure_tone(f1, time_in_seconds)
    samps2, sr2 = gen_pure_tone(f2, time_in_seconds)
    samps3, sr3 = gen_pure_tone(f3, time_in_seconds)

    newsamps = add_scale_3(samps1, samps2, samps3, .33, .33, .33)
    newsr = (sr1+sr2+sr3)//3             

    new_sound_data = [newsamps, newsr]
    write_wav(new_sound_data, "out.wav") 

    print("Playing new sound...")
    return play('out.wav')






