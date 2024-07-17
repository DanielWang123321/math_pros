import numpy as np


def rotation_matrix_to_euler(R):
    a=np.arctan2(R[2,1],R[2,2])
    b=np.arcsin(-R[2,0])
    c=np.arctan2(R[1,0],R[0,0])
    return a,b,c

def euler_to_rotation_matrix(a,b,c):
# a,b,c is Roll, Pitch, Yaw
    Rx=np.array([[1,0,0],
                 [0,np.cos(c),-np.sin(c)],
                 [0,np.sin(c),np.cos(c)]
                 ])
    Ry=np.array([[np.cos(b),0,np.sin(b)],
                 [0,1,0],
                 [-np.sin(b),0,np.cos(b)]
                 ])
    Rz=np.array([[np.cos(a),-np.sin(a),0],
                 [np.sin(a),np.cos(a),0],
                 [0,0,1]
                 ])

    R=np.dot(Rz,np.dot(Ry,Rx))
    return R



def quaternion_to_euler(q):
    # w,x,y,z is quaternion, w²+x²+y²+z²=1
    # a,b,c is Roll, Pitch, Yaw

    w,x,y,z=q
    a = np.arctan2(2.0 * (w * z + x * y), 1.0 - 2.0 * (y * y + z * z))


    sin_theta = 2.0 * (w * y - z * x)
    if np.abs(sin_theta) >= 1:
        b = np.sign(sin_theta) * np.pi / 2  # use 90 degrees if out of range
    else:
        b = np.arcsin(sin_theta)


    c = np.arctan2(2.0 * (w * x + y * z), 1.0 - 2.0 * (x * x + y * y))
    return a, b, c



def euler_to_quaternion(a, b, c):
    cy = np.cos(a * 0.5)
    sy = np.sin(a * 0.5)
    cp = np.cos(b * 0.5)
    sp = np.sin(b * 0.5)
    cr = np.cos(c * 0.5)
    sr = np.sin(c * 0.5)

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return np.array([w, x, y, z])



##useage
Roll=np.deg2rad(180)
Pitch=np.deg2rad(0)
Yaw=np.deg2rad(0)

ret=euler_to_rotation_matrix(Roll,Pitch,Yaw)
print(ret)
euler_rad=rotation_matrix_to_euler(ret)
print(euler_rad)
