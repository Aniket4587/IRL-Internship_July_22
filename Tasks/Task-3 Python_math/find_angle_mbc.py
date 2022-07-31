import math
AB,BC=int(input()),int(input())
#to calculate hypotenuse
hype=math.hypot(AB,BC)
#to calculate required angle                       
res=round(math.degrees(math.acos(BC/hype)))
#for DEGREE symbol 
degree=chr(176)                                
print(res,degree, sep='')
