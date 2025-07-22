API paths for Peer Testing...

Please use "python manage.py test tests/" to run the django.test. 

HTML Template Link:
/restaurant

Menu Items general search:
/restaurant/menu

Menu SingleItem search:
/restaurant/menu/{menuItemId} e.g /restaurant/menu/7

Booking List. Authentication needed ..
/restaurant/booking/
/restaurant/booking/tables
/restaurant/booking/tables/{bookingId}

DJOSER endpoint, for example, to make POST request and create new user:
/auth/users/ 

To login and auth get token:
/api-token-auth/ 

To login using DJOSER endpoint:
/auth/token/login 

Endpoints were thoroughly tested using Insomia.