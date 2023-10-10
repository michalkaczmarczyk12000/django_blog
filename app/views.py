from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view


@login_required(login_url='/login')
@api_view(['POST'])
def home(request, *args, **kwargs):
    return render(request, 'app/home.html')


# def login(request):
#     return render(request, 'app/login.html')
