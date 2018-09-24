from django.db import models
from django.utils import timezone
# from datetime import datetime

from datetime import date

class gitHubAPI(models.Model):
	login 					= 	models.CharField( max_length= 120,null=True)
	user_id 				=	models.IntegerField(null=True)
	node_id 				=	models.CharField( max_length= 120,null=True)
	avatar_url 				=	models.URLField(max_length=512, null=True)
	gravatar_id 			=	models.CharField( max_length= 120,null=True)
	url 					=	models.URLField(max_length=512, null=True)
	html_url 				=	models.URLField(max_length=512, null=True)
	followers_url 			=	models.URLField(max_length=512, null=True)
	following_url 			=	models.URLField(max_length=512, null=True)
	gists_url 				=	models.URLField(max_length=512, null=True)
	starred_url 			=	models.URLField(max_length=512, null=True)
	subscriptions_url 		=	models.URLField(max_length=512, null=True)
	organizations_url		=	models.URLField(max_length=512, null=True)
	repos_url 				=	models.URLField(max_length=512, null=True)
	events_url 				=	models.URLField(max_length=512, null=True)
	received_events_url		=	models.URLField(max_length=512, null=True)
	user_type 				=	models.CharField( max_length= 120, null=True)
	site_admin 				=	models.NullBooleanField()
	name 					=	models.CharField( max_length= 120, null=True)
	company 				=	models.CharField( max_length= 120, null=True)
	blog 					=	models.CharField( max_length= 120, null=True)
	location 				=	models.CharField( max_length= 120, null=True)
	email  					=	models.EmailField(max_length=254, null=True)
	hireable 				=	models.CharField( max_length= 120, null=True)
	bio 					=	models.CharField( max_length= 120, null=True)
	public_repos 			=	models.IntegerField(null=True)
	public_gists 			=	models.IntegerField(null=True)
	followers 				=	models.IntegerField(null=True)
	following 				=	models.IntegerField(null=True)
	created_at				=	models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	updated_at				=	models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	added_on				=	models.DateTimeField(auto_now=False, auto_now_add=False, null=True)


	def __str__(self):
		return self.login