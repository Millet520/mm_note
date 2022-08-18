from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from note.models import Note
from user.models import User


def list_view(request):
    try:
        notes = Note.objects.all()
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/note/list_note.html')
    username = request.session['username']
    return render(request, 'note/list_note.html', locals())


def add_view(request):
    if request.method == "GET":
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        username = User.objects.get(username=request.session['username'])
        Note.objects.create(title=title, content=content, user=username)
        return HttpResponse('save success...')
