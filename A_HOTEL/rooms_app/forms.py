from django import forms
from rooms_app.models import BookingRoom
from django.forms.widgets import DateInput
import datetime


class DateInput(forms.DateInput):
    input_type = "date"

 
class BookRoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["book_room"].empty_label = "Выберите номер"

    class Meta:
        model = BookingRoom
        fields = [
            "name",
            "surname",
            "email",
            "telephone_number",
            "book_room",
            "commentary",
            "date_in",
            "date_out",
        ]
        x = datetime.datetime.now()
        
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Имя", "tag": "input"}),
            "surname": forms.TextInput(
                attrs={"placeholder": "Фамилия", "tag": "input"}
            ),
            "email": forms.EmailInput(attrs={"placeholder": "Почта", "tag": "input"}),
            "telephone_number": forms.TextInput(
                attrs={
                    "placeholder": "Телефон номер",
                    "tag": "input",
                }
            ),
            "book_room": forms.Select(attrs={"tag": "select", "class": "bookRoom"}),
            "commentary": forms.Textarea(
                attrs={
                    "placeholder": "Комментария...",
                    "cols": 30,
                    "rows": 4,
                    "tag": "textarea",
                } 
            ),
            "date_in": DateInput(
                attrs={
                    "tag": "input",
                    "placeholder": "Дата приезда",
                    "onfocus": "(this.type='date')",
                    "onblur": "(this.type='text')",
                    "min": x.strftime("%Y-%m-%d"),
                }
            ),
            "date_out": DateInput(
                attrs={
                    "tag": "input",
                    "placeholder": "Дата отъезда",
                    "onfocus": "(this.type='date')",
                    "onblur": "(this.type='text')",
                    "min": x.strftime("%Y-%m-%d"),
                }
            ),
        }
