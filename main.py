import os
import streamlit
import matplotlib as mpl
import librosa
from librosa import display
from sys import platform
chunk = 1024

if platform == "win32":
    SAMPLE_DIR = '\\samples\\' #windows deving ARGH!!
else:
    SAMPLE_DIR = '/samples/'

# solution to overflow error below did not work
# increase limit in number of data points in matplotlib
# mpl.rcParams['agg.path.chunksize'] = 500000000

class AudioStruct:
    def __init__(self, name, sample):
        self.name = name
        self.sample = sample

def main():
    
    # scan through samples and load each one.
    fileList = []
    for filestr in os.listdir(os.getcwd() + SAMPLE_DIR):
        with open(os.path.join(os.getcwd() + SAMPLE_DIR + filestr), 'rb') as data:

            fileListItem = AudioStruct(filestr, data.read())
            fileList.append(fileListItem)

    #plot each file using data collected previously
    for i in fileList:
        fig, ax = mpl.pyplot.subplots(1, 1)
        mpl.pyplot.ylabel('Amplitude')
        mpl.pyplot.title(i.name)
        
        filename = os.path.join(os.getcwd() + SAMPLE_DIR) + i.name
        
        y,sr = librosa.load(filename, sr=22050)
        librosa.display.waveplot(y, sr, ax=ax, x_axis='time')
        
        streamlit.pyplot(fig)
        streamlit.audio(i.sample, format='audio/wav')

main()

# Playing audio
# ------
#
# import pyaudio
# import wave
# wf = wave.open(AUDIO_FILE, 'rb')
# p = pyaudio.PyAudio()

# stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
#                 channels = wf.getnchannels(),
#                 rate = wf.getframerate(),
#                 output = True)

# data = wf.readframes(chunk)
# while data != '':
#     stream.write(data)
#     data = wf.readframes(chunk)

# stream.close()
# p.terminate()