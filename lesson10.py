# 関数
def hoge():
    print("hogehoge")
    print("fugafuga")

def hello(name):
    print("hello, {}".format(name))

def multival(val1, val2):
    print("val1:{0}, val2:{1}".format(val1, val2))

hoge()
hello("Kirk")
hello("Mr.Sulu")

multival("v1", "v2")
multival(val2="v2-2", val1="v1-1") # 引数で代入すると順不同