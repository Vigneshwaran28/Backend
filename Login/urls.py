from django.urls import path
from .views import UserDetails, UserList, LoginView, LoginAuth, homeIndex, HeroView, HeroEditView, AddHeroList, LogoutView, CandidateView, CandidateListView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('herolist/', HeroView.as_view(), name='hero-list'), #show the hero list
    path('login/', LoginView.as_view(), name='login'), #login url
    path('userslist/', UserList.as_view(), name='user-list'),  #show the user details also add the user with post method
    path('user/<int:pk>/', UserDetails.as_view(), name='user-detail'),   #show the user details with their id
    path ('heroedit/<int:pk>',HeroEditView.as_view(),name='hero-edit'),  #edi the hero
    path ('addhero/',AddHeroList.as_view(),name='hero-edit'),  #adding a new hero
    path('auth/', LoginAuth.as_view(), name='login-auth'), #login authentication
    path ('logout/',LogoutView.as_view(), name='logout'),
    path ('candidateView/<int:pk>',CandidateView.as_view(), name='candidateView'),
    path('candidates/', CandidateListView.as_view(), name='candidate-list'),
    path('', homeIndex, name='home'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
