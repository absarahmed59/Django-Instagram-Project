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
    name = forms.CharField(label='Name',max_length=64)
    bio = forms.CharField(label='Bio',max_length=64)

class Accounts_(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')

class Posts_(forms.Form):
    text = forms.CharField(label='Post', max_length=2048)

class Comments_(forms.Form):
    text = forms.CharField(label='Comment')



 
# Create your views here.
suggested=['a','b','c']
followers=['a','b','c','d']
followings=[3,5,2,6]
friends=['a','b','c','d']
bookmarks=['x','y','z']


def home(request):
    if request.session['user']==None:
        request.session['user']='No Account'
        return render(request, 'app/ilogin.html',{'form':Accounts_()})
    posts = Posts.objects.all().values_list('text', flat=True)
    return render(request, 'app/ihome.html',    {
                                                'user': 'Anonymous' if request.session['user']==None else request.session['user'],
                                                'posts':suggested,
                                                'post':posts,
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
                posts = Posts.objects.all().values_list('text', flat=True)
                return render(request, 'app/ihome.html', {'user':request.session['user'], 'post':posts})
    return render(request, 'app/ilogin.html',{'form':Accounts_()})

def sign(request):
    if request.method=='POST':
        cred = Accounts_(request.POST)
        if cred.is_valid():
            u = cred.cleaned_data['username']
            p = cred.cleaned_data['password']
            user = Accounts(username=u, password=p)
            user.save()
            profile = Profile(user=user, name="", bio='This is a new user.')
            profile.save()
            request.session['user']=u
            return render(request, 'app/ihome.html', {'user':request.session['user']})
    return render(request, 'app/ilogin.html',{'form':Accounts_()})


def direct(request):
    return render(request, 'app/idirect.html')


def edit(request):
    if request.method == 'POST':
        form = Profile_(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            bio = form.cleaned_data['bio']
            user = request.session['user']
            profile = Profile.objects.get(user=user)
            profile.name = name
            profile.bio = bio
            profile.save()
            return render(request, 'app/iprofile.html', {'bio':bio, 'user':name})
    return render(request, 'app/iedit.html', {'form':Profile_()})

bio='abc'
#posts=['123','456','789']
followers=['a','b','c','d']
followings=['a','b','c','d']
friends=['a','b','c','d']
score=[65,84,52,16]
friendship=zip(friends,score)
#action=zip(['a','c'],['b','a'],[posts[1],posts[0]])
# [['a','b',posts[1]],['a','c',posts[0]]]
def profile(request):
    """Renders the profile page."""
    
    profile_ = Profile.objects.get(user=Accounts.objects.get(username=request.session['user']))
    posts = Posts.objects.filter(user=profile_.user).values_list('text')
    return render(request, 'app/iprofile.html', {'bio': profile_.bio,
                                                'posts':posts,
                                                'followers':followers,
                                                'followings':followings,
                                                'friendship':friendship,
                                                #'action':action,
                                                'user':profile_.name,
                                                'create':Posts_()})

def post(request):
    """Creates a new post."""
    if request.method == 'POST':
        form = Posts_(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user = Accounts.objects.get(username=request.session['user'])
            post = Posts(user=user, text=text, likes=0)
            post.save()
            posts = Posts.objects.filter(user=user).values_list('text')
            return render(request, 'app/iprofile.html', {'bio':bio, 
                                                'posts':posts,
                                                'followers':followers,
                                                'followings':followings,
                                                'friendship':friendship,
                                                #'action':action,
                                                'user':user})
    return render(request, 'app/iprofile.html', {'create':Posts_()})

def logout(request):
    """Logs out the user."""
    request.session['user'] = None
    return render(request, 'app/ihome.html', {'form':Accounts_(), 'user':request.session['user']})



p=['A','B']#profiles
l=[True,False]#likes
v=[3,5]#visits
c=['abc']#comments
lists=zip(p,l,v)
def story(request):
    a = request.session['user']
    if a:
        return render(request, 'app/istory.html', {'lists':lists,
                                          'c':c,
                                          'user':request.session['user']})

    return render(request, 'app/istory.html', {'lists':lists,
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

