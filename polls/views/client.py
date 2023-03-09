from django.shortcuts import render

from ..models.client import Client

def add_client(request):

    context = {}

    print('DEBUG=> views.client.add_client: request.method==' + request.method)

    match request.method:

        case 'GET':
            return render(request, 'polls/client/add_client.html', context)
        
        case 'POST':
            # Create a new client
            print('DEBUG=> views.client.new_client: POST items:')
            for key, val in request.POST.items():
                print('DEBUG=> views.client.new_client: key==' + key)
                print('DEBUG=> views.client.new_client: val==' + str(val))
                print('DEBUG=> views.client.new_client: type(val)==' + str(type(val)))
            
            return render(request, 'polls/client/add_client.html', context)
        
        case _:
            context['status_code'] = '405 Method Not Allowed'
            return render(request, 'polls/bad_request.html', context)
    
def get_client(request, client_id):

    context = {
        "client_id": str(client_id)
    }

    print('DEBUG=> views.client.client: client.id==' + str(client_id))
    print('DEBUG=> views.client.client: request.method==' + request.method)

    print("\n")

    print('DEBUG=> views.client.new_client: POST items:')
    for key, val in request.POST.items():
        print('DEBUG=> views.client.new_client: key==' + key)
        print('DEBUG=> views.client.new_client: val==' + str(val))
        print('DEBUG=> views.client.new_client: type(val)==' + str(type(val)))
    
    print("\n")

    print('DEBUG=> views.client.new_client: GET items:')
    for key, val in request.GET.items():
        print('DEBUG=> views.client.new_client: key==' + key)
        print('DEBUG=> views.client.new_client: val==' + str(val))
        print('DEBUG=> views.client.new_client: type(val)==' + str(type(val)))
    
    print("\n")

    match request.method:

        case 'DELETE':
            # Delete the client with the specified id, if exists
            context['client_id'] = '300'
            return render(request, 'polls/client/client.html', context)
        
        case 'GET':
            # Get the client with the specified id, if it exists
            return render(request, 'polls/client/client.html', context)
        
        case 'POST':
            # Update the client with the specified id, if it exists
            context['client_id'] = '100'
            return render(request, 'polls/client/client.html', context)
        
        case _:
            context['status_code'] = '405 Method Not Allowed'
            return render(request, 'polls/bad_request.html', context)