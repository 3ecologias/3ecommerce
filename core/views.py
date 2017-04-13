# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .models import *
from .forms import ContactUs

import urllib
import urllib2
import json
from django.conf import settings

class Index(FormView):
	template_name = "core/index.html"
	form_class = ContactUs
	success_url = '/'

	def get_context_data(self, **kwargs):

		context = super(Index, self).get_context_data(**kwargs)

		return context

	def form_valid(self, form):
		''' Begin reCAPTCHA validation '''
		recaptcha_response = self.request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
        }
		data = urllib.urlencode(values)
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		result = json.load(response)
		''' End reCAPTCHA validation '''
		if result['success']:
			form.send_email()
			messages.success(self.request, 'Seu contato foi enviado com sucesso!')
		else:
			messages.error(self.request, 'reCAPTCHA inválida. Por favor, tente novamente.')
			return HttpResponseRedirect(super(Index, self).get_success_url())

		return super(Index, self).form_valid(form)
