import base64
import os
# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from django.http import HttpResponse


class VoiceEncoder:

    @staticmethod
    def voice_encoding():
        import io
        # Instantiates a client
        client = speech.SpeechClient()

        file_name = os.path.join(os.path.dirname(__file__), 'audio.flac')

        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=48000,
            language_code='en-US')

        # Detects speech in the audio file
        response = client.recognize(config, audio)
        phrase = ''

        for result in response.results:
            phrase = result.alternatives[0].transcript
            # print('Transcript: {}'.format(result.alternatives[0].transcript))
        encoded_phrase = base64.b64encode(phrase.encode('utf-8'))
        return encoded_phrase


def voice(request):
    return HttpResponse(VoiceEncoder.voice_encoding())


