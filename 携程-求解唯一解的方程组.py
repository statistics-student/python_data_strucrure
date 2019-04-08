while True:
    try:
        X_=eval(input())
        Y_=eval(input())
        def solve_fx(x,y):
            #正求解
            r_len=len(x)
            c_len=len(x[0])
            i,j=0,0
            while True:
                if x[i][j]==0:
                    for k in range(1,len(x)):
                        if x[k][j]!=0:
                            x[i],x[k]=x[k],x[i]
                            y[i],y[k]=y[k],y[j]
                c_num_1=x[i][j]
                for p in range(i+1,r_len):
                    c_num_2=(-x[p][j])
                    y[p]=y[p]+y[i]*(c_num_2)/c_num_1
                    for q in range(j,c_len):
                        x[p][q]=x[p][q]+x[i][q]*c_num_2/c_num_1
                i+=1
                j+=1
                if j==c_len-1:
                    break
            #逆求解
            remain_x=[]
            remain_y=[]
            for k in range(r_len):
                if x[k].count(0)!=c_len:
                    remain_x.append(x[k])
                    remain_y.append(y[k])
            x=remain_x[:c_len]
            y=remain_y[:c_len]
            i,j=len(x)-1,c_len-1
            while True:
                c_num_1=x[i][j]
                for p in range(i-1,-1,-1):
                    c_num_2=-x[p][j]
                    x[p][j]=0
                    y[p]=y[p]+y[i]*c_num_2/c_num_1
                i-=1
                j-=1
                if i==0:
                    break
            out_list=[y[i]/x[i][i] for i in range(len(x))]
            return [i if len(str(i)[2:])<=5 else round(i,5) for i in out_list]
        print(solve_fx(X_,Y_))
    except:
        break