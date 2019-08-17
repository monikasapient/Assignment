import sys

class vector:
	def __init__(self,a = 0, b =0, c =0):
		self.size = size
        self.a = a
        self.b = b
        self.c = c

	def __add__(self,other):
		return vector(self.a+other.a, self.b + other.b, self.c + other.c)
	

	def __sub__(self,other):
	
		return vector(self.a-other.a, self.b - other.b, self.c - other.c)
	
	def __eq__(self,other):
        return self.a==other.a and b.self == other.b and c.self == other.c

	def __mul__(self,other):
        return vector(self.a*other.a, self.b*other.b, self.c*other.c)
		



if __name__ == "__main__": 
    v1 = vector(10,20,30)
    v2 = vector(11,22,33)

    v3 = v1 + v2
    print(v3)

