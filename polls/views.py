#djangoのショートカット
#return render(requestオブジェクト,テンプレート名('polls/index.html),(任意)辞書(context))
from django.shortcuts import render
#djangoの404エラー構文
from django.shortcuts import get_object_or_404


"""スタブメソッドなくなったため必要なし??
#スタブメソッドを使用するなら残す
#スタブ:下位モジュールの変わり、空の代用品用
from django.http import HttpResponse
"""
#ひとつの引数(リダイレクト先のURL)をとる。
#POSTデータが成功した後は常にHTTPResponseRedirectを返す必要がある。
##from django.contrib.sessions.backends.base import SessionBase
from django.http import HttpResponseRedirect,request#,HttpRequest
"""djangoのショートカットget_object_or_404がHttp404を楽にしてくれたため必要なし
#404エラー送出(httpのモジュール)
from django.http import Http404
"""


#ビュー関数中でURLのハードコードを妨げる事ができる。
#制御を渡したいビュー名とそのビューに与えるURLパターンの位置引数を与える。
from django.urls import reverse


#汎用ビューをしようするため
from django.views import generic


"""djangoのrenderを使用すれば必要なし?
#templateを読み込む
from django.template import loader
"""


from django.utils import timezone


#modelsパッケージ
from .models import Question,Choice


#urlsのpath()を通すことで以下の関数が使用できる。


#各汎用ビューは自分がどのモデルに対して動作するのか知っておく必要がある。
#(model属性を使用して提供される)

#ListViewは「オブジェクトのリストを表示する」

class IndexView(generic.ListView):
    
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        #日付を比較してチェック
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

        """
        #上から5つ
        return Question.objects.order_by('-pub_date')[:5]
        """
    def get_context_data(self, **kwargs):
        # セッションを追加する
        
        #self.request.session['username'] = self.request.user.username
        
        return super(IndexView, self).get_context_data(**kwargs)

#DetailViewは「あるタイプのオブジェクト詳細ページを表示する」
#DetailView汎用ビューには"pk"という名前でURLからプライマリキー(DBの登録番号のようなもの)
#キャプチャして渡すことになっているので、汎用ビュー向けにquestion_idをpkに変更している。
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        #未来の質問に到達させないために制約
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request,question_id):
    #question_idが存在しなければ、エラー表示(djangoのショートカット)(detailと一緒)
    question = get_object_or_404(Question,pk=question_id)

    try:
        #request.POSTはキーを指定すると送信したデータにアクセスできる。
        #今回は選択された選択肢のIDを文字列として返す。
        #POSTデータに(voteという投票(form)でPOSTデータが送信されたにもかかわらず)choiceが何も選択されなければexcept文
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't selected a choice.",
            #'aiueo':"aiueo",.html側で受け取らなくても送れる(受け取った方がよいが)
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))



#
##汎用ビューIndexViewの元関数
#def index(request):
#    #最新質問5つをlistにいれる
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    
#    '''responseじゃなくtemplate.renderをしようし、requestをできるように
#    #', 'でlatest_question_listの中身を繋げる
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)
#    '''
#
#    """djangoのrender使うため必要なくなった?
#    #templateにディレクトリtemplateのpolls/indexをいれる
#    template = loader.get_template('polls/index.html')
#    """
#
#    #contextに'latest_question_list'としてlatest_question_listをいれる(マッピング)
#    context = {'latest_question_list':latest_question_list,}
#    
#    """djangoのrender使うため必要なくなった?
#    #テンプレートの レンダリング (rendering) では、コンテキストから値を取り 
#    # 出して変数という「穴」に埋め、全てのブロックタグを実行します。
#    #templateのrenderメソッドをつかってrequest情報を全てでcontextを指定し送る
#    #template(indexに).render(記述する)(comtext(リスト),request(通信機能))
#    return HttpResponse(template.render(context,request))
#    """
#
#    #dhangoのrender関数(第一引数:request,第二:テンプレ名,第三:辞書)
#    return render(request,'polls/index.html',context
#
#
##汎用ビューDetailViewの元関数
#def detail(request,question_id):
#    #以下のtryを自動でしてくれる(djangoのショートカット)
#    question = get_object_or_404(Question,pk=question_id)
#
#    """djangoの404エラー構文を使うためtryとかは必要なくなった?
#    try:
#        #question_idをgetしてみる
#        question = Question.objects.get(pk=question_id)
#
#    #そのquestion_idが存在しなければ
#    except Question.DoesNotExist:
#        #エラー文を出力
#        raise Http404("Question does not exist")
#   
#    #except通らなければ、
#    """
#    #renderでquestionの中身をdetai.htmlに送る
#    return render(request,'polls/detail.html',{'question':question})
#    
#
#    """renderで値を送れるようになったため必要なくなった?
#    #空の代用品
#    return HttpResponse("you're question %s" % question_id)
#    
#
#
##汎用ビューResultsViewの元関数
#def results(request,question_id):
#    #question_idが存在しなければ、エラー表示(djangoのショートカット)(detailと一緒)
#    question = get_object_or_404(Question,pk=question_id)
#
#    return render(request,'polls/results.html',{'question':question})


