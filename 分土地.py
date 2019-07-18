'''
分土地问题，将一块矩形土地均匀分为若干方形土地，
使得该小块方形土地是最大的能够分拆成的最大土地
'''
def devide(length,width):
    if length%width == 0:
        return width
    else:
        temp = length-length//width*width
        length = max(temp,width)
        width = min(temp,width)
        return devide(length,width)