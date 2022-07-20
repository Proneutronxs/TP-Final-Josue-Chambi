
from django.urls import path
from WebApp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.defInicio, name="inicio"),

    path('about', views.defNosotros, name="about"),

    path('products', views.defProducts, name="products"),

    path('contact', views.defContact, name="contact"),

    path('singup', views.register, name="singup"),

    path('login', views.login_request, name="login"),

    path('logout', LogoutView.as_view(template_name='WebApp/index.html'), name='logout'),

    path('search', views.defSearch, name="search"),

    ## Páginas de usuario

    path('user', views.defUser, name="user"),

    path('new', views.defNew, name="new"),

    path('editprofile', views.editarPerfil, name='editprofile'),    

    path('options', views.ListarProductos.as_view(), name="options"),

    path(r'^(?P<pk>\d+)$', views.DetalleProductos.as_view(), name='detail'),

    path(r'^update/(?P<pk>\d+)$', views.ProductoUpdate.as_view(), name='update'),

    path(r'^delete/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name='delete'),

    #path('delete', views.defDelete, name="delete"),

    #path('update', views.defUpdate, name="update"),

]
