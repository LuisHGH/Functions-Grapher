import math
import tkinter

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


class Function:
    def __init__(self, coefficients):
        pass

    def printf(self):
        pass

    @staticmethod
    def getfunction(str):
        pass


class FirstDegreeFunction(Function):
    def __init__(self, coefficients):
        super().__init__(coefficients)
        self.a = coefficients[0]
        self.b = coefficients[1]
        if self.a > 0:
            self.progress = 'Growing'
        elif self.a < 0:
            self.progress = 'Descending'
        elif self.a == 0:
            self.progress = 'Null'
        if self.a != 0:
            self.root = -self.b / self.a
        else:
            self.root = 'None'

    def __call__(self, x):
        y = []
        for i in x:
            y.append(self.a * i + self.b)
        return y

    def gety(self, x):  # How the program works mainly with graphs, a "call" function that receives a single value is only present to be used by the Exponential Function exponent variable
        return self.a * x + self.b

    @staticmethod
    def getfunction(str):
        words = str.split('x')
        a = float(words[0])
        b = float(words[1])
        return [a, b]

    def printf(self):
        print("a:", self.a, "b:", self.b, 'root:', self.root, 'Progress:', self.progress)


class SecondDegreeFunction(Function):
    def __init__(self, coefficients):
        super().__init__(coefficients)
        self.a = coefficients[0]
        self.b = coefficients[1]
        self.c = coefficients[2]
        self.delta = self.b ** 2 - 4 * self.a * self.c
        if self.delta > 0:
            self.root = ((- self.b + math.sqrt(self.delta))/(2 * self.a), (- self.b - math.sqrt(self.delta))/(2 * self.a))
        elif self.delta == 0:
            self.root = (- self.b + math.sqrt(self.delta))/2 * self.a
        else:
            self.root = None
        if self.a > 0:
            self.concavity = 'Minimum'
        else:
            self.concavity = 'Maximum'
        self.vertex = (-self.b / (2 * self.a), -self.delta / (4 * self.a))

    def __call__(self, x):
        y = []  # creates an empty list to hold the values of f(x)
        for i in x:
            y.append((self.a * (i ** 2)) + (self.b * i) + self.c)
        return y

    @staticmethod
    def getfunction(str):
        words = str.split('x^2')
        words2 = (words[1].split('x'))
        words[1] = words2[0]
        words.append(words2[1])
        a = float(words[0])
        b = float(words[1])
        c = float(words[2])
        return [a, b, c]

    def printf(self):
        print('a :', self.a, 'b:', self.b, 'c:', self.c, 'delta:', self.delta, 'roots:', self.root, 'concativity:', self.concavity, 'vertex:', self.vertex)


class ExponentialFunction(Function):
    def __init__(self, coefficients):
        super().__init__(coefficients)
        self.a = coefficients[0]
        self.b = coefficients[1]
        self.c = coefficients[2]
        self.d = coefficients[3]
        if self.c == 1 and self.d == 0:
            self.exponent = lambda a: a
        elif self.c == 0:
            self.exponent = lambda a: self.d
        else:
            self.exponent = FirstDegreeFunction([self.c, self.d])

    def __call__(self, x):
        y = []
        for i in x:
            y.append(self.a * (math.pow(self.b, self.exponent(i))))
        return y

    @staticmethod
    def getfunction(str):  # str will be like 'a*b^cx+d'
        words = str.split('*')  # words will be like ['a', 'b^cx+d']
        words2 = words[1].split('^')  # words2 will be like ['b', 'cx+d']
        words3 = words2[1].split('x')  # words3 will be like ['c', 'd']
        words[1] = words2[0]  # changing words[1] from 'b**cx+d' to 'b'
        words.append(words3[0])  # adding 'c'
        words.append(words3[1])  # adding 'd'
        a = float(words[0])  # words is like ['a', 'b', 'c', 'd'] now
        b = float(words[1])
        c = float(words[2])
        d = float(words[3])
        return [a, b, c, d]

    def printf(self):
        print('a:', self.a, 'b:', self.b, 'c:', self.c, 'd:', self.d)


X = range(-10, 10)
print('BEM VINDO AO PROGRAMA DE FUNÇOES MATEMATICAS:')
print('Sintaxe:\n\tFunçao 1 grau: ax+b\n\tFunçao 2 grau: ax^2+bx+c\n\tFunçao exponencial:a*b^cx+d\n')
x = input('Digite a funcao que deseja colocar:')
if 'x^2' in x:
    coefficients = SecondDegreeFunction.getfunction(x)
    myFunction = SecondDegreeFunction(coefficients)
    myFunction.printf()
    plt.plot(X, myFunction(X))
    plt.show()
elif '^' in x:
    coefficients = ExponentialFunction.getfunction(x)
    myFunction = ExponentialFunction(coefficients)
    myFunction.printf()
    plt.plot(X, myFunction(X))
    plt.show()
elif 'x' in x:
    coefficients = FirstDegreeFunction.getfunction(x)
    myFunction = FirstDegreeFunction(coefficients)
    myFunction.printf()
    plt.plot(X, myFunction(X))
    plt.show()
else:
    print('Erro na formataçao do input!')
    print("ABORTANDO PROGRAMA")
