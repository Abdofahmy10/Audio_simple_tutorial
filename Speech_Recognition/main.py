from comm import upload_file , save_transcripe

audio_file = 'sample.wav'

audio_url = upload_file (audio_file)
save_transcripe(audio_url , audio_file)
