from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from pitter.models.user_model import User
import json
import jwt
import hashlib
from .keys import private_k


class Login(APIView):

    @csrf_exempt
    def post(self, request):
        user_query = json.loads(request.body)
        login = user_query['login']
        password = hashlib.sha256(user_query['password'].encode('utf-8')).hexdigest()
        user = User.objects.get(login=login, password=password)

        if user:
            payload = {
                'email': user.email_address,
                'name': user.profile_name,
            }
            token = jwt.encode(payload, private_k, algorithm='RS256')
            return HttpResponse(token)