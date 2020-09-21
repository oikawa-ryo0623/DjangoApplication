# AuthenticationFormからこのコードは派生し、
# 明示的にユーザー名とパスワードのフィールドをオーバーライドして、
# プレースホルダーテキストを追加している。

#プレースホルダーテキストとは
#  入力フォームの内側に表示される借り入れのテキストのこと
#  ユーザが入力欄にカーソルを合わせると文字が消える仕様のものが多い
from django.contrib.auth.forms import(
    #このクラスを利用すると簡単にログオン用フォームを生成できる
    AuthenticationForm
)

#ログオン用のフォームクラスを定義
class LoginForm(AuthenticationForm):
    #ログオンフォームの定義
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for fields in self.fields.values():
            #全てのフォームの部品のクラス属性に[form-comtrol]を指定(bootstrapのフォームを利用するため)
            fields.widget.attrs['class'] = 'form-control'
            #全てのフォームの部品に[placeholder]を定義して、入力フォームにフォーム名が表示されるように指定
            fields.widget.attrs['placeholder'] = fields.label

        
#全フォームはAuthenticationFormクラス内で定義されているfields
#ウィジェット(widget)はHTMLの入力エレメントを表現するためにオブジェクト
#field.widget.attrs[属性] = <設定値>という形でフォームのデザインを定義できる
