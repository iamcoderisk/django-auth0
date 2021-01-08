from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from .models import Product
def index(request):
    # products = [
    #     {'title': 'PlayStation', 'price': 300, 'image': 'https://cdn.auth0.com/blog/django-webapp/playstation.png'},
    #     {'title': 'iPhone', 'price': 900, 'image': 'https://cdn.auth0.com/blog/django-webapp/iphone.png'},
    #     {'title': 'Yummy Pizza', 'price': 10, 'image': 'https://cdn.auth0.com/blog/django-webapp/pizza.png'},
    # ]

    # context = {
    #     'products': products,
    # }
    # return render(request, 'webapp/index.html', context)
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'webapp/index.html', context)


@login_required
def profile(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'webapp/profile.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

def logout(request):
    django_logout(request)
    domain = 'dev-wvxgcz7a.us.auth0.com'
    client_id = '0YOlKsmuJrMcTJ0UL69Gl8LhDRjG8E5f'
    return_to = 'http://localhost:8000'
    return HttpResponseRedirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')
