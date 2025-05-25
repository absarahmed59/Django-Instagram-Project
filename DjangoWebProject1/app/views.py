"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django import forms
from django.shortcuts import render
from .models import Accounts, Posts, Comments, Profile


class Profile_(forms.Form):
    name = forms.CharField(label='Name',max_length=64)#, widget=forms.TextInput(attrs={'id':'name'})
    bio = forms.CharField(label='Bio',max_length=64)

class Accounts_(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')

class Posts_(forms.Form):
    text = forms.CharField(label='Post')

class Comments_(forms.Form):
    text = forms.CharField(label='Comment')



 
# Create your views here.
suggested=['a','b','c']
followers=['a','b','c','d']
followings=[3,5,2,6]
friends=['a','b','c','d']
bookmarks=['x','y','z']


def home(request):
    request.session['user']='No Account'
    return render(request, 
                  'home.html',
                  {
                        'user':request.session['user'],
                        'posts':suggested,
                        'bookmarks':bookmarks,
                        'friends':friends, 
                        'followings':followings
                  }
    )

def log(request):
    if request.method=='POST':
        cred = Accounts_(request.POST)
        if cred.is_valid():
            u = cred.cleaned_data['username']
            p = cred.cleaned_data['password']
            user = Accounts.objects.get(username=u)
            if user.password == p:
                request.session['user']=user.username
                return render(request, 'home.html', {'user':request.session['user']})
    return render(request, 'login.html',{'form':Accounts_()})

def sign(request):
    if request.method=='POST':
        cred = Accounts_(request.POST)
        if cred.is_valid():
            u = cred.cleaned_data['username']
            p = cred.cleaned_data['password']
            user = Accounts(username=u, password=p)
            user.save()
            request.session['user']=u
            return render(request, 'home.html', {'user':request.session['user']})
    return render(request, 'login.html',{'form':Accounts_()})
def direct(request):
    return render(request, 'direct.html')


def edit(request):

    return render(request, 'edit.html', {'form':Profile_()})

bio='abc'
posts=['123','456','789']
followers=['a','b','c','d']
followings=['a','b','c','d']
friends=['a','b','c','d']
score=[65,84,52,16]
friendship=zip(friends,score)
action=zip(['a','c'],['b','a'],[posts[1],posts[0]])
# [['a','b',posts[1]],['a','c',posts[0]]]
def profile(request):
    return render(request, 'profile.html', {'bio':bio,
                                            'posts':posts,
                                            'followers':followers,
                                            'followings':followings,
                                            'friendship':friendship,
                                            'action':action})



p=['A','B']#profiles
l=[True,False]#likes
v=[3,5]#visits
c=['abc']#comments
lists=zip(p,l,v)
def story(request):
    a = request.session['user']
    if a:
        return render(request, 'story.html', {'lists':lists,
                                          'c':c,
                                          'user':request.session['user']})

    return render(request, 'story.html', {'lists':lists,
                                          'c':c})

"""
def home(request):
    Renders the home page.
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
"""
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

