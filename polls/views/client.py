from django.shortcuts import render

from ..models.client import Client

def new_client(request):

    if request.method == 'GET':
        print('DEBUG=> views.client.new_client: method==GET')
    
    if request.method == 'POST':
        print('DEBUG=> views.client.new_client: method==POST') 