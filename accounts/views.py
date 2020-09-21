from django.shortcuts import render

#このクラスを継承するだけで、継承したクラスに遷移する場合はログインが必要になる。
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.sessions.backends.base import SessionBase
from django.http import HttpRequest
"""
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
"""
#ログイン後に元にいたページにリダイレクト処理

#ログインURLがGETメソッドで呼ばれた場合にはログイン用のフォームをテンプレートで
# 利用できるようにした状態でログインページのテンプレートを返す 
# ログインURLがPOSTメソッドで呼ばれた場合にはユーザーのログイン処理を実行
# ログイン「に成功すれば、nextというパラメータに指定されたパスのURLにリダイレクトする
# nextが指定されていない場合はsetting.pyファイルのsettings.LOGIM_REDIRECT_URLに指定してURLにリダイレクトする 
from django.contrib.auth.views import(
    LoginView,LogoutView,
)


from . forms import LoginForm

class Login(LoginView):
    #ログインページ
    form_class = LoginForm
    template_name = 'accounts/login.html'
    #next = みたいな感じでどこにリダイレクトするか指定できる
    #書かないのならば、プロジェクト直下のLOGIN_REDIRECT_URLに指定すべき
    

#ログインしているユーザでないとログアウトボタンを押せないようにするため
#(ログインしているユーザだけが制御できるようにするため)
# -> ログインしていないのにログアウトボタン押されるとバグになる
class Logout(LoginRequiredMixin,LogoutView):
    #ログインページ
    #template_nameでログアウト後に表示されるテンプレートファイルを指定
    template_name = 'accounts/login.html'


def index(request):
    #ログイン後に遷移するテスト用のTOPページを定義した関数
    #request.session['user_id'] = user_id
    request.session['username'] = request.user.username
    return render(request,'accounts/index.html')