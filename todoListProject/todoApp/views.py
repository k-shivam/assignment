from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import requests
from django.template import RequestContext
from django.forms import ModelForm
from .forms import todoModelForm
from .models import todoModel
from django.contrib import messages
from django.core import serializers
import json


def home(request):
    todo = todoModel.objects.all()
    form = todoModelForm()
    return render(request, 'index.html', {'form': form, 'todo': todo})


def todoPost(request):
    if request.method == 'POST' and request.is_ajax():  # if the form has been submitted
        form = todoModelForm(request.POST)
        if form.is_valid():
            form.save()
        todo_json = serializers.serialize('json', todoModel.objects.order_by('-pk'))
        return HttpResponse(json.dumps(todo_json), content_type="application/json")
    return HttpResponse("status")


def delete(request, id):
    if request.method == "POST" and request.is_ajax:
        print("ajax")
        del_object = get_object_or_404(todoModel, pk=id)
        del_object.delete()
        todo_json = serializers.serialize('json', todoModel.objects.order_by('-pk'))
        return HttpResponse(json.dumps(todo_json), content_type="application/json")
    return HttpResponse("status")



