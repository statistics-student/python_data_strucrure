class Graph:
    '''
    创建一个图的类
    '''
    '''
    mat邻接矩阵，vnum顶点的个数，unconn无关联时提供的值
    '''
    def __init__(self,mat,unconn=0):
        vnum=len(mat)
        for x in mat:
            if len(x)!=vnum:
                raise ValueError("Argument for 'Graph'.")
        self._mat=[mat[i][:] for i in range(vnum)]
        self._unconn=unconn
        self._vnum=vnum

    def vertex_num(self):
        return self._vnum
    '''
    当新增顶点时报错
    '''
    def _invalid(self,v):
        return 0 > v or v >= self._vnum
    def add_vertex(self):
        raise ValueError(
            "Adj-Matrix does not support 'add_vertex'."
        )
    '''
    添加一个边的权
    '''
    def add_edge(self,vi,vj,val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi)+'or'+str(vj)+
                             "is not a valid vertex.")
        self._mat[vi][vj]=val
    '''
    获得一个边的权
    '''
    def get_edge(self,vi,vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi)+'or'+str(vj)+
                             "is not a valid vertex.")
        return self._mat[vi][vj]
    @staticmethod
    def _out_edges(row,unconn):
        edges=[]
        for i in  range(len(row)):
            if row[i]!=unconn:
                edges.append((i,row[i]))
        return edges
    '''
    获得出边的节点
    '''
    def out_edges(self,vi):
        if self._invalid(vi):
            raise ValueError(str(vi) +
                             "is not a valid vertex.")
        return self._out_edges(self._mat[vi],self._unconn)
    def __str__(self):
        return ",\n".join(map(str,self._mat))\
                +"\nUnconnected:"+str(self._unconn)