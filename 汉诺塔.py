#搞清楚流程
#深拷贝与浅拷贝
#分功能去编程
#多种功能，使函数从初始化功能后开始迭代,设置多个函数
#单个元素的列表，[1:]有pop（0）的功能
#变量的主体和对象
def move(n,a,b,c):
    pass

a=[]
b=[]
c=[]
list=[a,b,c]
n=int(input('请输入你要玩的汉诺塔的层数:'))

def rode():
    x, y = int(input('起始点'))-1, int(input('结束点'))-1
    move(x, y)

def floor(n):
    for i in range(n):
        a.append(i)

def move(x,y):
    A=list[x]
    B=list[y]
    global n
    print(list)
    print('移动后')
    try:
        B[0]
        if A[0]<B[0]:
            B.insert(0,A[0])
            list[x]=A[1:]
            print(list)
            if len(list[2]) == n:
                print('你获胜了!')
            else:
                return rode()
        else:
            print('错误的移动！请重新移动：')
            print(list)
            return rode()
    except IndexError or SyntaxError:
        B.append(A[0])
        list[x]= A[1:]
        print(list)
        if len(list[2]) == n:
            print('你获胜了!')
        else:
            return rode()

def game():
    #n=int(input('请输入你要玩的汉诺塔的层数:'))
    '''a = []
    b = []
    c = []
    list=[a,b,c]'''
    for i in range(n):
        list[0].append(i)
    rode()

game()


