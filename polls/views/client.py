from django.shortcuts import render

from ..models.client import Client

def new_client(request):

    if request.method == 'GET':
        print('DEBUG=> views.client.new_client: method==GET')

        context = {}
        return render(request, 'polls/client/new_client.html', context)
    
    if request.method == 'POST':
        print('DEBUG=> views.client.new_client: method==POST')
        for key, val in request.POST.items():
            print('DEBUG=> views.client.new_client: key==' + key)
            print('DEBUG=> views.client.new_client: val==' + str(val))
            print('DEBUG=> views.client.new_client: type(val)==' + str(type(val)))

        context = {}
        return render(request, 'polls/client/new_client.html', context)