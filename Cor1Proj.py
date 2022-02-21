import math
import matplotlib.pyplot as plt
v_0 = 80.5 # m/s
g = 9.8 # m/s^2
m = 0.04593 # in Kg
C = 4E-4 # in Kg/m
w = 7.27E-5 # angular velocity of the earth. rad/s
l = 37.4109 # degrees
theta = (90-l) 


# F = 2m<v*w>
# F = 2mvwsin(90)
# F = ma => a = 2[(-v_z*w_y)i^+(v_z*w_x)j^+(v_x*w_y-v_y*w_x)k^]


dt = 2E-6
def acceleration(v_x, v_y, v_z, C, m):
    a_x = -C*v_x*math.sqrt(v_x*v_x + v_y*v_y)/m - 2*v_z*(w*math.sin(l*math.pi/180))
    a_y = -g - C*v_y*math.sqrt(v_x*v_x + v_y*v_y)/m + 2*v_z*(w*math.cos(l*math.pi/180))
    a_z = -C*v_z*math.sqrt(v_z*v_z + v_y*v_y)/m +2*(v_x*(w*math.sin(l*math.pi/180))-v_y*(w*math.cos(l*math.pi/180)))
    return a_x, a_y, a_z
def update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt):
    x = x + v_x*dt + 0.5*a_x*dt*dt
    y = y + v_y*dt + 0.5*a_y*dt*dt
    z = z + v_z*dt + 0.5*a_z*dt*dt
    v_x = v_x + a_x*dt
    v_y = v_y + a_y*dt
    v_z = v_z + a_z*dt
    return x, y, z, v_x, v_y, v_z

# Since these values are all constant for this assignment. I have commented these out to save time.
# Get the initial input
# v_0 = float(input("What is the magnitude of the initial velocity?: "))
# theta = float(input("What is the launch angle in degrees?: "))
#dt = float(input("What is the size of the time step?: "))
# m = float(input("What is the projectile mass?: ")) # golf ball ~ 0.04593 kg
# C = float(input("What is the drag coefficient?: ")) # golf ball ~ 4E-4 kg/m
# Break the initial velocity into components

v_x = v_0*math.cos(theta*math.pi/180)
v_y = v_0*math.sin(theta*math.pi/180)
v_z = 0
outFile = open("ProjectileCorData.txt", "w")
t = 0 # s
x = 0 # m
y = 0 
z = 0
y_max = 0 

inFlight = True
while(inFlight):
    a_x, a_y, a_z = acceleration(v_x, v_y, v_z, C, m)
    x, y, z, v_x, v_y, v_z = update(x, y, z, v_x, v_y, v_z, a_x, a_y, a_z, dt)
    t += dt
    if(y>= 0):
        outFile.write(str(t) + " " + str(x) + " " + str(y) + " " + str(z) + " " + str(v_x) +" " + str(v_y) + " " + str(v_z) + " " + str(a_x) + " " + str(a_y) + " " + str(a_z) + "\n")
        if(y > y_max):
            y_max = y
    else:
            inFlight = False
outFile.close()

print("Max Height: ", y_max)
print("Horizontal Range: ", x)


X = []
Y = []
Z = []
inFile = open("ProjectileCorData.txt", "r")
for line in inFile:
    t, x, y, z, v_x, v_y, v_z, a_x, a_y, a_z = line.split(" ")
    X.append(float(x))
    Y.append(float(y))
    Z.append(float(z))
inFile.close()
plt.xlabel("$x$ (m)")
plt.ylabel("$y$ (m)")
plt.plot(X, Y)
plt.show()
plt.xlabel("$x$ (m)")
plt.ylabel("$z$ (m)")
plt.plot(X, Z)
plt.show()