from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Room(models.Model):
    status = models.TextField(
        verbose_name="Класс",
        unique=True
    )
    max_capacity = models.IntegerField(_("Максимальное вместимость"))
    description = models.TextField(_("Описание"))
    decimail = models.IntegerField(_("Стоимость(UZS)"))
    image1 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    image2 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    image3 = models.ImageField(upload_to="photos/%Y/%m/%d/")
    image4 = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True)
    amount_rooms = models.IntegerField(_("Количество комнат"))
    
    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Добавление комнаты"
        verbose_name_plural = "Добавление комнаты"


class BookingRoom(models.Model):
    name = models.CharField(_("Имя"), max_length=30)
    surname = models.CharField(_("Фамилия"), max_length=30)
    email = models.CharField(_("Почта"), max_length=50, unique=True)
    telephone_number = models.CharField(_("Телефон номер"), max_length=15, unique=True) 
    book_room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        max_length=30,
        verbose_name="Заброн. комната",
        null=True, 
    )
    commentary = models.TextField(_("Комментария"), blank=True)
    date_in = models.DateField(_("Дата входа"))
    date_out = models.DateField(_("Дата выхода"))
    time_create = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Забронированная комната"
        verbose_name_plural = "Забронированные комнаты"
        ordering = ["time_create", "name"]
