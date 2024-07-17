
## 1. 二维空间
![图一](../Resources/2d_rotation.png)

二维坐标系中，向量OP旋转β得到P' \

x'=OP*cos(α+β)=OP \
y'=OP*sin(α+β)

OP的长度为l，OP'的长度也为l
P的坐标为(x,y), 其中\
x=l* cos(β)\
y=l* sin(β)

P'的坐标为(x',y') \
x'=l* cos(α+β)=l*[cos(α)*cos(β)+sin(α)*sin(β)]=l*cos(β)*cos(α)+l*sin(β)*sin(α)=x*cos(α)+y*sin(α)
\
y=l* sin(α+β)=l*[sin(α)*cos(β)+cos(α)*sin(β)]=l*cos(β)*sin(α)+l*sin(β)*cos(α)=x*sin(α)+y*cos(α)

所以P'的坐标可以表示为\
P'=(x*cos(α)+y*sin(α),x*sin(α)+y*cos(α))

P'的坐标使用矩阵表示为


P' = \[
\begin{bmatrix}
x & y
\end{bmatrix}
\begin{bmatrix}
\cos(\beta) & \sin(\beta) \\
-\sin(\beta) & \cos(\beta)
\end{bmatrix}
\]


以上可以得出，二维直角坐标系内的点P(x,y)绕原点逆时针旋转角度θ，得到点P' (x',y')，可以表示为点A左乘旋转矩阵R(θ)得到点B.
其中旋转矩阵

R(\theta) = \[
\begin{bmatrix}
\cos(\theta) & -\sin(\theta) \\
\sin(\theta) & \cos(\theta)
\end{bmatrix}
\]

## 三维空间
**定义：**

旋转矩阵（rotation matrix），是一个正交矩阵，即满足：
$$
R R^{T}=I \text { 且 } \operatorname{det}(R)=1
$$

**欧拉角：**

欧拉角描述了一个三维空间中的刚体从一个固定参考系的位置到一个新位置的三个旋转角度。常用的旋转顺序有 Z-Y-X、X-Y-Z 等。
对于 Z-Y-X 顺序，欧拉角定义为：
$$
R(\alpha, \beta, \gamma)=\begin{bmatrix}
    \cos \alpha \cos \beta & \cos \alpha \sin \beta \sin \gamma - \sin \alpha \cos \gamma & \cos \alpha \sin \beta \cos \gamma + \sin \alpha \sin \gamma \\
    \sin \alpha \cos \beta & \sin \alpha \sin \beta \sin \gamma + \cos \alpha \cos \gamma & \sin \alpha \sin \beta \cos \gamma - \cos \alpha \sin \gamma \\
    -\sin \beta & \cos \beta \sin \gamma & \cos \beta \cos \gamma
\end{bmatrix}
$$




