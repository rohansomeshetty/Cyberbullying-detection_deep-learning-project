

from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *

import matplotlib.pyplot as plt;
import numpy as np
import numpy
from django.shortcuts import render, redirect
from PIL import ImageTk, Image
from .Prediction import CNN



def homepage(request):
	return render(request, 'index.html')

def signuppage(request):
	if request.method=='POST':
		email=request.POST['mail']

		d=usertab.objects.filter(e_mail__exact=email).count()
		if d>0:
			return render(request, 'signup.html',{'msg':"email Already Registered"})
		else:
			
			pass_word=request.POST['pass_word']
			phone=request.POST['phone']
			n_a_m_e=request.POST['n_a_m_e']
			gen=request.POST['gen']
			picture=request.POST['picture']
		
			d=usertab(n_a_m_e=n_a_m_e,e_mail=email,pass_word=pass_word,phone=phone,gender=gen,picture=picture)
			d.save()

			return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})
	else:
		return render(request, 'signup.html')


	
def userloginaction(request):
	if request.method=='POST':
		uid=request.POST['mail']
		pass_word=request.POST['pass_word']
		d=usertab.objects.filter(e_mail__exact=uid).filter(pass_word__exact=pass_word).count()
		
		if d>0:
			d=usertab.objects.filter(e_mail__exact=uid)
			request.session['email']=uid
			request.session['n_a_m_e']=d[0].n_a_m_e
			fc=frequest.objects.filter(to_e_mail__exact=uid).filter(stz__exact='request').count()	
			if fc>0:
				fc=str(fc)+str(" new")
			else:
				fc=""

			return render(request, 'user_home.html',{'data': d[0],'fc':fc})

		else:
			return render(request, 'user.html',{'msg':"Login Fail"})

	else:
		return render(request, 'user.html')

def adminloginaction(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pwd = request.POST['pwd']

        if uid == 'admin' and pwd == 'admin':
            request.session['adminid'] = 'admin'
            return render(request, 'admin_home.html')

        else:
            return render(request, 'admin.html', {'msg': "Login Fail"})

    else:
        return render(request, 'admin.html')



def adminhomedef(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'admin_home.html')

    else:
        return render(request, 'admin.html')

def training(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'training.html')

    else:
        return render(request, 'admin.html')

def testing(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'testing.html')

    else:
        return render(request, 'admin.html')

def adminlogoutdef(request):
    try:
        del request.session['adminid']
    except:
        pass
    return render(request, 'admin.html')



def userlogoutaction(request):
	try:
		del request.session['email']
	except:
		pass
	return render(request, 'user.html')



def userhomepage(request):
	if "email" in request.session:
		email=request.session["email"]
		d=usertab.objects.filter(e_mail__exact=email)

		fc=requests.objects.filter(to_e_mail__exact=email).filter(stz__exact='request').count()	
		print('..........',fc)
		if fc>0:
			fc=str(fc)+str(" new")
		else:
			fc=""

		return render(request, 'user_home.html',{'data': d[0],'fc':fc})

	else:
		return redirect('n_userlogout')

		
def viewprofilepage(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=usertab.objects.filter(e_mail__exact=uid)
		return render(request, 'viewpprofile.html',{'data': d[0]})
	else:
		return render(request, 'user.html')


def fsearch(request):
	if "email" in request.session:
		uid=request.session["email"]
		femail=request.POST['e_mail']
		d=usertab.objects.filter(e_mail__exact=femail)

		if len(d)>0:
			
			return render(request, 'fsearch.html',{'data': d[0]})
		else:
			return render(request, 'msg.html',{'msg': "No Details Available"})


	else:
		return render(request, 'user.html')

def freqsend(request):
	if "email" in request.session:
		uid=request.session["email"]
		un_a_m_e=request.session["n_a_m_e"]
		femail=request.POST['e_mail']
		fn_a_m_e=request.POST['n_a_m_e']
		
		d=frequest.objects.filter(fe_mail__exact=uid).filter(to_e_mail__exact=femail).count()
		
		if d>0:

			d=usertab.objects.filter(e_mail__exact=uid)
			return render(request, 'user_home.html',{'data': d[0],'msg':'Already sent friend request'})

		else:
			d=frequest(fn_a_m_e=un_a_m_e,fe_mail=uid,to_e_mail=femail,stz='request')
			d.save()
					
			d=usertab.objects.filter(e_mail__exact=uid)
			return render(request, 'user_home.html',{'data': d[0],'msg':'Friend Request Sent Successfully'})

		
	else:
		return render(request, 'user.html')


def viewfreq(request):
	uid=request.session["email"]
	un_a_m_e=request.session["n_a_m_e"]
	if request.method=='POST':
		
		femail=request.POST['e_mail']
		fn_a_m_e=request.POST['n_a_m_e']
		
		d=friends.objects.filter(e_mail__exact=uid).filter(frnd_e__exact=femail).count()
		if d>0:
			return render(request, 'user_home.html',{'data': d[0],'msg':'Your Already Friends'})
		else:
			

			d=friends(e_mail=uid,frnd_e=femail,frnd_n=fn_a_m_e)
			d.save()
			d=friends(e_mail=femail,frnd_e=uid,frnd_n=un_a_m_e)
			d.save()
			
			frequest.objects.filter(to_e_mail = uid).filter(fe_mail = femail).update(stz = 'accepted')
			d=usertab.objects.filter(e_mail__exact=uid)
			return render(request, 'user_home.html',{'data': d[0],'msg':'Updated !!'})
	else:
		d=frequest.objects.filter(to_e_mail__exact=uid).filter(stz__exact="request")
		return render(request, 'viewfreq.html',{'data': d})

def reqreject(request):

	uid=request.session["email"]
	femail=request.POST['email']
	frequest.objects.filter(to_e_mail = uid).filter(femail = femail).update(stz = 'rejected')
	d=usertab.objects.filter(e_mail__exact=uid)
	return render(request, 'user_home.html',{'data': d[0],'msg':'Updated !!'})

def viewfrds(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=friends.objects.filter(e_mail__exact=uid)
		return render(request, 'viewfrds.html',{'data': d})
	else:
		return render(request, 'user.html')



def writepost(request):
	if request.method=='POST':
		import random
		
		msg=request.POST['msg']
		n_a_m_e=request.session["n_a_m_e"]
		email=request.session["email"]
		picture=request.POST['picture']

		rs=CNN.detecting(msg)
		print('..........', rs)
		if rs=='not_cyberbullying':
			d=posts(n_a_m_e=n_a_m_e,e_mail=email,msg=msg,picture=picture,stz='non',stz2='False')
			d.save()
		else:
			rs=rs
			d=posts(n_a_m_e=n_a_m_e,e_mail=email,msg=msg,picture=picture,stz=rs, stz2="True")
			d.save()

		return render(request, 'writepost.html',{'msg':"Post shared.."})
	
	else:
		return render(request, 'writepost.html')



def writepost2(request):
	if request.method=='POST':
		import random
		
		msg=request.POST['msg']
		n_a_m_e=request.session["n_a_m_e"]
		email=request.session["email"]
		picture='non'

		rs=CNN.detecting(msg)
		print('..........', rs)
		if rs=='not_cyberbullying':
			d=posts(n_a_m_e=n_a_m_e,e_mail=email,msg=msg,picture=picture,stz='non',stz2='False')
			d.save()
		else:
			rs=rs
			d=posts(n_a_m_e=n_a_m_e,e_mail=email,msg=msg,picture=picture,stz=rs, stz2="True")
			d.save()
		return render(request, 'writepost.html',{'msg':"Post shared.."})
	
	else:
		return render(request, 'writepost.html')



def ownwall(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=posts.objects.filter(e_mail__exact=uid).order_by('-id')

		r=[]
		pp=True
		for d1 in d:
			pp=True
			if d1.picture=='non':
				pp=False
			if True:
				ss=None
				if d1.stz2=='True':
					ss=True
					ss2=False
				else:
					ss=False
					ss2=True

				print('>>>>>>>>>>',bool(d1.stz2))
				r.append({'n':d1.n_a_m_e,'p':d1.picture,'m':d1.msg,'stz1':d1.stz,'stz2':ss,'stz3':ss2,'pstz':pp})
		
		return render(request, 'ownwall.html',{'data': r})


	else:
		return render(request, 'user.html')



def viewwall(request):
	if "email" in request.session:
		uid=request.session["email"]
		
		d=posts.objects.all().order_by('-id')

		r=[]
		pp=True
		for d1 in d:
			pp=True
			if d1.picture=='non':
				pp=False
			d3=friends.objects.filter(e_mail__exact=uid).filter(frnd_e__exact=d1.e_mail).count()
			if d3>0:
				ss=None
				if d1.stz2=='True':
					ss=True
					ss2=False
				else:
					ss=False
					ss2=True

				print('>>>>>>>>>>',bool(d1.stz2))
				r.append({'n':d1.n_a_m_e,'p':d1.picture,'m':d1.msg,'stz1':d1.stz,'stz2':ss,'stz3':ss2,'pstz':pp})
		
		return render(request, 'viewwall.html',{'data': r})

	else:
		return render(request, 'user.html')





def d1dtdef(request):
    
    from .DT import model
    model()

    return render(request, 'training.html', {'msg': "Decision Tree Classifier Training Completed Successfully"})
 

def d1lrdef(request):
    
    from .LR import model
    model()

    return render(request, 'training.html', {'msg': "Logistic Regression Classifier Training Completed Successfully"})
 


def d1nndef(request):
    
    from .NN import model
    model()

    return render(request, 'training.html', {'msg': "Neural Network Classifier Training Completed Successfully"})
 



def d1rfdef(request):
    
    from .RF import model
    model()

    return render(request, 'training.html', {'msg': "Random Forest Classifier Training Completed Successfully"})
 

def d1cnndef(request):
    
    from .CNN_train import model
    model()

    return render(request, 'training.html', {'msg': "CNN Classifier Training Completed Successfully"})
 




def d1testingdef(request):
    
    from .D1Testing import D1Testing
    D1Testing.main()

    return render(request, 'testing.html', {'msg': "Testing completed.."})
 


def results(request):
    if "adminid" in request.session:
        d = performance.objects.all()

        return render(request, 'viewaccuracy.html', {'data': d})

    else:
        return render(request, 'admin.html')




def viewgraph(request):
    if "adminid" in request.session:
        algorithms = ['LR','RF','DT', 'NN', 'CNN']
        plt.cla()
        plt.clf()

        row = performance.objects.all()
        rlist = []
        for r in row:
        	rlist.append(float(r.acc))
        plt.title('Accuracy Measure')
        
        height = rlist
        print(height,',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
        baars = algorithms
        y_pos = np.arange(len(baars))
        # plt.bar(baars, height, color=['green', 'orange', 'cyan'])
        plt.bar(baars, height, color=['green', 'orange', 'cyan','green', 'orange', 'cyan' ])
        # plt.plot( baars, height )
        plt.xlabel('')
        plt.ylabel('Algorithms ')
        from PIL import Image

        plt.savefig('g1.jpg')
        im = Image.open(r"g1.jpg")
        im.show()

        return redirect('results')


