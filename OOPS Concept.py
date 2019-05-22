'''
class MultilevelInheritance:
	def classA(self):
		print('Class A')

class child(MultilevelInheritance):
	def classB(self):
		print('Class B')
		
class son(child):
	def classC(self):
		print('class C')

c = son()
c.classB()
b = child()
b.classA()

'''

'''
class MultipleInheritance:
	def classA(self):
		print('Class A')

class child:
	def classB(self):
		print('Class B')
		
class son(MultipleInheritance,child):
	def classC(self):
		print('class C')

c = son()
c.classB()
c.classA()
'''

'''
class Polymorphism:						# or Overriding
	def classA(self):
		print('Class A Parent')

class child(Polymorphism):
	def classA(self):
		print('Class A child')
		

c = child()
c.classA()
p = Polymorphism()
p.classA()
'''

'''
# use Init constructor
class A:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	
	def funct1(self):
		print(self.name)
		
	def funct2(self):
		print(self.age)
		
a = A('Abhi',26)
a.funct1()
a.funct2()
'''





