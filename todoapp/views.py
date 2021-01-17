from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .models import Contact, Todo

# Create your views here.


def index(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    data = {
        'todo_items': todo_items,
    }
    return render(request, 'todoapp/index.html', data)


def about(request):
    return render(request, 'todoapp/about.html')


def contact(request):
    return render(request, 'todoapp/contact.html')


def add_contact(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    textarea = request.POST.get('textarea')

    created_contact = Contact.objects.create(
        first_name=first_name, last_name=last_name, email=email, phone=phone, textarea=textarea)

    return HttpResponseRedirect('/')


def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']
    if content!='':
        created_obj = Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect('/')


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
