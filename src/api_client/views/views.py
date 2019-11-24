import django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from pitter.acc_actions.reg_del import register, delete, save_pitt
from pitter.acc_actions.login import Login
from pitter.acc_actions.auth import TokenAuthentication


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        try:
            register(request)
            return HttpResponse('Registration is completed.')
        except django.db.utils.IntegrityError:
            return HttpResponse('User already exists.')
    elif request.method == 'DELETE':
        delete(request)
        return HttpResponse('Account is deleted.')


@csrf_exempt
def login(request):
    user_logged = Login()
    return HttpResponse(user_logged.post(request))


@csrf_exempt
def auth(request):
    user_auth = TokenAuthentication()
    return HttpResponse(user_auth.get(request))


@csrf_exempt
def makepitt(request):
    save_pitt(request)
    return HttpResponse('Pitt is added.')

