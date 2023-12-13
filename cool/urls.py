from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView

app_name='cool'
urlpatterns = [
    path('',views.loginPage,name='login'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    path('tache/<int:id>',views.tache_update,name='tache_update'),
    path('tache/create',views.tache_create,name='tache_create'),
    path('tache/<int:id>/delete',views.tache_delete,name='tache_delete'),
    path('logout/',views.Logout,name='logout'),
    path('profil',views.profil,name='profil'),
    path('profil/change',views.profil_change,name='profil_change'),
    path('compte/delete',views.UserDeleteView.as_view(),name='delete'),
    path('horaire/',views.horaire,name='horaire'),
]