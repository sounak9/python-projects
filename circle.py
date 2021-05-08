#a
class circle:
    radious=5

#b
class circle:
    
    def conructer_radious(self,r):
        print(r)
b1=circle()
b1.conructer_radious(5)
#c
def get_radious():
    R1=circle()
    print(R1.radious)
#d
import math
class circle:
    def calc_area(self,radious):
        print("radious=",radious)
        return math.pi*radious**2
obl=circle()
print('areaa if circle is',obl.calc_area(6))