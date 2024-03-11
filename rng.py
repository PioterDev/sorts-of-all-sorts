import random

def losowe(n: int):
    return [random.randint(1, 10*n) for i in range(n)] if n > 0 else []

def rosnace(n: int):
    return sorted([random.randint(1, 10*n) for i in range(n)]) if n > 0 else []

def malejace(n: int):
	return rosnace(n)[::-1]

def v_ksztaltne(n: int):
	n1 = n // 2
	n2 = n - n1
	return malejace(n1) + rosnace(n2)

def a_ksztaltne(n: int):
	n1 = n // 2
	n2 = n - n1
	return rosnace(n1) + malejace(n2)