'''
华为编程：数字出现在字符串前面表示重复的次数
example：
abc3(A)
AAAcba
'''
while True:
    try:
        a=input()
        out_s=''
        zhan_=[]
        big_=0
        mid_=0
        small_=0
        for i in range(len(a)):
            if a[i].isalpha():
                if big_ == 0 and mid_ == 0 and small_ == 0:
                    out_s=out_s+a[i]
                else:
                    zhan_.append(a[i])
            if a[i].isnumeric():
                zhan_.append(a[i])
            if a[i]=='{':
                zhan_.append(a[i])
                big_+=1
            if a[i]=='[':
                zhan_.append(a[i])
                mid_+=1
            if a[i]=='(':
                zhan_.append(a[i])
                small_+=1
            if a[i]==')':
                if mid_==0:
                    str_temp=''
                    while len(zhan_)>0:
                        pop_=zhan_.pop()
                        if pop_.isalpha():
                            str_temp+=pop_
                        if pop_.isnumeric():
                            str_temp=int(pop_)*str_temp[::-1]
                        if pop_=='(':
                            small_-=1
                    out_s+=str_temp
                else:
                    zhan_.append(a[i])
            if a[i]==']':
                if big_==0:
                    str_temp=''
                    while len(zhan_)>0:
                        pop_=zhan_.pop()
                        if pop_.isalpha():
                            str_temp+=pop_
                        if pop_.isnumeric():
                            str_temp=int(pop_)*str_temp[::-1]
                        if pop_=='(':
                            small_-=1
                        if pop_==')':
                            pass
                        if pop_=='[':
                            mid_-=1
                    out_s += str_temp
                else:
                    zhan_.append(a[i])
            if a[i]=='}':
                str_temp = ''
                while len(zhan_) > 0:
                    pop_ = zhan_.pop()
                    if pop_.isalpha():
                        str_temp += pop_
                    if pop_.isnumeric():
                        str_temp= int(pop_) * str_temp[::-1]
                    if pop_ == '(':
                        small_ -= 1
                    if pop_ == ')':
                        pass
                    if pop_ == '[':
                        mid_ -= 1
                    if pop_ == ']':
                        pass
                    if pop_ =='{':
                        big_-=1
                out_s += str_temp
        out_s_T=''
        for i in sorted(out_s):
            out_s_T+=i
        out_s_T=out_s_T[::-1]
        for i in range(len(out_s_T)):
            if out_s_T[i].isupper():
                out_s_T=out_s_T[i:]+out_s_T[:i]
                break
        print(out_s_T)
    except:
        break



