from django.contrib import admin

from rooms_app.models import Room
from rooms_app.models import BookingRoom


class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = (
        "id",
        "status",
        "max_capacity",
        "description",
        "decimail",
        "amount_rooms",
    )


class RoomBookingRoom(admin.ModelAdmin):
    model = BookingRoom
    list_display = (
        
        "id",
        "name",
        "surname",
        "email",
        "telephone_number",
        "book_room",
        "commentary",
        "date_in",
        "date_out",
        "time_create",
    )


admin.site.register(Room, RoomAdmin)
admin.site.register(BookingRoom, RoomBookingRoom)
