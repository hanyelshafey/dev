from django.urls import path,include
from .views import post_list ,post_details,new_post , edite_post

app_name='post'


urlpatterns = [
    path('', post_list ),
    path('post<int:post_id>/', post_details, name="onepost" ),
    path('new/', new_post, name="new" ),
    path('edite<int:post_id>/', edite_post, name="editepost" ),

    

]



