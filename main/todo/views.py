from django.shortcuts import render
from .models import Todo
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from random import randint


BASE_URL = "https://www.pinterest.com/search/pins/?q={}"


def home(request):

    todo_list = Todo.objects.all()

    return render(request, "todo/home.html", {"todo_list": todo_list,})


def newtodo(request):

    if request.POST.get('title', 'content'):
        todo_title = request.POST.get("title")
        todo_text = request.POST.get("content")

        IMAGE_LIST=['www.arttablo.com/upload/U-su-alti-balik-mercan-manzara-kanvas-tablo1446892539-800.jpg',
        "golos.ua/images/items/2015-05/09/djDtmwym6bQWdH67/img_top.jpg",
        "www.yachtrussia.com/files/381/598/1910x1000/Sochi_1.jpg",
        "auto.sevastopol.su/wp-content/uploads/2020/06/2020-06-14-21.09.07-avatars.mds_.yandex.net-23181edea5a5.jpg",
        "fainaidea.com/wp-content/uploads/2018/11/7-2-696x464.jpg"]
        
        son=randint(0,4)
        todo_image=IMAGE_LIST[son]        
        


        newtodoobject = Todo.objects.create(
            todo_title=todo_title, todo_text=todo_text,todo_image=todo_image)

    return HttpResponseRedirect('/')


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
