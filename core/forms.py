# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context


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
        widget=forms.CheckboxInput(attrs={'placeholder': '', 'id': 'marketing', 'class': 'form-control switch-wrapper', 'type': 'checkbox'}))

    chat = forms.CharField(required=False,
        widget=forms.CheckboxInput(attrs={'placeholder': '', 'id': 'chat', 'class': 'form-control switch-wrapper', 'type': 'checkbox'}))

    visual = forms.CharField(required=False,
        widget=forms.CheckboxInput(attrs={'placeholder': '', 'id': 'visual', 'class': 'form-control switch-wrapper', 'type': 'checkbox'}))

    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Observações', 'id': 'message', 'class': 'form-control', 'rows': '3'})
    )

    def send_email(self):
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        itens = self.cleaned_data['itens']
        marketing = 'Sim' if self.cleaned_data['marketing']=='True' else 'Não'
        chat = 'Sim' if self.cleaned_data['chat']=='True' else 'Não'
        visual = 'Sim' if self.cleaned_data['visual']=='True' else 'Não'
        message = self.cleaned_data['message']
        subject = '[3ECOMMERCE - Novo Contato]'

        template = get_template('core/email_template.html')

        context_email = {
            'name': name,
            'from_email': from_email,
            'phone': phone,
            'itens': itens,
            'marketing': marketing,
            'chat': chat,
            'visual': visual,
            'message': message,
        }

        content = template.render(context_email)

        try:
            email = EmailMessage(subject+" de "+name+" tel: "+phone, content, from_email,['admin@3ecologias.net'])
            email.content_subtype = "html"
            email.send()
        except BadHeaderError:
            raise ValidationError("Cabeçalho inválido")
