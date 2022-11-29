import json
# import stripe

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render

from rest_framework import generics
from . import models, serilize, perms

# Create your views here.
class PlaceList(generics.ListCreateAPIView):
  serializer_class = serilize.PlaceSerializer

  def get_queryset(self):
    return models.Place.objects.filter(owner_id=self.request.user.id)

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [perms.IsOwnerOrReadOnly]
  serializer_class = serilize.PlaceDetailSerializer
  queryset = models.Place.objects.all()

class CategoryList(generics.CreateAPIView):
  permission_classes = [perms.PlaceOwnerOrReadOnly]
  serializer_class = serilize.CategorySerializer

class CategoryDetail(generics.UpdateAPIView, generics.DestroyAPIView):
  permission_classes = [perms.PlaceOwnerOrReadOnly]
  serializer_class = serilize.CategorySerializer
  queryset = models.Category.objects.all()

class MenuItemList(generics.CreateAPIView):
  permission_classes = [perms.PlaceOwnerOrReadOnly]
  serializer_class = serilize.MenuItemSerializer

class MenuItemDetail(generics.UpdateAPIView, generics.DestroyAPIView):
  permission_classes = [perms.PlaceOwnerOrReadOnly]
  serializer_class = serilize.MenuItemSerializer
  queryset = models.MenuItem.objects.all()

def home(request):
  return render(request, 'index.html')

# stripe.api_key = settings.STRIPE_API_SECRET_KEY

# @csrf_exempt
# def create_payment_intent(request):
#   try:
#     data = json.loads(request.body)
#     intent = stripe.PaymentIntent.create(
#       amount = data['amount'] * 100,
#       currency = 'usd',
#       payment_method = data['payment_method']['id'],
#       off_session = True,
#       confirm = True,
#     )

#     order = models.Order.objects.create(
#       place_id = data['place'],
#       table = data['table'],
#       detail = json.dumps(data['detail']),
#       amount = data['amount'],
#       payment_intent = intent['id']
#     )

#     return JsonResponse({
#       "success": True,
#       "order": order.id,
#     })
#   except Exception as e:
#     return JsonResponse({
#       "success": False,
#       "error": str(e),
#     })

class OrderList(generics.ListAPIView):
  serializer_class = serilize.OrderSerializer

  def get_queryset(self):
    return models.Order.objects.filter(place__owner_id=self.request.user.id, place_id=self.request.GET.get('place'))

class OrderDetail(generics.UpdateAPIView):
  permission_classes = [perms.PlaceOwnerOrReadOnly]
  serializer_class = serilize.OrderSerializer
  queryset = models.Order.objects.all()