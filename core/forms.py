# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage


class ContactUs(forms.Form):

    name = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nome *', 'id': 'name', 'class': 'form-control', 'type': 'text'}))

    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email *', 'id': 'email', 'class': 'form-control'}))

    phone = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Telefone', 'id': 'phone', 'class': 'form-control', 'type': 'tel'}))

    itens = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Itens no Catálogo', 'id': 'itens', 'class': 'form-control slider', 'type': 'text'}))

    marketing = forms.CharField(required=False,
        widget=forms.CheckboxInput(attrs={'placeholder': '', 'id': 'marketing', 'class': 'form-control', 'type': 'checkbox'}))

    chat = forms.CharField(required=False,
        widget=forms.CheckboxInput(attrs={'placeholder': '', 'id': 'chat', 'class': 'form-control', 'type': 'checkbox'}))

    visual = forms.CharField(required=False,
        widget=forms.CheckboxInput(attrs={'placeholder': '', 'id': 'visual', 'class': 'form-control', 'type': 'checkbox'}))

    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Observações *', 'id': 'message', 'class': 'form-control', 'rows': '3'})
    )

    def send_email(self):
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        itens = self.cleaned_data['itens']
        marketing = self.cleaned_data['marketing']
        chat = self.cleaned_data['chat']
        visual = self.cleaned_data['visual']
        message = self.cleaned_data['message']
        subject = '[3ECOMMERCE - Novo Contato]'

        try:
            email = EmailMessage(subject+" de "+name+" tel: "+phone+" Prod: "+itens+" M:"+marketing+" C:"+chat+" ID:"+visual, message, from_email,['admin@3ecologias.net'])
            email.content_subtype = "html"
            email.send()
        except BadHeaderError:
            raise ValidationError("Cabeçalho inválido")
