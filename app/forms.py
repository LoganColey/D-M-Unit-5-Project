from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Character
from django.contrib.auth.models import User
from app.models import  *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateMonsterForm(ModelForm):
    class Meta:
        model = Monster
        fields ='__all__'

class CreateCharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = '__all__'

class CreateStatsForm(ModelForm):
    class Meta:
        model = Stats
        fields = '__all__'

class CreateCampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'

class CreateNoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'

class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'