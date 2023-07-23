import cProfile

def f():
	for i in range(0,10000):
		for j in range(0,10000):
			z = i * j

cProfile.run('f()')