# /*
# Let the coordinates of three corners be (x1, y1), (x2, y2) and (x3, y3). And coordinates of the given point P be (x, y)

# 1) Calculate area of the given triangle, i.e., area of the triangle ABC in the above diagram. Area A = [ x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2)]/2
# 2) Calculate area of the triangle PAB. We can use the same formula for this. Let this area be A1.
# 3) Calculate area of the triangle PBC. Let this area be A2.
# 4) Calculate area of the triangle PAC. Let this area be A3.
# 5) If P lies inside the triangle, then A1 + A2 + A3 must be equal to A.
# */


def trianglepoint(x1,y1,x2,y2,x3,y3,x,y):
	A = area (x1, y1, x2, y2, x3, y3)
	# /* Calculate area of triangle PBC */ 
	A1 = area (x, y, x2, y2, x3, y3)
	# /* Calculate area of triangle PAC */  
	A2 = area (x1, y1, x, y, x3, y3)
	# /* Calculate area of triangle PAB */   
	A3 = area (x1, y1, x2, y2, x, y)
	return (A == A1 + A2 + A3)
def area(x1,y1,x2,y2,x3,y3):
	return abs((x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2.0)
print trianglepoint(1,1,2,3,4,5,2,3)

