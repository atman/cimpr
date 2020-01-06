from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_jwt.settings import api_settings

from .serializers import UserRegisterSerializer

User = get_user_model()


class AuthAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)

        data = request.data
        username = data.get('username')
        password = data.get('password')

        qs = User.objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=username)
        ).distinct()

        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token=token, user=user,request=request)
                return Response(response)
        return Response({'detail': 'Invalid credentials'}, status=401)


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class RegisterAPIViewOld(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

        if request.user.is_authenticated:
            return Response({'detail': 'You are already registered and authenticated'}, status=400)

        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        password_2 = data.get('password2')

        if password != password_2:
            return Response({"detail": "Passwords do not match, please enter matching passwords"}, status=401)

        qs = User.objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=username)
        ).distinct()

        if qs.exists():
            return Response({"detail":"You are already registered! Please log in"}, status=401)
        else:
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = jwt_response_payload_handler(token=token, user=user, request=request)
            return Response(response, status=201)