from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from django.contrib import messages
from django.template import RequestContext

from index_app.views import send_message
from rooms_app.models import Room
from rooms_app.forms import BookRoomForm


def bookRoomTwin(request):
    object_name = Room.objects.get(id=1)
    form = BookRoomForm
    
    if request.user.is_authenticated:
        form = BookRoomForm(initial={
        'name': request.user.first_name,
        'surname': request.user.last_name,
        'email': request.user.email,
        })
        
    context = {"twin": object_name, "form": form}
    return render(request, "room_twin.html", context=context)


def bookRoomPrestige(request):
    object_name = Room.objects.get(id=2)
    form = BookRoomForm
    
    if request.user.is_authenticated:
        form = BookRoomForm(initial={
        'name': request.user.first_name,
        'surname': request.user.last_name,
        'email': request.user.email,
        })
    
    context = {"prestige": object_name, "form": form}
    return render(
        request, template_name="room_prestige.html", context=context
    )


def bookRoomDeluxe(request):
    object_name = Room.objects.get(id=3)
    form = BookRoomForm

    if request.user.is_authenticated:
        form = BookRoomForm(initial={
        'name': request.user.first_name,
        'surname': request.user.last_name,
        'email': request.user.email,
        })
    
    context = {"deluxe": object_name, "form": form}
    return render(request, template_name="room_deluxe.html", context=context)


def bookRoomFamily(request):
    object_name = Room.objects.get(id=4)
    form = BookRoomForm

    if request.user.is_authenticated:
        form = BookRoomForm(initial={
        'name': request.user.first_name,
        'surname': request.user.last_name,
        'email': request.user.email,
        })
    
    context = {"family": object_name, "form": form}
    return render(request, template_name="room_family.html", context=context)


def bookRoomTriple(request):
    object_name = Room.objects.get(id=5)
    form = BookRoomForm

    if request.user.is_authenticated: 
        form = BookRoomForm(initial={
        'name': request.user.first_name,
        'surname': request.user.last_name,
        'email': request.user.email,
        })
    
    context = {"triple": object_name, "form": form}
    return render(request, template_name="room_triple.html", context=context)


def bookRoomQuadr(request):
    object_name = Room.objects.get(id=6)
    form = BookRoomForm

    if request.user.is_authenticated:
        form = BookRoomForm(initial={
        'name': request.user.first_name,
        'surname': request.user.last_name,
        'email': request.user.email,
        })
    
    context = {"quadruple": object_name, "form": form}
    return render(request, template_name="room_quadruple.html", context=context)


def bookRoom(request):
    form = BookRoomForm
    
    if request.method == "POST":
        form = BookRoomForm(request.POST)
        if form.is_valid():
            form.save()
    
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            telephone_number = form.cleaned_data['telephone_number']
            book_room = form.cleaned_data['book_room']
            commentary = form.cleaned_data.get['commentary']
            date_in = form.cleaned_data['date_in']
            date_out = form.cleaned_data['date_out']
            
            send = {
                "name": name,
                "surname": surname,
                "email": email,
                "telephone_number": telephone_number,
                "book_room": book_room,
                "commentary": commentary,
                "date_in": date_in,
                "date_out": date_out
            }
            print(send)

            html_body = render_to_string("send_mail.html", send)
            send_message(html_body, "Забронированный номер")
            messages.success(request, 'Номер успешно забронирован.')
            return redirect("home")
    
    return render('home.html', {}, context_instance=RequestContext(request)) 
