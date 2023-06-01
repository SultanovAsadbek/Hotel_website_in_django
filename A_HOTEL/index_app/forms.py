from django import forms

 
class FeedbackForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Имя"}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Фамилия"})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Почта"}))
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Телефон номер"})
    )
    commentary = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Сообщение...",
                "cols": 30,
                "rows": 6,
                "tag": "textarea",
            }
        )
    )

    class Meta:
        fields = ["first_name", "last_name", "email", "phone_number", "commentary"]
