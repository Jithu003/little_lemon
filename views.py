from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, ListAPIView, DestroyAPIView
from .models import Booking, Menu
from .serializer import BookingSerializer, MenuSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny



# Create your views here.
def homeView(request):
    return render (request, "index.html")


class BookingView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItem(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    permission_classes = [IsAuthenticated]
