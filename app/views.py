from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *

from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPagePly(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')

				group = Group.objects.get(name='Player')
				user.groups.add(group)

				messages.success(request, f" Player: {username} + has created Account")
				return redirect('login')
	context = {'form': form}
	return render(request,'registerp.html',context)
@unauthenticated_user
def registerPageDm(request):
    form = CreateUserForm()
    if request.method == "POST":
	    form = CreateUserForm(request.POST)
	    if form.is_valid():
			    user = form.save()
			    username = form.cleaned_data.get('username')

			    group = Group.objects.get(name='DM')
			    user.groups.add(group)

			    messages.success(request, "DM: " + username + " has created Account")
			    return redirect('login')
    context = {'form': form}
    return render(request,"registerdm.html", context)

def welcomeview(request):
    	return render(request,"welcome.html")

@unauthenticated_user
def loginPage(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
            	login(request, user)
            	return redirect('DMview')   
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def DMview(request):
    context = {}
    return render(request,"DMview.html", context)

def Pview(request):
    context = {}
    return render(request,"Pview.html", context)

@login_required(login_url='login')
def createmonsterview(request):
	form = CreateMonsterForm()
	context = {'form': form}
	if request.method == "POST":
		form = CreateMonsterForm(request.POST)
		if form.is_valid():
			monster = form.save()
			monster.creator = request.user
			monster.save()
			return redirect('DMview')
	return render(request,'create_monster.html',context)

@login_required(login_url='login')
def createcharacterview(request):
		form = CreateCharacterForm()
		context = {'form': form}
		if request.method == "POST":
			form = CreateCharacterForm(request.POST)
			if form.is_valid():
					character = form.save()
					character.creator = request.user
					character.save()
		return render(request, 'create_character.html', context)

@login_required(login_url='login')
def updateCharacter(request, pk):

	order = Character.objects.get(id=pk)
	form = CreateCharacterForm(instance=order)

	if request.method == 'POST':
		form = CreateCharacterForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'update_ch.html', context)

@login_required(login_url='login')
def deleteCharacter(request, pk):
	character = Character.objects.get(id=pk)
	if request.method == "POST":
		character.delete()
		return redirect('home')

	context = {'item':character}
	return render(request, 'delete_ch.html', context)

@login_required(login_url='login')
def updateMonster(request, pk):

	order = Monster.objects.get(id=pk)
	form = CreateMonsterForm(instance=order)

	if request.method == 'POST':
		form = CreateMonsterForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'update_m.html', context)

@login_required(login_url='login')
def deleteMonster(request, pk):
	monster = Monster.objects.get(id=pk)
	if request.method == "POST":
		monster.delete()
		return redirect('home')

	context = {'item':monster}
	return render(request, 'delete_m.html', context)
