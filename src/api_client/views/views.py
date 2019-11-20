from django.http import HttpResponse
from src.pitter.integrations.speech_to_text import SpeechToText


def voice(request):
    return HttpResponse(SpeechToText.speech_to_text())


