from django.urls import path,include

from . import views

#app_nameをつけることで、Djangoのプロジェクト間のURLを区別できる
#
app_name = 'polls'

#polls.urlsモジュールと結びつけることが出来る。
#第一引数はpath接続するため
urlpatterns = [
    #path('',views.index,name = 'index'),#通常
    path('',views.IndexView.as_view(),name='index'),#generic viewの書き方
    #path('<int:question_id>/',views.detail,name = 'detail'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),#generic viewの書き方
    #path('<int:question_id>/result/',views.results,name = 'results'),
    path('<int:pk>/results',views.ResultsView.as_view(),name='results'),#generic viewの書き方
    path('<int:question_id>/vote/',views.vote,name = 'vote'),

]