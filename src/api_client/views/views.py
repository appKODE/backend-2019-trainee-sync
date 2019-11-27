import json

import django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from pitter.acc_actions.user import register, delete, make_pitt, save_pitt, follow_user, delete_subscription
from pitter.acc_actions.login import Login
from pitter.acc_actions.auth import TokenAuthentication
import requests
from pitter.models import User


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
    user_info = make_pitt(request)
    user_id = user_info['user_id']
    audio_path = user_info['audio_path']
    data = {'user_id': user_id, 'audio_path': audio_path}
    headers = {"Content-Type": "application/json"}
    r = requests.post(url='http://localhost:8118/voice/', data=data, headers=headers)
    return HttpResponse('Sent')


@csrf_exempt
def savepitt(request):
    save_pitt(request)
    return HttpResponse('audio is recieved')


@csrf_exempt
def follow(request):
    if request.method == 'POST':
        follow_user(request)
        return HttpResponse('You are subscribed.')
    elif request.method == 'DELETE':
        delete_subscription(request)
        return HttpResponse('Subscription is deleted.')


@csrf_exempt
def getusers(request):
    all_users = User.objects.all()
    users_list = [x.login for x in all_users]
    return HttpResponse(f'{users_list}')


@csrf_exempt
def finduser(request):
    data = json.loads(request.body)
    login = data['login']
    try:
        user = User.objects.get(login=login)
        return HttpResponse(f'login: {user.login}\nemail: {user.email_address}')
    except User.DoesNotExist:
        return HttpResponse('User is not found.')