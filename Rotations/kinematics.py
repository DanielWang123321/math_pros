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

##useage
Roll=np.deg2rad(180)
Pitch=np.deg2rad(0)
Yaw=np.deg2rad(0)

ret=euler_to_rotation_matrix(Roll,Pitch,Yaw)
print(ret)
euler_rad=rotation_matrix_to_euler(ret)
print(euler_rad)
