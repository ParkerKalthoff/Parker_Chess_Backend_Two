from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username, password)
    if user:
        login(request, user)
        return JsonResponse()


def signup(request):
    serializer = CustomUser(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUserSerializer.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)