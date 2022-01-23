import numpy as np


# Neville method

def neville(datax, datay, x):
    n = len(datax)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x-datax[i+k])*p[i]+ \
                        (datax[i]-x)*p[i+1])/ \
                        (datax[i]-datax[i+k])
    return p[0]


def createTable():
    print("CREATING TABLE\n")
    lenOfTable = int(input("enter number of points\n"))
    datax = []
    datay = []
    for _ in range(lenOfTable):
        print("enter a value for the current point\n")
        x = float(input("x :\n"))
        datax.append(x)
        y = float(input("y :\n"))
        datay.append(y)
    return datax, datay


# Spline Cubic method:

def calculate_h(X):
    h = []
    for i in range(len(X)-1):
        h.append(X[i+1]-X[i])
    return h

def calculate_gama(h):
    gama = []
    gama.append(0)
    for i in range(1, len(h)):
        gama.append(h[i]/(h[i]+h[i-1]))
    gama.append(0)
    return gama


def calculate_meu(gama):
    meu = []
    meu.append(0)
    for i in range(1, len(gama)-1):
        meu.append(1-gama[i])
    meu.append(0)
    return meu


def calculate_d(h, Y):
    d = []
    d.append(0)
    for i in range(1, len(h)):
        d.append((6/(h[i-1]+h[i]))*(((Y[i+1]-Y[i])/h[i])-((Y[i]-Y[i-1])/h[i-1])))
    d.append(0)
    return d


def find_range(X, x0):
    for i in range(len(X)):
        if x0 <= X[i+1] and x0>=X[i]:
            return i
    return False


def cubic_spline(X, Y, x, h, M, i):

    fx = 0
    fx += (((((X[i+1] - x) ** 3) * M[i])+(((x- X[i+1]) ** 3) * M[i+1]))) / (6 * h[i])
    fx += (((X[i+1] - x)*Y[i])+(x-X[i])*Y[i+1])/h[i]
    fx -= ((((X[i+1]-x)*M[i])+((x-X[i])*M[i+1]))*h[i]/6)
    return fx


def create_matrix(meu, gama):
    mat = []
    for i in range(len(meu)):
        mat.append([])
        for _ in range(len(meu)):
            mat[i].append(0)
    for i in range(len(meu)):
        for j in range(len(meu)):
            if i == j:
                mat[i][j] = 2
            if i-1 == j:
                mat[i][j] = meu[i]
            if i == j-1:
                mat[i][j] = gama[i]
    return mat


X = [1, 1.3, 1.6, 1.9, 2.2]
Y = [0.7651, 0.62, 0.4554, 0.2818, 0.1103]
x = 1.5


def Startspline(listx, listy, findpoint):
    h = calculate_h(listx)
    g = calculate_gama(h)
    meu = calculate_meu(g)
    mat = create_matrix(meu, g)
    d = calculate_d(h, listy)
    M = np.linalg.solve(mat, d)
    i = find_range(listx, findpoint)

    print(f'f({findpoint}) = ', cubic_spline(listx, listy, findpoint, h, M, i))


# Driver:

listx, listy = createTable()
findpoint = float(input("enter x you want to find its value\n"))
choose = input("pls choose :\n 1 for Naville method \n 2 for Spline cubic method\n")

if choose == '1':
    print("*** CUBIC SPLINE METHOD ***\n")
    print(neville(listx, listy, findpoint))
elif choose == '2':
    print("*** NEVILLE METHOD ***\n")
    Startspline(listx, listy, findpoint)



