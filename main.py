import numpy as np
#Zad1
'''
a = np.arange(3, 46, 3)
print(a)
'''
#Zad2
'''
tablicaF = np.arange(5,dtype='float')
tablica64 = tablicaF.astype('int64')
print(tablica64.dtype)
'''
#Zad3
'''
def zadanie3(n):
    tab = np.array([np.arange(1, n+1),np.arange(1, n+1)])
    return tab
x = zadanie3(4)
print(x)
'''
#Zad4
'''
def zadanie4(n,m):
    tab = np.logspace(1,m,m,True,n,'int')
    return tab

print(zadanie4(2,4))
'''
#Zad5
'''
def zadanie5(n):
    wek = np.arange(n,0,-1)
    mat_diag = np.diag(wek)
    return mat_diag

print(zadanie5(4))
'''
#Zad6
'''
mat1 = np.array(list(b"Marcin"))
mat2 = np.array(list(b"aojdkc"))
mat3 = np.array(list(b"rsnosz"))
mat4 = np.array(list(b"cdokju"))
mat5 = np.array(list(b"exyjep"))
mat6 = np.array(list(b"ldxsby"))
matrix = [mat1, mat2, mat3, mat4, mat5, mat6]

print(matrix)

'''
