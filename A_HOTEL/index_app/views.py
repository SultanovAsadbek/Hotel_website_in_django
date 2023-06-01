from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from index_app.forms import FeedbackForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def send_message(html_body, theme):
    msg = EmailMultiAlternatives(subject=theme, to=['sultanovvasadbek0101@gmail.com'])
    msg.attach_alternative(html_body, "text/html")
    msg.send()


def feedback(request):
    form = FeedbackForm
    
    if request.user.is_authenticated:
        form = FeedbackForm(initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        })
        
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            commentary = form.cleaned_data["commentary"]
        
        send = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
            "commentary": commentary
        }
        
        html_body = render_to_string("appoitment_model.html", send)
        send_message(html_body, "Обратная Связь")
        messages.success(request, "С вами скоро свяжемся.")
        return redirect('home', permanent=True)
    context = {'form': form}
    
    return render(request, 'feedback.html', context)
