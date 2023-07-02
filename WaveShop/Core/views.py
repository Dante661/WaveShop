import os

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import filters, generics
from rest_framework.parsers import JSONParser

from .serializer import *


# from rest_framework.templatetags.rest_framework import data


# Create your views here.


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def check_login(request, email):
    try:
        user = User.objects.filter(email=email)
    except:
        return HttpResponse(status=400)

    if request.method == "GET":
        serializer = UserSerializer(User, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)


@csrf_protect
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all().order_by("create_at").reverse()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_protect
def product_by_id(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        product.delete()
        return HttpResponse(status=201)


@csrf_protect
def product_seller(request, storeId):
    try:
        product = Product.objects.filter(storeId=storeId)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        product.delete()
        return HttpResponse(status=201)


@csrf_protect
def productImg_list(request):
    if request.method == "GET":
        productImgs = ProductImg.objects.all()
        serializer = ProductImgSerializer(productImgs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProductImgSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_protect
def productImg_product_id(request, productId):
    try:
        productImg = ProductImg.objects.filter(productId=productId)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductImgSerializer(productImg, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_protect
def productImg_by_id(request, id):
    try:
        productImg = ProductImg.objects.get(pk=id)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductImgSerializer(productImg)
        return JsonResponse(serializer.data)

    elif request.method == "DELETE":
        productImg.delete()
        return HttpResponse(status=201)


@csrf_protect
def product_by_category(request, category):
    try:
        product = Product.objects.filter(category=category)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_protect
def cart_list(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_protect
def cart_by_user_id(request, userId):
    try:
        cart = Cart.objects.filter(userId_id=userId).first()
    except:
        return JsonResponse(status=404)

    if request.method == "GET":
        serializer = CartSerializer(cart)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CartSerializer(cart, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.mehod == "DELETE":
        cart.delete()
        return JsonResponse(status=201)


@csrf_protect
def cart_item_list(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CartItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_protect
def cartItem_by_id(request, pk):
    try:
        cartItem = CartItem.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CartItemSerializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=True)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CartItemSerializer(cartItem, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        cartItem.delete()
        return HttpResponse(status=201)


@csrf_protect
def cartItem_by_cart_id(request, cartId):
    try:
        cartItem = CartItem.objects.filter(cartId=cartId)
    except:
        return JsonResponse(status=404)

    if request.method == "GET":
        serializer = CartItemSerializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)


class search_product(generics.ListAPIView):
    search_fields = ("title", "description", "category")
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@csrf_exempt
def create_store(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_protect
def get_store(request, userId):
    try:
        store = Store.objects.get(userId=userId)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = UserSerializer(store, many=True)
        return JsonResponse(serializer.data, safe=False)


class upload_file(generics.CreateAPIView):
    queryset = ImgUpload.objects.all()
    serializer_class = ImgUploadSerializer


def delete_file(request, filename):
    if request.method == "GET":
        ext = filename.split(".")[-1]
        filenamenoExt = filename.replace(f"{ext}", "")
        fileDir = "%s/%s.%s" % ("img", filenamenoExt, ext)
        if os.path.isfile((f"{img}/{filename}")):
            os.remove(fileDir)
            return HttpResponse(f"{filename} deleted")
        return HttpResponse("file not found")


def filter_min_price(request, minprice):
    try:
        products = Product.objects.filter(minprice=minprice)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_max_price(request, maxprice):
    try:
        products = Product.objects.filter(maxprice=maxprice)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_maxmin_price(request, maxprice, minprice):
    try:
        products = Product.objects.filter(price_maxmin=(maxprice, minprice))
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_rating(request, rating):
    try:
        products = Product.objects.filter(rating=rating)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_price_rating(request, minprice, maxprice, rating):
    try:
        products = Product.objects.filter(price_maxmin=(maxprice, minprice)).filter(
            rating=rating
        )
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_condition(request, condition):
    try:
        products = Product.objects.filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def filter_all(request, minprice, maxprice, rating, condition):
    try:
        products = (
            Product.objects.filter(price_maxmin=(maxprice, minprice))
            .filter(rating=rating)
            .filter(condition=condition)
        )
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_cart_item_by_cart_id(request, cartId):
    try:
        cartItem = (
            CartItem.objects.filter(cartId_id=cartId)
            .prefetch_related("productId")
            .order_by("create_at")
        )
    except:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = JoinSerializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)
