while 1:
    s=input()
    trans_dict={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
               'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
                'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,
                'V':22,'W':23,'X':24,'Y':25,'Z':26}
    trans_dict_t={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',
               9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',
                16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',
                22:'V',23:'W',24:'X',25:'Y',26:'Z'}
    if s!='':
        nums=int(s)
        for i in range(0,nums):
            s1=input()
            test=''
            for i in s1:
                if i.isalpha():
                    test+=i
                else:
                    break
            if len(test)>1:
                cloumns=0
                trans_num=0
                for i in test[::-1]:
                    cloumns+=trans_dict[i]*(26**(trans_num))
                    trans_num+=1
                print('R'+s1[len(test):]+'C'+str(cloumns))
            else:
                if test=='R' and ('C' in s1):
                    rows=s1[1:].split('C')[0]
                    columns=int(s1[1:].split('C')[1])
                    columns_str=''
                    if columns<=26:
                        columns_str+=trans_dict_t[columns]
                    else:
                        while columns>26:
                            mod=columns%26
                            if mod!=0:
                                columns_str+=trans_dict_t[mod]
                            columns=columns//26
                        columns_str+=trans_dict_t[columns]
                    print(columns_str[::-1]+rows)
                else:
                    print('R'+s1[1:]+'C'+str(trans_dict[s1[1]]))
    else:
        break