from django.shortcuts import render
from django.http  import  HttpReponse

def  index(Request):
    return HttpReponse("欢迎使用萍乡学院图书馆学术资源共享系统")

# Create your views here.
