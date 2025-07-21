#define URL route for index() view
from django.urls import path,include
from . import views
# from .views import BookingView
# from .views import MenuItemView

# from rest_framework.routers import DefaultRouter
# import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

# router = DefaultRouter(trailing_slash=False)
# router.register(r'menu', views.MenuItemView,basename='Menu')
# router.register(r'tables', views.BookingViewSet,basename='Booking')


urlpatterns = [
    path('',views.index, name='index'),
    # path('booking',BookingView.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    # path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]


# urlpatterns += router.urls

