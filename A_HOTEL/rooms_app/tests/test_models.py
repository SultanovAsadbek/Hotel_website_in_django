from django.test import TestCase
from rooms_app.models import Room, BookingRoom
from django.utils import timezone
from rooms_app.forms import BookRoomForm

# models test
class BookingRoomTest(TestCase):

    def create_BookingRoom(self, 
                    name = 'Asadbek',  
                    surname = 'Sultanov', 
                    email = 'sultanovv@gmail.com',
                    telephone_number = '+ 99890 660 79 19',
                    book_room = 'Двухместный  номер PRESTIGE',
                    commentary = 'На одного',
                    date_in = '2023-05-20',
                    date_out = '2023-05-24',
                    time_create = timezone.now(),
                    ):
        
        return BookingRoom.objects.create(
                                        name = name,
                                        surname = surname,
                                        email = email,
                                        telephone_number = telephone_number,
                                        book_room = book_room,
                                        commentary = commentary,
                                        date_in = date_in,
                                        date_out = date_out,
                                        time_create = time_create,
                                          )

    def test_bookingroom_creation(self):
        w = self.create_bookingroom()
        self.assertTrue(isinstance(w, BookingRoom))
        self.assertEqual(w.__unicode__(), w.title)