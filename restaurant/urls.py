#define URL route for index() view
from django.urls import path,include
from . import views
# from .views import BookingView
# from .views import MenuItemView

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
# router.register(r'menu', views.MenuItemView,basename='Menu')
router.register(r'tables', views.BookingViewSet,basename='Booking')


urlpatterns = [
    path('',views.index, name='index'),
    # path('booking',BookingView.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]


urlpatterns += router.urls

