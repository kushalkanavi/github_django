from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import gitHubAPI

import requests
import json
import urllib
from django.utils import timezone
import datetime
# from datetime import datetime

from django.db.models import Q
from django.contrib import messages

class index(View):
	def get(self, request, *args, **kwargs):
		return render(request,'apiapp/template1.html')

class addUser(View):
	def post(self, request, *args, **kwargs):

		if self.request.method == 'POST':
			user = self.request.POST.get('add_user')
		
		url="https://api.github.com/users/" + user
		r=requests.get(url)
		data=json.loads(r.content)


		gitHubAPI.objects.create(
			login 				= 	data['login'],
			user_id 			=	data['id'],
			node_id 			=	data['node_id'],
			avatar_url 			=	data['avatar_url'],
			gravatar_id 		=	data['gravatar_id'],
			url 				=	data['url'],
			html_url 			=	data['html_url'],
			followers_url 		=	data['followers_url'],
			following_url 		=	data['following_url'],
			gists_url 			=	data['gists_url'],
			starred_url 		=	data['starred_url'],
			subscriptions_url 	=	data['subscriptions_url'],
			organizations_url	=	data['organizations_url'],
			repos_url 			=	data['repos_url'],
			events_url 			=	data['events_url'],
			received_events_url	=	data['received_events_url'],
			user_type 			=	data['type'],
			site_admin 			=	data['site_admin'],
			name 				=	data['name'],
			company 			=	data['company'],
			blog 				=	data['blog'],
			location 			=	data['location'],
			email  				=	data['email'],
			hireable 			=	data['hireable'],
			bio 				=	data['bio'],
			public_repos 		=	data['public_repos'],
			public_gists 		=	data['public_gists'],
			followers 			=	data['followers'],
			following 			=	data['following'],
			created_at			=	data['created_at'],
			updated_at			=	data['updated_at'],
			added_on			=	timezone.now()
			)

		return render(request,'apiapp/template1.html',{'user':user,})

class searchUser(View):
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			srch  = request.POST.get('search')

			if srch:
				match = gitHubAPI.objects.filter(Q(login = srch) | Q(user_id__icontains = srch) | Q(email__icontains = srch) | Q(blog__icontains = srch) | Q(company__icontains = srch) | Q(location__icontains = srch) | Q(bio__icontains = srch))

				if match:
					return render(request,'apiapp/template1.html',{'srch':match})
				else:
					messages.error(request,'No Result Found.')

			else:
				return render(request,'apiapp/template1.html')

		return render(request,'apiapp/template1.html')
class adminReport(View):
	def get(self, request, *args, **kwargs):
		d = gitHubAPI.objects.filter(added_on__icontains=datetime.date.today()).count()

		month = datetime.datetime.today() -  datetime.timedelta(30)
		m = gitHubAPI.objects.filter(added_on__range=[datetime.datetime.today(), month]).count()

		year = datetime.datetime.today() -  datetime.timedelta(365)
		y = gitHubAPI.objects.filter(added_on__range=[datetime.datetime.today(), month]).count()

		data = {'day' : d,
				'month' : m,
				'year'	: y,

		}
		
		return render(request,'apiapp/adminreport.html',data)

