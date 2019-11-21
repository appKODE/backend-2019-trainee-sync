from django.http import HttpResponse
from pitter.integrations.speech_to_text import SpeechToText
from pitter.account_actions.registration import registration
from pitter.account_actions.delete import delete


def voice(request):
    return HttpResponse(SpeechToText.speech_to_text())


def register(request):
    registration()
    return HttpResponse('Registration is completed.')


def delete_account(request):
    delete()
    return HttpResponse('Account is deleted.')