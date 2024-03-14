from api_key import api_key
import requests
import time
import os


## upload file 
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcripe_endpoint = 'https://api.assemblyai.com/v2/transcript'
headers = { "authorization": api_key}

audio_file = 'sample.wav'

def upload_file (audio_file):
    def read_file(audio_file , chunk_size = 5_242_880):
        with open (audio_file , 'rb') as _file :
            while True:
                data = _file.read(chunk_size)
                if not data :
                    break
                yield data

    response = requests.post(upload_endpoint,headers=headers ,data= read_file(audio_file))
    audio_url = response.json()['upload_url']
    return audio_url


## transcripe
def transcripe(audio_url):
    transcripe_request = {'audio_url' : audio_url }
    response = requests.post(transcripe_endpoint,headers=headers ,json=transcripe_request)
    jop_id = response.json()['id']
    return jop_id

audio_url = upload_file (audio_file)
jop_id = transcripe(audio_url)


## poll

def poll(jop_id):
    polling_endpoint = transcripe_endpoint + '/' + jop_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()

def get_transcription_result_url(audio_url):
    jop_id = transcripe(audio_url)
    while True:
        data = poll(jop_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        print("waiting time ...")
        time.sleep(30)


def get_first_name(audio_file):
    file_name = os.path.basename(audio_file)
    first_name = os.path.splitext(file_name)[0]
    return first_name

def save_transcripe(audio_url , audio_file):
    first_name = get_first_name(audio_file)
    data, error = get_transcription_result_url(audio_url)
    if data:
        text_file = first_name + '.txt'
        with open(text_file, 'w') as f:
            f.write(data['text'])
        print('Transcript saved')
    elif error:
        print("Error!!!", error)
