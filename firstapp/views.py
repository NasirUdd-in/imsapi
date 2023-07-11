from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from .models import Product, Category, Stock, Invoice
from .serializers import ProductSerializer, CategorySerializer, StockSerializer, InvoiceSerializer, RegisterSerializer, \
    UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Register API
@api_view(['POST'])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "User Created Successfully. Now perform Login to get your token",
        })
    return Response(serializer.errors, status=400)


# Product Stat
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh_token = request.data['refresh_token']
        token = RefreshToken(refresh_token)

        # Blacklist the refresh token to invalidate it
        token.blacklist()

        # Clear the user session
        session_key = request.session.session_key
        if session_key:
            # Retrieve the session object
            session = Session.objects.get(session_key=session_key)
            session_data = session.get_decoded()

            # Perform session cleanup actions (example: clear specific keys or all keys)
            session_data.pop('your_key', None)  # Remove a specific key from session data
            session_data.clear()  # Clear all keys from session data

            # Save the modified session data
            session.update({session.session_key: session_data})

        # Perform any additional logout-related actions here
        logout(request)

        return Response({"detail": "Logout successful."})
    except TokenError:
        return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_detail(request, pk):
    task = Product.objects.get(pk=pk)
    serializer = ProductSerializer(task)
    return Response(serializer.data)


@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def product_update(request, pk):
    task = Product.objects.get(pk=pk)
    serializer = ProductSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def product_delete(request, pk):
    task = Product.objects.get(pk=pk)
    task.delete()
    return Response(status=204)


# category start
@api_view(['GET'])
def category_list(request):
    products = Category.objects.all()
    serializer = CategorySerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, pk):
    task = Category.objects.get(pk=pk)
    serializer = CategorySerializer(task)
    return Response(serializer.data)


@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def category_update(request, pk):
    task = Category.objects.get(pk=pk)
    serializer = CategorySerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def category_delete(request, pk):
    task = Category.objects.get(pk=pk)
    task.delete()
    return Response(status=204)


# Stock start
@api_view(['GET'])
def stock_list(request):
    products = Stock.objects.all()
    serializer = StockSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def stock_detail(request, pk):
    task = Stock.objects.get(pk=pk)
    serializer = StockSerializer(task)
    return Response(serializer.data)


@api_view(['POST'])
def stock_create(request):
    serializer = StockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def stock_update(request, pk):
    task = Stock.objects.get(pk=pk)
    serializer = StockSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def stock_delete(request, pk):
    task = Stock.objects.get(pk=pk)
    task.delete()
    return Response(status=204)


# Invoice start
@api_view(['GET'])
def invoice_list(request):
    products = Invoice.objects.all()
    serializer = InvoiceSerializer(invoice_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def invoice_detail(request, pk):
    task = Invoice.objects.get(pk=pk)
    serializer = InvoiceSerializer(task)
    return Response(serializer.data)


@api_view(['POST'])
def invoice_create(request):
    serializer = InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def invoice_update(request, pk):
    task = Invoice.objects.get(pk=pk)
    serializer = InvoiceSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def invoice_delete(request, pk):
    task = Invoice.objects.get(pk=pk)
    task.delete()
    return Response(status=204)
