from django.db import models


## This model stores user's registration data, and it will used for many oprtaions such as user login, view profile, etc. 
class usertab(models.Model):
	n_a_m_e=models.CharField(max_length=149);
	e_mail=models.CharField(max_length=149);
	pass_word=models.CharField(max_length=149);
	phone=models.CharField(max_length=149);
	gender=models.CharField(max_length=149);
	picture=models.CharField(max_length=149);

## This model stores user's frieds request data such as name and email of the sender, recipient email and status of the friend requests.
class frequest(models.Model):
	fn_a_m_e=models.CharField(max_length=149);
	fe_mail=models.CharField(max_length=149);
	to_e_mail=models.CharField(max_length=149);
	stz=models.CharField(max_length=149);

## This model stores frieds data of a user friend with such as email of the user and his/her friend name and email.
class friends(models.Model):
	e_mail=models.CharField(max_length=149);
	frnd_e=models.CharField(max_length=149);
	frnd_n=models.CharField(max_length=149);


## This model stores user's posts data such as name and email of the post owner, message of the post, etc.
class posts(models.Model):
	n_a_m_e=models.CharField(max_length=149);
	e_mail=models.CharField(max_length=149);
	msg=models.CharField(max_length=149);
	picture=models.CharField(max_length=149);
	stz=models.CharField(max_length=149);
	stz2=models.CharField(max_length=149);



class performance(models.Model):
	algo=models.CharField(max_length=30);
	acc=models.CharField(max_length=30);
	
