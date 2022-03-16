


from django.urls import path
from . import views

urlpatterns = [

    path('',views.demo, name='demo'),
    # path('opr/',views.operation, name='opr')
    # path('about/',views.page1,name='page1'),
    # path('contact/',views.page2,name='page2'),
    # path('detail/',views.details,name='details'),
    # path('thanks/',views.thanks,name='thanks')



]
