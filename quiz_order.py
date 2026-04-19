from dis import dis


def quiz1():
	a = 1
	b = a + 4

def quiz2():
	a = 0
	for i in range(10):
		a += 1
	return a

def quiz3():
	def inner_1(val_1):
		return val_1 + 2

	def inner_2(val_2):
		return val_2 * 2

	return inner_1(inner_2(3))

def quiz4():
	return sum([i for i in range(10)])

dis(quiz1)

