import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from user.models import User


def register_view(request):

    if request.method == 'GET':

        return render(request, 'user/register.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_r = request.POST['password_r']
        if not password == password_r:
            return HttpResponse('password is not the same ')

        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('already register')
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            print(e)
            return HttpResponse('already register')
        request.session['username'] = username
        request.session['uid'] = user.id
        return HttpResponseRedirect('/index')


def login_view(request):

    if request.method == 'GET':

        if request.session.get('username') and request.session.get('uid'):
            return HttpResponseRedirect('/index')
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            return HttpResponse('already login2')

        return render(request, 'user/login.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()
        try:
            user = User.objects.get(username=username)
            if password_m != user.password:
                return HttpResponse('username or password is wrong ')

        except Exception as e:
            print(e)
            return HttpResponse('username or password is wrong')

        request.session['username'] = username
        request.session['uid'] = user.id
        resp = HttpResponseRedirect('/index')
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600*24*3)
            resp.set_cookie('uid', user.id, 3600*24*3)
        return resp
