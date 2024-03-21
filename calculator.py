from typing import List, Union
from random import randint
import math

class Equation:
    def __init__(self) -> None:
        self.type = ''
        self.var = []

f = open('calculator_show.tex', 'w')
f_py = open('calculator_py_code.py', 'w')


def pycode_equ_print(equ : Equation):
    if equ.type == 'number':
        f_py.write('c_num('+format(equ.var)+')')
    if equ.type == 'variable':
        f_py.write('c_var(\''+equ.var+'\')')
    if equ.type == '+':
        f_py.write('(')
        pycode_equ_print(equ.var[0])
        f_py.write('+')
        pycode_equ_print(equ.var[1])
        f_py.write(')')
    if equ.type == '-':
        f_py.write('(')
        pycode_equ_print(equ.var[0])
        f_py.write('-')
        pycode_equ_print(equ.var[1])
        f_py.write(')')
    if equ.type == '*':
        f_py.write('(')
        pycode_equ_print(equ.var[0])
        f_py.write('*')
        pycode_equ_print(equ.var[1])
        f_py.write(')')
    if equ.type == '/':
        f_py.write('(')
        pycode_equ_print(equ.var[0])
        f_py.write('/')
        pycode_equ_print(equ.var[1])
        f_py.write(')')
    if equ.type == '^':
        f_py.write('(')
        pycode_equ_print(equ.var[0])
        f_py.write('^')
        pycode_equ_print(equ.var[1])
        f_py.write(')')
    if equ.type == 'sqrt':
        f_py.write('c_sqrt(')
        pycode_equ_print(equ.var)
        f_py.write(')')
    if equ.type == 'sin':
        f_py.write('c_sin(')
        pycode_equ_print(equ.var)
        f_py.write(')')
    if equ.type == 'cos':
        f_py.write('c_cos(')
        pycode_equ_print(equ.var)
        f_py.write(')')
    if equ.type == 'tan':
        f_py.write('c_tan(')
        pycode_equ_print(equ.var)
        f_py.write(')')
    if equ.type == 'ln':
        f_py.write('c_ln(')
        pycode_equ_print(equ.var)
        f_py.write(')')
    if equ.type == '2ordequ':
        f_py.write('c_2ordequ(')
        pycode_equ_print(equ.var[0])
        f_py.write(',')
        pycode_equ_print(equ.var[1])
        f_py.write(',')
        pycode_equ_print(equ.var[2])
        f_py.write(')')
    if equ.type == 'matrix':
        f_py.write('c_matrix([')
        m = len(equ.var)
        n = len(equ.var[0])
        for i in range(m):
            f_py.write('[')
            for j in range(n):
                if j != 0:
                    f_py.write(',')
                pycode_equ_print(equ.var[i][j])
            if i == n - 1:
                f_py.write(']')
            else:
                f_py.write('],\n          ')
        f_py.write('])')

def pycode_print(equ : Equation):
    f_py.write('from calculator import *\n\n')
    pycode_equ_print(equ)

def latex_equ_print(equ : Equation):
    if equ.type == 'number':
        f.write(format(equ.var))
    if equ.type == 'variable':
        f.write(equ.var)
    if equ.type == '+':
        f.write('(')
        latex_equ_print(equ.var[0])
        f.write('+')
        latex_equ_print(equ.var[1])
        f.write(')')
    if equ.type == '-':
        f.write('(')
        latex_equ_print(equ.var[0])
        f.write('-')
        latex_equ_print(equ.var[1])
        f.write(')')
    if equ.type == '*':
        f.write('(')
        latex_equ_print(equ.var[0])
        f.write('\\times ')
        latex_equ_print(equ.var[1])
        f.write(')')
    if equ.type == '/':
        f.write('(\\frac{')
        latex_equ_print(equ.var[0])
        f.write('}{')
        latex_equ_print(equ.var[1])
        f.write('})')
    if equ.type == '^':
        f.write('{')
        latex_equ_print(equ.var[0])
        f.write('}^{')
        latex_equ_print(equ.var[1])
        f.write('}')
    if equ.type == 'sqrt':
        f.write('\\sqrt{')
        latex_equ_print(equ.var)
        f.write('}')
    if equ.type == 'sin':
        f.write('\\sin{')
        latex_equ_print(equ.var)
        f.write('}')
    if equ.type == 'cos':
        f.write('\\cos{')
        latex_equ_print(equ.var)
        f.write('}')
    if equ.type == 'tan':
        f.write('\\tan{')
        latex_equ_print(equ.var)
        f.write('}')
    if equ.type == 'ln':
        f.write('\\ln{')
        latex_equ_print(equ.var)
        f.write('}')
    if equ.type == '2ordequ':
        latex_equ_print(equ.var[0])
        f.write('x^2+')
        latex_equ_print(equ.var[1])
        f.write('x+')
        latex_equ_print(equ.var[2])
        f.write('=0')
    if equ.type == 'matrix':
        f.write('\\begin{bmatrix}\n')
        m = len(equ.var)
        n = len(equ.var[0])
        for i in range(m):
            for j in range(n):
                if j != 0:
                    f.write('&')
                latex_equ_print(equ.var[i][j])
            f.write('\\\\\n')
        f.write('\\end{bmatrix}')

def latex_print(Equ : Union[Equation, List[Equation]]):
    f.write('\\documentclass{article}'+'\n')
    f.write('\\usepackage{amsmath}'+'\n')
    f.write('\\begin{document}'+'\n')
    if isinstance(Equ, Equation):
        Equ = [Equ]
    for equ in Equ:
        f.write('$$\n')
        latex_equ_print(equ)
        f.write('\n$$\n')
    f.write('\\end{document}'+'\n')

def equ_copy(equ : Equation):
    Equ = Equation()
    Equ.type = equ.type
    if equ.type == 'number' or equ.type == 'variable':
        Equ.var = equ.var
    else:
        if isinstance(equ.var, Equation):
            Equ.var = equ_copy(equ.var)
        else:
            if equ.type == 'matrix':
                m = len(equ.var)
                n = len(equ.var[0])
                Equ.var = [[Equation() for j in range(n)] for i in range(m)]
                for i in range(m):
                    for j in range(n):
                        Equ.var[i][j] = equ_copy(equ.var[i][j])
            else:
                for e in equ.var:
                    E = equ_copy(e)
                    Equ.var.append(E)
    return Equ

def equ_id(equ1 : Equation, equ2 : Equation):
    if equ1.type != equ2.type:
        return 0
    if equ1.type == 'number' or equ1.type == 'variable':
        return equ1.var == equ2.var
    if isinstance(equ1.var, Equation):
        return equ_id(equ1.var, equ2.var)
    n = len(equ1.var)
    for i in range(n):
        if equ_id(equ1.var[i], equ2.var[i]) == 0:
            return 0
    return 1

def c_num(num):
    equ = Equation()
    equ.type = 'number'
    equ.var = num
    return equ

def c_var(var):
    equ = Equation()
    equ.type = 'variable'
    equ.var = var
    return equ

def c_add(equ1 : Equation, equ2 : Equation):
    equ = Equation()
    equ.type = '+'
    equ.var = [equ_copy(equ1), equ_copy(equ2)]
    return equ

def c_add_extra(equ1 : Equation, equ2 : Union[Equation, int]):
    if isinstance(equ2, int):
        equ2 = c_num(equ2)
    if equ1.type == 'matrix' and equ2.type == 'matrix':
        equ = c_matrix_add(equ1, equ2)
    if equ1.type != 'matrix' and equ2.type != 'matrix':
        equ = c_add(equ1, equ2)
    return equ
Equation.__add__ = c_add_extra
Equation.__radd__ = c_add_extra

def c_sub(equ1 : Equation, equ2 : Equation):
    equ = Equation()
    equ.type = '-'
    equ.var = [equ_copy(equ1), equ_copy(equ2)]
    return equ
def c_sub_extra(equ1 : Equation, equ2 : Union[Equation, int]):
    if isinstance(equ2, int):
        equ2 = c_num(equ2)
    if equ1.type == 'matrix' and equ2.type == 'matrix':
        equ = c_matrix_sub(equ1, equ2)
    if equ1.type != 'matrix' and equ2.type != 'matrix':
        equ = c_sub(equ1, equ2)
    return equ
Equation.__sub__ = c_sub_extra

def c_mul(equ1 : Equation, equ2 : Equation):
    equ = Equation()
    equ.type = '*'
    equ.var = [equ_copy(equ1), equ_copy(equ2)]
    return equ

def c_mul_extra(equ1 : Equation, equ2 : Equation):
    if isinstance(equ2, int):
        equ2 = c_num(equ2)
    if equ1.type == 'matrix' and equ2.type != 'matrix':
        equ = c_matrix_mul_num(equ1, equ2)
    if equ1.type != 'matrix' and equ2.type == 'matrix':
        equ = c_matrix_num_mul(equ1, equ2)
    if equ1.type != 'matrix' and equ2.type != 'matrix':
        equ = c_mul(equ1, equ2)
    return equ
Equation.__mul__ = c_mul_extra
Equation.__rmul__ = c_mul_extra

def c_frac(equ1 : Union[Equation, int], equ2 : Union[Equation, int]):
    if isinstance(equ1, int):
        equ2 = c_num(equ1)
    if isinstance(equ2, int):
        equ2 = c_num(equ2)
    equ = Equation()
    equ.type = '/'
    equ.var = [equ_copy(equ1), equ_copy(equ2)]
    return equ

def c_frac_extra(equ1 : Equation, equ2 : Union[Equation, int]):
    if equ1.type == 'matrix':
        return  c_matrix_div_num(equ1, equ2)
    else:
        return c_frac(equ1, equ2)
Equation.__truediv__ = c_frac_extra

def c_power(equ1 : Union[Equation, int], equ2 : Union[Equation, int]):
    if isinstance(equ1, int):
        equ1 = c_num(equ1)
    if isinstance(equ2, int):
        equ2 = c_num(equ2)
    equ = Equation()
    equ.type = '^'
    equ.var = [equ_copy(equ1), equ_copy(equ2)]
    return equ

def c_power_extra(equ1 : Union[Equation, int], equ2 : Union[Equation, int]):
    if isinstance(equ2, int):
        equ2 = c_num(equ2)
    if equ1.type == 'matrix' and equ2.type == 'number':
        equ = equ_copy(equ1)
        for i in range(equ2.var-1):
            equ = equ @ equ1
    else:
        equ = c_power(equ1, equ2)
    return equ
Equation.__xor__ = c_power_extra
Equation.__pow__ = c_power_extra

def c_sqrt(equ1 : Union[Equation, int]):
    if isinstance(equ1, int):
        equ1 = c_num(equ1)
    equ = Equation()
    equ.type = 'sqrt'
    equ.var = equ_copy(equ1)
    return equ

def c_sin(equ1 : Union[Equation, int]):
    if isinstance(equ1, int):
        equ1 = c_num(equ1)
    equ = Equation()
    equ.type = 'sin'
    equ.var = equ_copy(equ1)
    return equ

def c_cos(equ1 : Union[Equation, int]):
    if isinstance(equ1, int):
        equ1 = c_num(equ1)
    equ = Equation()
    equ.type = 'cos'
    equ.var = equ_copy(equ1)
    return equ

def c_tan(equ1 : Union[Equation, int]):
    if isinstance(equ1, int):
        equ1 = c_num(equ1)
    equ = Equation()
    equ.type = 'tan'
    equ.var = equ_copy(equ1)
    return equ

def c_ln(equ1 : Union[Equation, int]):
    if isinstance(equ1, int):
        equ1 = c_num(equ1)
    equ = Equation()
    equ.type = 'ln'
    equ.var = equ_copy(equ1)
    return equ

def c_assign(Equ : Equation, equ1 : Equation, equ2 : Equation):
    equ = Equation()
    equ.type = Equ.type
    if equ_id(Equ, equ1):
        equ = equ_copy(equ2)
        return equ
    if Equ.type != 'number' and Equ.type != 'variable':
        if isinstance(Equ.var, Equation):
            equ.var = c_assign(Equ.var, equ1, equ2)
        else:
            m = len(Equ.var)
            if Equ.type == 'matrix':
                n = len(Equ.var[0])
                equ.var = [[Equation() for j in range(n)] for i in range(m)]
                for i in range(m):
                    for j in range(n):
                        equ.var[i][j] = c_assign(Equ.var[i][j], equ1, equ2)
            else:
                equ.var = [Equation() for i in range(m)]
                for i in range(m):
                    equ.var[i] = c_assign(Equ.var[i], equ1, equ2)
    else:
        equ.var = Equ.var
    return equ

def c_matrix(Equ : List[List[Union[Equation, int]]]):
    equ = Equation()
    equ.type = 'matrix'
    m = len(Equ)
    n = len(Equ[0])
    equ.var = [[Equation() for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if isinstance(Equ[i][j], int):
                equ.var[i][j] = equ_copy(c_num(Equ[i][j]))
            else:
                equ.var[i][j] = equ_copy(Equ[i][j])
    return equ

def c_matrix_eye(n : int):
    equ = Equation()
    equ.type = 'matrix'
    equ.var = [[Equation() for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            equ.var[i][j] = c_num(int(i == j))
    return equ

def c_matrix_t(Equ : Equation):
    equ = Equation()
    equ.type = 'matrix'
    m = len(Equ.var)
    n = len(Equ.var[0])
    equ.var = [[Equation() for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            equ.var[j][i] = equ_copy(Equ.var[i][j])
    return equ

def c_matrix_add(equ1 : Equation, equ2 : Equation):
    equ = Equation()
    equ.type = 'matrix'
    m = len(equ1.var)
    n = len(equ1.var[0])
    equ.var = [[Equation() for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            equ.var[i][j] = equ1.var[i][j] + equ2.var[i][j]
    return equ

def c_matrix_sub(equ1 : Equation, equ2 : Equation):
    equ = Equation()
    equ.type = 'matrix'
    m = len(equ1.var)
    n = len(equ1.var[0])
    equ.var = [[Equation() for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            equ.var[i][j] = equ1.var[i][j] - equ2.var[i][j]
    return equ

def c_matrix_mul(equ1 : Equation, equ2 : Equation):
    m = len(equ1.var)
    n = len(equ2.var[0])
    l = len(equ2.var)
    equ = Equation()
    equ.type = 'matrix'
    equ.var = [[Equation() for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            equ.var[i][j] = c_num(0)
            for k in range(l):
                equ.var[i][j] = equ.var[i][j]+equ1.var[i][k]*equ2.var[k][j]
    return equ
Equation.__matmul__ = c_matrix_mul

def c_matrix_num_mul(equ1 : Equation, Equ : Equation):
    equ = equ_copy(Equ)
    m = len(equ.var)
    n = len(equ.var[0])
    for i in range(m):
        for j in range(n):
            equ.var[i][j] = equ1 * equ.var[i][j]
    return equ

def c_matrix_mul_num(Equ : Equation, equ1 : Equation):
    equ = equ_copy(Equ)
    m = len(equ.var)
    n = len(equ.var[0])
    for i in range(m):
        for j in range(n):
            equ.var[i][j] = equ.var[i][j] * equ1
    return equ

def c_matrix_div_num(equ : Equation, equ1 : Equation):
    m = len(equ.var)
    n = len(equ.var[0])
    for i in range(m):
        for j in range(n):
            equ.var[i][j] = equ.var[i][j] / equ1
    return equ

def c_matrix_tr(equ1 : Equation):
    m = len(equ1.var)
    n = len(equ1.var[0])
    n = min(m, n)
    equ = equ1.var[0][0]
    for i in range(1, n):
        equ = c_add(equ, equ1.var[i][i])
    return equ

def c_matrix_det(equ1 : Equation):
    m = len(equ1.var)
    n = len(equ1.var[0])
    if m == 1 and n == 1:
        equ = equ_copy(equ1.var[0][0])
    if m == 2 and n == 2:
        equ = c_sub(c_mul(equ1.var[0][0], equ1.var[1][1]),c_mul(equ1.var[0][1], equ1.var[1][0]))
    if m == 3 and n == 3:
        e1 = c_add(c_add(c_mul(equ1.var[0][0],c_mul(equ1.var[1][1],equ1.var[2][2])),
                         c_mul(equ1.var[0][1],c_mul(equ1.var[1][2],equ1.var[2][0]))),
                         c_mul(equ1.var[0][2],c_mul(equ1.var[1][0],equ1.var[2][1])))
        e2 = c_add(c_add(c_mul(equ1.var[0][2],c_mul(equ1.var[1][1],equ1.var[2][0])),
                         c_mul(equ1.var[0][1],c_mul(equ1.var[1][0],equ1.var[2][2]))),
                         c_mul(equ1.var[0][0],c_mul(equ1.var[1][2],equ1.var[2][1])))
        equ = c_sub(e1, e2)
    return equ

def c_matrix_seq_form(Equ : Equation, p : int, q : int):
    equ = Equation()
    equ.type = 'matrix'
    m = len(Equ.var)
    n = len(Equ.var[0])
    equ.var = [[Equation() for j in range(n-1)] for i in range(m-1)]
    for i in range(n-1):
        for j in range(m-1):
            if i >= p:
                ii = i + 1
            else:
                ii = i
            if j >= q:
                jj = j + 1
            else:
                jj = j
            equ.var[i][j] = Equ.var[ii][jj]
    return equ

def c_matrix_inv_mul_det(Equ : Equation):
    equ = Equation()
    equ.type = 'matrix'
    m = len(Equ.var)
    n = len(Equ.var[0])
    equ.var = [[Equation() for i in range(m)] for j in range(n)]
    if m == n:
        for i in range(m):
            for j in range(n):
                equ1 = c_matrix_det(c_matrix_seq_form(Equ, i, j))
                if (i + j) & 1:
                    equ.var[j][i] = -1 * equ1
                else:
                    equ.var[j][i] = equ1
    return equ

def c_matrix_inv(Equ : Equation):
    equ = Equation()
    equ.type = 'matrix'
    m = len(Equ.var)
    n = len(Equ.var[0])
    equ.var = [[Equation() for i in range(m)] for j in range(n)]
    if m == n:
        for i in range(m):
            for j in range(n):
                equ1 = c_matrix_det(c_matrix_seq_form(Equ, i, j))
                if (i + j) & 1:
                    equ.var[j][i] = -1 * equ1
                else:
                    equ.var[j][i] = equ1
        equ = equ / c_matrix_det(Equ)
    # if m == 2 and n == 2:
    #     equ = c_matrix([[Equ.var[1][1],Equ.var[0][1]*cn1],
    #                     [Equ.var[1][0]*cn1,Equ.var[0][0]]])
    #     equ = c_matrix_div_num(equ, c_matrix_det(equ))
    return equ

def c_matrix_eigenfunc(Equ : Equation):
    m = len(Equ.var)
    n = len(Equ.var[0])
    if m == n:
        x = c_var('x')
        return c_matrix_det(x*c_matrix_eye(n)-Equ)

def c_matrix_eigenvalue(Equ : Equation):
    m = len(Equ.var)
    n = len(Equ.var[0])
    if m == 2 and n == 2:
        trA = c_matrix_tr(Equ)
        detA = c_matrix_det(Equ)
        equ1 = c_frac(c_add(trA,c_sqrt(c_sub(c_mul(trA,trA),c_mul(c_num(4),detA)))),c_num(2))
        equ2 = c_frac(c_sub(trA,c_sqrt(c_sub(c_mul(trA,trA),c_mul(c_num(4),detA)))),c_num(2))
        return equ1, equ2
    
def c_matrix_eigen(Equ : Equation):
    m = len(Equ.var)
    n = len(Equ.var[0])
    if m == 2 and n == 2:
        e1, e2 = c_matrix_eigenvalue(Equ)
        if Equ.var[0][1].type == 'number' and Equ.var[0][1].var == 0:
            a2 = c_sub(e1, Equ.var[1][1])
            a1 = Equ.var[1][0]
            qa = c_sqrt(a1**2+a2**2)
        else:
            a1 = c_sub(e1, Equ.var[0][0])
            a2 = Equ.var[0][1]
            qa = c_sqrt(a1**2+a2**2)
        if Equ.var[1][0].type == 'number' and Equ.var[1][0].var == 0:
            b1 = c_sub(e2, Equ.var[0][0])
            b2 = Equ.var[0][1]
            qb = c_sqrt(b1**2+b2**2)
        else:
            b2 = c_sub(e2, Equ.var[1][1])
            b1 = Equ.var[1][0]
            qb = c_sqrt(b1**2+b2**2)
        return c_matrix([[a2/qa,b2/qb],[a1/qa,b1/qb]]), c_matrix([[e1, 0], [0, e2]])

def c_2ordequ_rt(Equ : Equation):
    e0 = Equ.var[0]
    e1 = Equ.var[1]
    e2 = Equ.var[2]
    equ1 = c_frac(c_sub(c_sqrt(c_sub(c_mul(e1,e1),c_mul(c_num(4),c_mul(e0,e2)))),e1),c_mul(c_num(2),e0))
    equ2 = c_frac(c_sub(c_mul(c_num(-1),c_sqrt(c_sub(c_mul(e1,e1),c_mul(c_num(4),c_mul(e0,e2))))),e1),c_mul(c_num(2),e0))
    return equ1, equ2

def c_2ordequ(equ1 : Equation, equ2 : Equation, equ3 : Equation, sign = 'x'):
    equ = Equation()
    equ.type = '2ordequ'
    equ.var = [equ1, equ2, equ3]
    equ.sign = sign
    return equ

def cancel_num_div_check(equ : Equation, cancel_num_div : Union[Equation, int]):
    if equ.type == 'number' and isinstance(cancel_num_div, int):
        if cancel_num_div != -1 and equ.var % cancel_num_div == 0:
            return c_num(int(equ.var / cancel_num_div))
        if cancel_num_div == -1 and equ.var < 0:
            return c_num(-equ.var)
    if isinstance(cancel_num_div, Equation) and equ_id(cancel_num_div, equ):
        return c_num(1)
    if equ.type == '+':
        equ1 = cancel_num_div_check(equ.var[0], cancel_num_div)
        if isinstance(equ1, int):
            return 0
        equ2 = cancel_num_div_check(equ.var[1], cancel_num_div)
        if isinstance(equ2, int):
            return 0
        return equ1 + equ2
    if equ.type == '-':
        equ1 = cancel_num_div_check(equ.var[0], cancel_num_div)
        if isinstance(equ1, int):
            return 0
        if cancel_num_div == -1:
            return equ1 + equ.var[1]
        equ2 = cancel_num_div_check(equ.var[1], cancel_num_div)
        if isinstance(equ2, int):
            return 0
        return equ1 - equ2
    if equ.type == '*':
        equ1 = cancel_num_div_check(equ.var[0], cancel_num_div)
        if isinstance(equ1, int) == 0:
            return equ1 * equ.var[1]
        equ1 = cancel_num_div_check(equ.var[1], cancel_num_div)
        if isinstance(equ1, int) == 0:
            return equ.var[0] * equ1
    if equ.type == '/':
        equ1 = cancel_num_div_check(equ.var[0], cancel_num_div)
        if isinstance(equ1, int) == 0:
            return equ1 / equ.var[1]
    if equ.type == '^':
        if isinstance(cancel_num_div, Equation) and equ_id(equ.var[0], cancel_num_div):
            return equ.var[0] ^ (equ.var[1] - 1)
    if equ.type == 'sqrt' and isinstance(cancel_num_div, int) and cancel_num_div != -1:
        equ1 = cancel_num_div_check(equ.var, cancel_num_div**2)
        if isinstance(equ1, int) == 0:
            return c_sqrt(equ1)
    return 0

def cancel_num_frac_check(equ : Equation): # no frac return 1
    if equ.type == '+':
        return cancel_num_frac_check(equ.var[0]) and cancel_num_frac_check(equ.var[1])
    if equ.type == '-':
        return cancel_num_frac_check(equ.var[0]) and cancel_num_frac_check(equ.var[1])
    if equ.type == '*':
        return cancel_num_frac_check(equ.var[0]) and cancel_num_frac_check(equ.var[1])
    if equ.type == '/':
        return 0
    return 1

def cancel_num(Equ : Equation):
    equ = Equation()
    equ.type = Equ.type
    equ.var = Equ.var
    if equ.type == '+':
        equ.var[0] = cancel_num(equ.var[0])
        equ.var[1] = cancel_num(equ.var[1])
        if (equ.var[0].type == 'number' and 
            equ.var[1].type == 'number'):
            equ.type = 'number'
            equ.var = equ.var[0].var+equ.var[1].var
            return equ
        for k in range(2):
            if equ.var[k].type == 'number' and equ.var[k].var == 0:
                equ = equ_copy(equ.var[1-k])
                return equ
        if randint(0, 1):
            e = equ_copy(equ.var[1])
            equ.var[1] = equ_copy(equ.var[0])
            equ.var[0] = e
        if equ.var[1].type == '+' and randint(0, 1):
            equ = c_add(c_add(equ.var[0],equ.var[1].var[0]),
                        equ.var[1].var[1])
        if equ.var[1].type == '-':
            p = randint(0, 2)
            if p == 0:
                equ = c_add(c_sub(equ.var[0],equ.var[1].var[1]),
                            equ.var[1].var[0])
            if p == 1:
                equ = c_sub(c_add(equ.var[0],equ.var[1].var[0]),
                            equ.var[1].var[1])
                return equ
        for k in range(2):
            if equ.var[k].type == 'number' and equ.var[k].var < 0:
                equ = c_sub(equ.var[1-k], c_num(-equ.var[k].var))
                return equ
            if equ.var[k].type == '*':
                for j in range(2):
                    if equ.var[k].var[j].type == 'number' and equ.var[k].var[j].var < 0:
                        equ = c_sub(equ.var[1-k],
                                      c_mul(equ.var[k].var[1-j],c_num(-equ.var[k].var[j].var)))
                        return equ
            if equ.var[k].type == '/' and cancel_num_frac_check(equ.var[1-k]):
                equ = c_frac(c_add(equ.var[k].var[0],c_mul(equ.var[1-k],equ.var[k].var[1])),
                            equ.var[k].var[1])
                return equ
        if equ_id(equ.var[0], equ.var[1]):
            equ = c_mul(c_num(2), equ.var[0])
            return equ
        if equ.var[0].type == '/' and equ.var[1].type == '/':
            if equ_id(equ.var[0].var[1], equ.var[1].var[1]):
                equ = c_frac(c_add(equ.var[0].var[0], equ.var[1].var[0]),equ.var[1].var[1])
                return equ
            # equ = (equ.var[0].var[0]*equ.var[1].var[1]+
            #        equ.var[0].var[1]*equ.var[1].var[0])/(equ.var[0].var[1]*equ.var[1].var[1])
            return equ
        if equ.var[0].type == '*':
            if (equ.var[0].var[0].type == 'number' and 
                equ_id(equ.var[0].var[1], equ.var[1])):
                equ = c_mul(c_num(equ.var[0].var[0].var+1), equ.var[1])
                return equ
            if (equ.var[1].type == '*' and
                equ.var[0].var[0].type == 'number' and 
                equ.var[1].var[0].type == 'number' and
                equ_id(equ.var[0].var[1], equ.var[1].var[1])):
                equ = c_mul(c_num(equ.var[0].var[0].var+equ.var[1].var[0].var),
                             equ.var[0].var[1])
                return equ
    if equ.type == '-':
        equ.var[0] = cancel_num(equ.var[0])
        equ.var[1] = cancel_num(equ.var[1])
        if (equ.var[0].type == 'number' and 
            equ.var[1].type == 'number'):
            equ.type = 'number'
            equ.var = equ.var[0].var-equ.var[1].var
            return equ
        if equ.var[1].type == 'number' and equ.var[1].var == 0:
            equ = equ.var[0]
            return equ
        if equ.var[1].type == 'number' and equ.var[1].var < 0:
            equ = equ.var[0] + c_num(-equ.var[1].var)
            return equ
        # if randint(0, 1):
        #     equ = c_num(-1) * equ.var[1] + equ.var[0]
        #     return equ
        if equ_id(equ.var[0], equ.var[1]):
            equ = c_num(0)
            return equ
        if equ.var[0].type == '/' and cancel_num_frac_check(equ.var[1]):
            equ = c_frac(c_sub(equ.var[0].var[0],c_mul(equ.var[1],equ.var[0].var[1])),
                         equ.var[0].var[1])
            return equ
        if equ.var[0].type == '+' and randint(0, 1):
            equ = c_add(c_sub(equ.var[0].var[0],equ.var[1]),
                        equ.var[0].var[1])
            return equ
        if equ.var[1].type == '+' and randint(0, 1):
            equ = c_sub(c_sub(equ.var[0],equ.var[1].var[0]),
                        equ.var[1].var[1])
        if equ.var[0].type == '-':
            p = randint(0, 1)
            if p == 0:
                equ = c_sub(c_sub(equ.var[0].var[0],equ.var[1]),
                              equ.var[0].var[1])
            if p == 1:
                equ = c_sub(equ.var[0].var[0],
                              c_add(equ.var[0].var[1],equ.var[1]))
        if equ.var[1].type == '-':
            p = randint(0, 1)
            if p == 0:
                equ = c_add(c_sub(equ.var[0],equ.var[1].var[0]),
                            equ.var[1].var[1])
                return equ
            if p == 1:
                equ = c_sub(c_add(equ.var[0],equ.var[1].var[1]),
                              equ.var[1].var[0])
        if equ.var[0].type == '*':
            if (equ.var[0].var[0].type == 'number' and 
                equ_id(equ.var[0].var[1], equ.var[1])):
                equ = c_mul(c_num(equ.var[0].var[0].var-1), equ.var[1])
                return equ
            if (equ.var[1].type == '*' and
                equ.var[0].var[0].type == 'number' and 
                equ.var[1].var[0].type == 'number' and
                equ_id(equ.var[0].var[1], equ.var[1].var[1])):
                equ = c_mul(c_num(equ.var[0].var[0].var-equ.var[1].var[0].var),
                             equ.var[0].var[1])
                return equ
        if equ.var[1].type == '/' and cancel_num_frac_check(equ.var[0]):
            equ = (equ.var[0]*equ.var[1].var[1]-equ.var[1].var[0])/equ.var[1].var[1]
            return equ
        if equ.var[0].type == '/' and equ.var[1].type == '/':
            if equ_id(equ.var[0].var[1], equ.var[1].var[1]):
                equ = (equ.var[0].var[0]-equ.var[1].var[0])/equ.var[1].var[1]
                return equ
        #     equ = (equ.var[0].var[0]*equ.var[1].var[1]-
        #            equ.var[0].var[1]*equ.var[1].var[0])/(equ.var[0].var[1]*equ.var[1].var[1])
            return equ
    if equ.type == '*':
        equ.var[0] = cancel_num(equ.var[0])
        equ.var[1] = cancel_num(equ.var[1])
        if (equ.var[0].type == 'number' and 
            equ.var[1].type == 'number'):
            equ.type = 'number'
            equ.var = equ.var[0].var * equ.var[1].var
            return equ
        if equ_id(equ.var[0], equ.var[1]):
            equ.type = '^'
            equ.var[1] = c_num(2)
            return equ
        if (equ.var[1].type == '^' and
            equ_id(equ.var[1].var[0], equ.var[0])):
            equ.type = '^'
            equ.var[1] = c_num(1) + equ.var[1].var[1]
            return equ
        if randint(0, 1):
            e = equ_copy(equ.var[1])
            equ.var[1] = equ_copy(equ.var[0])
            equ.var[0] = e
        if equ.var[1].type == '*' and randint(0, 1):
            equ = c_mul(c_mul(equ.var[0],equ.var[1].var[0]),
                        equ.var[1].var[1])
        if (equ.var[0].type == 'sqrt' and 
            equ.var[1].type == 'sqrt'):
            equ.type = 'sqrt'
            equ.var = c_mul(equ.var[0].var, equ.var[1].var)
            return equ
        for k in range(2):
            if equ.var[k].type == 'number' and equ.var[k].var == 1:
                equ = equ.var[1-k]
                return equ
            if equ.var[k].type == 'number' and equ.var[k].var == 0:
                equ = c_num(0)
                return equ
            if equ.var[k].type == '+':
                equ = c_add(c_mul(equ.var[k].var[0],equ.var[1-k]),
                            c_mul(equ.var[k].var[1],equ.var[1-k]))
                return equ
            if equ.var[k].type == '-':
                equ = c_sub(c_mul(equ.var[k].var[0],equ.var[1-k]),
                            c_mul(equ.var[k].var[1],equ.var[1-k]))
                return equ
            if equ.var[k].type == '/' and cancel_num_frac_check(equ.var[1-k]):
                equ = c_frac(c_mul(equ.var[k].var[0],equ.var[1-k]),
                            equ.var[k].var[1])
                return equ
        if equ.var[0].type == '/' and equ.var[1].type == '/':
            equ = c_frac(c_mul(equ.var[0].var[0],equ.var[1].var[0]),
                         c_mul(equ.var[0].var[1],equ.var[1].var[1]))
            return equ
        if (equ.var[0].type == '^' and equ.var[1].type == '^' and 
            equ_id(equ.var[0].var[0], equ.var[1].var[0])):
            equ = c_power(equ.var[0].var[0], 
                          c_add(equ.var[0].var[1], equ.var[1].var[1]))
            return equ
    if equ.type == '/':
        equ.var[0] = cancel_num(equ.var[0])
        equ.var[1] = cancel_num(equ.var[1])
        if (equ.var[0].type == 'number' and 
            equ.var[1].type == 'number' and 
            equ.var[0].var % equ.var[1].var == 0):
            equ.type = 'number'
            equ.var = int(equ.var[0].var/equ.var[1].var)
            return equ
        if (equ.var[0].type == 'number' and 
            equ.var[0].var == 0):
            equ = c_num(0)
            return equ
        if (equ.var[1].type == 'number' and 
            equ.var[1].var == 1):
            equ = equ.var[0]
            return equ
        if equ.var[0].type == '/':
            equ = c_frac(equ.var[0].var[0],
                         c_mul(equ.var[1],equ.var[0].var[1]))
        if equ.var[1].type == '/':
            equ = equ.var[0]*equ.var[1].var[1]/equ.var[1].var[0]
        cancel_num_div = [-1, 2, 3, 5, 7, 11, 13]
        for p in cancel_num_div:
            if p == -1:
                equ2 = cancel_num_div_check(equ.var[1], p)
                if isinstance(equ2, int) == 0:
                    equ = -1 * equ.var[0] / equ2
                continue
            equ1 = cancel_num_div_check(equ.var[0], p)
            if isinstance(equ1, int):
                continue
            equ2 = cancel_num_div_check(equ.var[1], p)
            if isinstance(equ2, int):
                continue
            equ = equ1 / equ2
        equ1 = cancel_num_div_check(equ.var[0], equ.var[1])
        if isinstance(equ1, Equation):
            equ = equ_copy(equ1)
            return equ
    if equ.type == '^':
        equ.var[0] = cancel_num(equ.var[0])
        equ.var[1] = cancel_num(equ.var[1])
        if (equ.var[1].type == 'number' and 
            equ.var[1].var == 1):
            equ = equ.var[0]
            return equ
        if (equ.var[1].type == 'number' and 
            equ.var[1].var == 0):
            equ = c_num(1)
            return equ
        if (equ.var[0].type == 'number' and 
            equ.var[1].type == 'number'):
            equ.type = 'number'
            equ.var = int(math.pow(equ.var[0].var, equ.var[1].var))
            return equ
        if equ.var[0].type == '^':
            equ = equ.var[0].var[0]^(equ.var[0].var[1]*equ.var[1])
            return equ
        if equ.var[0].type == '*':
            equ = (equ.var[0].var[0]^equ.var[1])*(equ.var[0].var[1]^equ.var[1])
            return equ
        if equ.var[0].type == '+' and equ.var[1].type == 'number':
            equ1 = c_num(0)
            n = equ.var[1].var
            for i in range(n+1):
                equ1 = equ1+math.comb(n,i)*(equ.var[0].var[0]^i)*(equ.var[0].var[1]^(n-i))
            equ = equ_copy(equ1)
            return equ
        if equ.var[0].type == '-' and equ.var[1].type == 'number':
            equ1 = c_num(0)
            n = equ.var[1].var
            for i in range(n+1):
                if i & 1:
                    equ1 = equ1+math.comb(n,i)*(equ.var[0].var[0]^i)*(equ.var[0].var[1]^(n-i))
                else:
                    equ1 = equ1-math.comb(n,i)*(equ.var[0].var[0]^i)*(equ.var[0].var[1]^(n-i))
            equ = equ_copy(equ1)
            return equ
        if equ.var[0].type == '/':
            equ = (equ.var[0].var[0]^equ.var[1])/(equ.var[0].var[1]^equ.var[1])
            return equ
    if equ.type == 'sqrt':
        equ.var = cancel_num(equ.var)
        if equ.var.type == 'number':
            sq = int(math.sqrt(equ.var.var))
            if sq * sq == equ.var.var:
                equ.type = 'number'
                equ.var = sq
                return equ
    if equ.type == 'sin':
        equ.var = cancel_num(equ.var)
    if equ.type == 'cos':
        equ.var = cancel_num(equ.var)
    if equ.type == 'tan':
        equ.var = cancel_num(equ.var)
    if equ.type == 'matrix':
        m = len(equ.var)
        n = len(equ.var[0])
        for i in range(m):
            for j in range(n):
                equ.var[i][j] = cancel_num(equ.var[i][j])
    return equ

def cancel_all(Equ : Union[Equation, List[Equation]], T = 1000):
    if isinstance(Equ, Equation):
        for t in range(T):
            Equ = cancel_num(Equ)
        return Equ
    m = len(Equ)
    for i in range(m):
        for t in range(T):
            Equ[i] = cancel_num(Equ[i])
    return Equ