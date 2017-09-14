#１行コメントは#
'''
複数行コメントは
わかりにくいと思われるので使わない方向で
'''
#pylintのオプションはコメントで記述できるっぽい
# pylint: disable=invalid-name

#へろー
##後ろに ;　とか要らない
print("Hello world")


##変数に代入
###宣言不要で、型もなし

num = 1 #数値
print(num)


##掛け算とか、とくに変な記述はない様子
print(num*3)
###その他の演算子はhttps://docs.python.jp/3/reference/lexical_analysis.html#operators

##文字列
str1 = "文字列"
print(str1+"連結")
print(str1[0])  #インデックスは0起算
print(str1[-1]) #マイナスで右から


#制御構造
a = 0
while a < 20:  #行末にコロン必要
    print(a)    #必ず字下げ！
    if a%15 == 0:
        print("FizzBuzz")
    elif a%3 == 0:    #独特な elif  ( else if の意)
        print("Fizz")
    elif a%5 == 0:
        print("Buzz")

    a = a+1       #インクリメント演算子は無いっぽい

for a in ["A",1,2,3,4,5]: #forEachっぽい
    print(a)

for a in range(0,10,1): # for(i=0;i<10;l++)的な
    print(a)

#関数
def hello(arg="world"):
    """関数やクラスの最初にこんな感じでコメントを書くとdocstringという扱いになって、
    リファレンス作成時や、コード補完などの際に使用されます。後々便利なので書きましょう。
    http://www.sphinx-doc.org/ja/stable/domains.html#info-field-lists
    """

    greet="Hello " + arg
    print(greet)
    return greet

hello()
result=hello("oreore")
print("result:" + result)
#   print(greet)    #関数内スコープ変数なのでエラーになります

#クラス
## クラス定義
class TheClass:
    """クラスサンプル """

    member=1    #なにもつけなければpublicメンバ
    __num=1     #アンダースコア２個でprivate

    def __init__(self):
        '''コンストラクタ'''
        self._num=2
        self.__num=3


    def method1(self):  #メソッドの第一引数はselfにしとけ
        print("TheClass method" + str(self.member))

    def method2(self):
        print("The Class private num=" + str(self.__num))

## クラスインスタンス化 newとか要らない
tclass = TheClass()
tclass.method1()    #メソッド呼び出し
tclass.member=2     #publicメンバー上書き
tclass.method1()

tclass.method2()
tclass.__num=4      #privateメンバー上書き。エラーにはならないみたい
tclass.method2()    #エラーにはならないけど上書きはされない

## 継承
class ExtClass(TheClass):   #こう書くらしい
    def method2(self):
        #self.__num プライベートメンバにはアクセスできない
        print("this is overwrote method")

exclass=ExtClass()
exclass.method1()
exclass.method2()
