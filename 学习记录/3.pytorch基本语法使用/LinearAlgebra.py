import torch
#线性代数的基本实现
# 标量
x=torch.tensor([3.0])
y=torch.tensor([2.0])
x=torch.arange(4)
#向量长度
l_x=len(x)
print(l_x)

A=torch.arange(20).reshape(4,5)
print(f'A矩阵为\n{A}')
#矩阵的转置
A=A.T
print(f'A的转置矩阵为\n{A}')

B=torch.tensor([[1,2,3],[2,0,4],[3,4,5]])
# 矩阵与其转置矩阵相等说明是对称矩阵
print(B==B.T)

#和matlab不一样,pytorch中的A*B表示的是按元素乘
Z1=torch.arange(9).reshape(3,3)
Z2=torch.tensor([[9,8,7],[6,5,4],[3,2,1]])
Z3=Z1*Z2
print(Z3)

#指定求和张量的轴
X=torch.arange(24).reshape(2,3,4)
print(f'X=\n{X}')
X_sum_axis0 = X.sum(axis=0)
print(f'在0维度求和是\n{X_sum_axis0}\n它的形状是{X_sum_axis0.shape}')
X_sum_axis1 = X.sum(axis=1)
print(f'在1维度求和是\n{X_sum_axis1}\n它的形状是{X_sum_axis1.shape}')
X_sum_axis2 = X.sum(axis=2)
print(f'在2维度求和是\n{X_sum_axis2}\n它的形状是{X_sum_axis2.shape}')

#你也可以在求和时保留一下维度
X_SUM_div=X.sum(axis=0,keepdim=True)

#也可以在两个维度下求和
X_sum_axis01 = X.sum(axis=[0,1])
print(f'在0和1维度求和是\n{X_sum_axis01}\n它的形状是{X_sum_axis01.shape}')

#求和操作也是如此,不过呢,只有浮点型张量可以求平均值，你不能直接把整数给带进来
X_mean=X.float().mean()
print(f'全体平均值为{X_mean}')
#沿0方向求平均值
X_mean1=A.float().mean(axis=0)
print(f'沿0方向求平均值为\n{X_mean1}')


#
x=torch.arange(4,dtype=float)
y=torch.ones(4,dtype=float)
print(torch.dot(x,y))

A=torch.arange(12).reshape(3,4)
x=torch.tensor([3,1,2,4])
#A的每一行与b的每个标量点积
b=torch.mv(A,x)
print(A)
print(b)

C=torch.tensor([[1,2,3],[3,2,1]])
D=torch.tensor([[1,1],[2,2],[3,3]])
E=torch.mm(C,D)
print(E)