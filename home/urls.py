from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name='login'),
    path("about", views.about, name='about'),
    path("profile", views.profile, name='profile'),
    path("contact", views.contact, name='contact'),
    path("signup", views.singup, name="signup"),
    path('login', views.login, name="login"),
    path('index', views.index, name='index'),
    path('c_forum', views.c_forum, name='c_forum'),
    path('forum', views.forum_index, name='forum_index'),
    path('post_detail/<int:id>', views.post_detail),
    path('post_detail/post_detail/d/<int:id>', views.del_post),
    #testing forums
    path('planner', views.planner, name='planner'),
    path('forum_t', views.d_forum, name='d_forum'),
    path('book/<int:id>', views.book, name='book'),
    path('cal/<int:id>', views.cal, name='cal'),
    path('plan', views.plan, name='plan'),
    path('c_plan', views.c_plan, name='c_plan'),
    path('cal/d/<int:id>', views.del_plan),
    path('tem', views.tem, name = 'tem'),
    path('test', views.test, name='test'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('<int:id>', views.del_alert),
    path('act/<int:id>', views.setact),
    path('inact/<int:id>', views.setinact),
]