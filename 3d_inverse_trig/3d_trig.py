from math import *

p1 = (0,0,0)
p2 = (22,15,16)

#distance on the x and y axis
dxy = sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
dxz = sqrt((p1[0]-p2[0])**2 + (p1[2]-p2[2])**2)
dzy = sqrt((p1[2]-p2[2])**2 + (p1[1]-p2[1])**2)
dxyz = sqrt((p1[0]-p2[0])**2 + dxy**2)
X = p1[0]-p2[0]
Y = p1[1]-p2[1]
Z = p1[2]-p2[2]

if Y < 0:
    axy = -degrees(asin(X/dxy))+180
else:
    axy = degrees(asin(X/dxy))
if Z < 0:
    axz = -degrees(asin(X/dxz))+180
else:
    axz = degrees(asin(X/dxz))


print(dxyz)
print(f"G1 X{p1[0]} Y{p1[1]} Z{p1[2]}")
res = 5
for i in range(round(dxyz*res)):
    i = i/res

    ixy = (i/dxyz)*dxy
    ixz = (i/dxyz)*dxz

    Xf = -sin(radians(axy))*ixy+p1[0]
    Yf = -cos(radians(axy))*ixy+p1[1]
    Zf = -cos(radians(axz))*ixz+p1[2]


    
    print(f"G1 X{Xf} Y{Yf} Z{Zf}")
print(f"G1 X{p2[0]} Y{p2[1]} Z{p2[2]}")

