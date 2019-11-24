from pitter.models.user_model import User
from pitter.models.pitt_model import Pitt
from django.views.decorators.csrf import csrf_exempt
import json
import hashlib


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
def save_pitt(request):
    audio_decoded = request.POST['audio_decoded']
    audio_path = request.POST['audio_path']
    user_id = request.POST['user_id']
    id = request.POST['id']
    Pitt.create_pitt(id, user_id, audio_path, audio_decoded)
