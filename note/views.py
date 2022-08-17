from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from note.models import Note


def list_view(request):
    try:
        notes = Note.objects.all()
    except Exception as e:
        print(e)
        return HttpResponseRedirect('/note/list_note.html')
    return render(request, 'note/list_note.html', locals())
