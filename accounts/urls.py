from django.urls import path
from .import views
urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/',views.UserLogin.as_view(),name='login' ),
    path('Logout/',views.UserLogout.as_view(),name='logout' ),
    path('profile/',views.UserProfile,name='profile' ),
    path("borrow/<int:id>", views.borrow, name="borrow_book"),
]