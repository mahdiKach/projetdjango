
from.import views
from django.urls import path
urlpatterns = [
   path('',views.home),
   path('produits/',views.index,name="produits"),
   path('chariot/', views.chariot, name="chariot"),
   path('checkout/', views.checkout, name="checkout"),
   path('majproduits/', views.majProd, name="majprod"),
   path('details/<int:pk>/', views.produitdetail, name="details"),
   path('dashboard/',views.Dashboard,name="dashboard"),
   path('login/', views.loginn, name="login"),
   path('register/', views.register, name="register"),
   path('logout/', views.logoutUser, name="logout"),

]