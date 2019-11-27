import requests

from pitter.models.user_model import User
from pitter.models.pitt_model import Pitt
from pitter.models.follower_model import Follower
from django.views.decorators.csrf import csrf_exempt
import json
import hashlib
from django.core.mail import EmailMultiAlternatives


@csrf_exempt
def register(request):
    user_query = json.loads(request.body)
    id = user_query['id']
    login = user_query['login']
    password = hashlib.sha256(user_query['password'].encode('utf-8')).hexdigest()
    profile_name = user_query['profile_name']
    email_address = user_query['email_address']
    email_notifications_mode = user_query['email_notifications_mode']
    User.create_user(id, login, password, profile_name, email_address, email_notifications_mode)


@csrf_exempt
def delete(request):
    user_query = json.loads(request.body)
    delete_id = user_query['id']
    user_do_delete = User.objects.get(id=delete_id)
    user_do_delete.delete()


@csrf_exempt
def make_pitt(request):
    data = json.loads(request.body)
    user_id = data['id']
    user = User.objects.get(id=user_id)
    user_info = {'user_id': user.id, 'audio_path': 'audio.flac'}
    return user_info


@csrf_exempt
def save_pitt(request):
    data = request.body.decode('utf-8').split('&')
    user_id = data[0][8:]
    audio_path = data[1][11:]
    audio_decoded = data[2][14:]
    Pitt.create_pitt(user_id, audio_path, audio_decoded)


@csrf_exempt
def follow_user(request):
    data = json.loads(request.body)
    follower_id = data['follow_user_id']
    user_id = data['user_id']
    subscription_flag = data['subscription_flag']
    Follower.create_follower(user_id, follower_id, subscription_flag)

    find_follower = User.objects.get(id=follower_id)
    follower_login = find_follower.login
    mailto_user = User.objects.get(id=user_id)
    email = mailto_user.email_address
    r = requests.post(
        url="https://api.mailgun.net/v3/sandboxb3f7b13f20844cedaf8e5a0e05cdb824.mailgun.org/messages",
        auth=("api", "3adac155c921fea3423695a3acee1e58-e470a504-39684050"),
        data={"from": "mailgun@sandboxb3f7b13f20844cedaf8e5a0e05cdb824.mailgun.org",
              "to": email,
              "subject": "New follower",
              "text": f'You have one new follower. His login: {follower_login}'}
    )


@csrf_exempt
def delete_subscription(request):
    data = json.loads(request.body)
    delete_id = data['follow_user_id']
    user_do_delete = Follower.objects.get(follower_id=delete_id)
    user_do_delete.delete()





