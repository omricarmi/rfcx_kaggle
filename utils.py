import torch
import torchaudio
# from playsound import playsound


def play_audio(src_vector,sample_rate):
    tmp_audio_file = "./tmptmp.flac"
    torchaudio.save(tmp_audio_file,src_vector,sample_rate)
    # TODO find function to play sound from vector
    # playsound(tmp_audio_file)