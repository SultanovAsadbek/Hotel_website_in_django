from django.urls import path
from rooms_app.views import bookRoomTwin 
from rooms_app.views import bookRoomPrestige 
from rooms_app.views import bookRoomDeluxe 
from rooms_app.views import bookRoomFamily 
from rooms_app.views import bookRoomTriple 
from rooms_app.views import bookRoomQuadr 
from rooms_app.views import bookRoom 

urlpatterns = [
    path("twin/", bookRoomTwin, name="twin"),
    path("prestige/", bookRoomPrestige, name="prestige"),
    path("deluxe/", bookRoomDeluxe, name="deluxe"),
    path("family/", bookRoomFamily, name="family"),
    path("triple/", bookRoomTriple, name="triple"),
    path("quadruple/", bookRoomQuadr, name="quadruple"),
    path("book_room/", bookRoom, name="book_room"),
]