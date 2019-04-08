def lcs(x,y):
    x_len=len(x)
    y_len=len(y)
    web=[[0 for i in range(x_len+1)] for i in range(y_len+1)]
    out_str=''
    r_local=[]
    c_local=[]
    for i in range(1,y_len+1):
        for j in range(1,x_len+1):
            if y[i-1]==x[j-1]:
                web[i][j]=web[i-1][j-1]+1 
            else:
                web[i][j]=max(web[i-1][j],web[i][j-1])
    return web

def print_lcs(web,x,y,x_len,y_len):
    s=''
    while (x_len>=0 and y_len>=0):
        if x[x_len]==y[y_len]:
            s=s+x[x_len]
            x_len=x_len-1
            y_len=y_len-1
        else:
            if web[y_len][x_len+1]>=web[y_len+1][x_len]:
                y_len=y_len-1
            else:
                x_len=x_len-1
    return s[::-1]