from .serializer import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework .parsers import JSONParser
from rest_framework import generics, filters
from rest_framework.templatetags.rest_framework import data
import os


# Create your views here.

def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def check_login(request, email):
    try:
        user = User.objects.filter(email=email)
    except:
        return JsonResponse(status=400)

    if request.method == 'GET':
        serializer = UserSerializer(User, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)


def item_list(request):
    if request.method == 'GET':
        item = Item.objects.all().order_by('createDate').reverse()
        serializer = ItemSerializer(item, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def item_by_id(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=201)


def item_seller(request, storeId):
    try:
        item = Item.objects.filter(storeId=storeId)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(item, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=201)


def itemImg_list(request):
    if request.method == 'GET':
        itemImg = ItemImg.objects.all()
        serializer = ItemImgSerializer(itemImg, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemImgSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def itemImg_item_id(request, itemId):
    try:
        itemImg = ItemImg.objects.filter(itemId=itemId)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ItemImgSerializer(itemImg, many=True)
        return JsonResponse(serializer.data, safe=False)


def itemImg_by_id(request, id):
    try:
        itemImg = ItemImg.objects.get(pk=id)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ItemImgSerializer(itemImg)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        itemImg.delete()
        return HttpResponse(status=201)
