import os
import librosa
import utils

import torch
import torchaudio

import matplotlib.pyplot as plt

DATA_TRAIN = './data/train'

waveform, sample_rate = torchaudio.load(os.path.join(DATA_TRAIN,'003b04435.flac'),normalization=True)
# utils.play_audio(waveform,sample_rate)
mel_specgram = torchaudio.transforms.MelSpectrogram(sample_rate)(waveform)

plt.imshow(mel_specgram.squeeze().numpy())
plt.show()

# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()