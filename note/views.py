from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from note.models import Note
from user.models import User


def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)
    return wrap


def list_view(request):
    try:
        notes = Note.objects.all()
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/note/list_note.html')
    username = request.session['username']
    return render(request, 'note/list_note.html', locals())


@check_login
def add_view(request):
    if request.method == "GET":
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        username = User.objects.get(username=request.session['username'])
        Note.objects.create(title=title, content=content, user=username)
        return HttpResponse('save success...')
