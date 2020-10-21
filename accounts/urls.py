from django.urls import path,include
from .views import signup , profile




app_name='accounts'


urlpatterns = [

    
   path('signup/', signup, name="new_user" ),
    path('profile/', profile, name="profile" ),


    

]



