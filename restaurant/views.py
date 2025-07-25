from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# auth import
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes



# Create your views here.
def index(request):
    return render(request, 'index.html',{})

# class based view for Booking
# class BookingView(APIView):
#     def get(self,request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data) #return JSON
    
#     def post(self,request):
#             serializer = BookingSerializer(data=request.data)
            
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"status":"success","data":serializer.data})
            
# end of class based view for Booking

# class based view for MenuItem
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})