from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import createForm
from .models import Item, ToDoList

def index(response):
    return render(response, 'main/base.html', {})

def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    form = createForm()
    return render(response, 'main/create.html', {"form":form})