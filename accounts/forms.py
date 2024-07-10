from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import GENDER 
from django.contrib.auth.models import User
from .models import UserAccount

class UserRegistrationForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER)
    
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'gender'
        ]
      
        
    def save(self, commit=True):
        our_user = super().save(commit=False)
        
        if commit:
            our_user.save()
            gender = self.cleaned_data.get('gender')
            
            UserAccount.objects.create(
                user=our_user,
                gender=gender,
                account_id=1000 + our_user.id
            )
        
        return our_user
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })

class UserUpdateForm (forms.ModelForm)         :
    gender = forms.ChoiceField(choices=GENDER)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
            
            if self.instance:
                try:
                    user_account = self.instance.account
                except:
                    user_account = None
            
            if user_account:
                self.fields['gender'].initial = user_account.gender
   
   
                
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account, created = UserAccount.objects.get_or_create(user=user) 
            user_account.gender = self.cleaned_data['gender']
            user_account.save()
        return user
            
            
            
            