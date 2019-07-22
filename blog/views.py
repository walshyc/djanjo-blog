from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'ConorW',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates beatae quasi, officiis alias ducimus soluta sed explicabo, ratione reiciendis nesciunt ullam atque. In voluptatem quibusdam, quo enim maxime hic velit animi natus dolores assumenda impedit alias corrupti molestiae officia. Illum quas vero temporibus natus aspernatur!',
        'date_posted': 'March 7, 2019'
    },
    {
        'author': 'WalshyC',
        'title': 'Blog Post 2',
        'content': 'Iure velit veniam rerum molestias voluptates beatae quasi, officiis alias ducimus soluta sed explicabo, ratione reiciendis nesciunt ullam atque. In voluptatem quibusdam, quo enim maxime hic velit animi natus dolores assumenda impedit alias corrupti molestiae officia. Illum quas vero temporibus natus aspernatur!',
        'date_posted': 'March 25, 2019'
    }

]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})