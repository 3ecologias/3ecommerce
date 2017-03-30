from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .models import *
from .forms import ContactUs

class Index(FormView):
	template_name = "core/index.html"
	form_class = ContactUs
	success_url = '/'

	def get_context_data(self, **kwargs):

		context = super(Index, self).get_context_data(**kwargs)

		return context

	def form_valid(self, form):
		form.send_email()

		return super(Index, self).form_valid(form)
