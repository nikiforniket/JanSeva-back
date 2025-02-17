# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import generics, status

from juser.serializers import RegisterUserSerializer

User = get_user_model()


class RegisterUserSerializer(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "User registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        "message": "Please provide correct values for user registration.",
                        "error": serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except ValidationError as e:
            return Response(
                {"message": f"{e.__class__.__name__} : {e}", "error_code": 4001},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"message": f"{e.__class__.__name__} : {e}", "error_code": 5001},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )