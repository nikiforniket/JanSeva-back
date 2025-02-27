# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from juser.serializers import LoginSerializer

User = get_user_model()


class LoginView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                user = get_object_or_404(
                    User, phone_number=request.data["phone_number"]
                )
                rf = RefreshToken.for_user(user)
                return Response(
                    {
                        "message": "Success",
                        "access": str(rf.access_token),
                        "refresh": str(rf),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for login.",
                        "error": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Http404 as e:
            return Response(
                {"message": f"{e.__class__.__name__} : {e}", "error_code": 4001},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"message": f"{e.__class__.__name__} : {e}", "error_code": 5001},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
