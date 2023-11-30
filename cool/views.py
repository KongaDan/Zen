from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.urls import reverse_lazy

@login_required
def home(request):
    cours=Cours.objects.filter(promotion=request.user.promotion,section=request.user.section)
    taches=Tache.objects.filter(etudiant=request.user.id)
    return render(request,'home.html',{'cours':cours,'taches':taches})

@login_required
def Logout(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

@login_required
def profil(request):
    return render(request,'profil.html')

@login_required
def profil_change(request):
    message="Eureka"
    form=UserCreationChangeForm(instance=request.user)
    if request.method=="POST":
        form=UserCreationChangeForm(request.POST,instance=request.user)
        try:
            if form.is_valid():
                form.save()
                return redirect('profil')
        except ValueError:
            message="Desole une erreur s'est produite"
    return render(request,'profil_change.html',{'form':form,'message':message})
@login_required
def tache_update(request,id):
    tache=Tache.objects.get(id=id)
    form=TacheForm(instance=tache)
    return render(request,'tache.html',{'form':form})

@login_required
def tache_delete(request,id):
    tache=Tache.objects.get(id=id)
    if request.method=="POST":
        tache.delete()
        return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request,'tache_delete.html',{'tache':tache})

@login_required
def tache_create(request):
    tache=TacheForm()
    message=""
    if request.method=="POST":
        tache=TacheForm(request.POST)
        try:
            if tache.is_valid():
                tache.save(commit=False)
                tache.etudiant=request.user.id
                tache.save()
                return redirect(settings.LOGIN_REDIRECT_URL)
        except:
            message="une tache comprend un nom et une description"
    return render(request,'tache_create.html',{'form':tache,'message':message})

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'user_delete.html'
    form_class=UserDeleteform
    def get_object(self, queryset=None):
        return User.objects.get(username=self.request.user.username)
    def delete(self, request, *args, **kwargs):
        logout(request)
        return super().delete(request, *args, **kwargs)
user_delete = login_required(UserDeleteView.as_view())


def loginPage(request):
    if request.method=='POST':
        name=request.POST['username']
        pword=request.POST['password']
        print(pword)
        print(name)
        user=authenticate(request,username=name,password=pword)
        if user is not  None:
            login(request,user )
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            message='l\'email ou le mot de passe est incorrecte '
            return render(request,'login.html',{'message':message})
    return render(request,'login.html')

def signup(request):
    form1 = CustomUserForm(request.POST or None)
    message = ''
    if request.method == "POST":
        if form1.is_valid():
            user = form1.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'signup.html', {'form1': form1, 'message': message})

