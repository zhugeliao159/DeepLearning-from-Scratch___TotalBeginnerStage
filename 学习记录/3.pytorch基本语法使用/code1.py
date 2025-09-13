import torch
# 数据的操作
# 创建一个张量
x=torch.arange(12)
# print(x)
# 打印这个张量的形状
print(f"张量形状为{x.shape}")
# 打印这个张量的总数
print(f"张量总数为{x.numel()}")
# 数字和总数不变,改变形状
X=x.reshape(3,4)
print(f"将张量改变形状后变成\n{X}")
# 打印这个张量的形状
print(f"新张量形状为{X.shape}")

# 一些创建方法 和matlab差不多
torch.zeros((2,3,4))
torch.ones((2,3,4))
Y=torch.tensor([[2,1,4,3],[1,2,3,4],[4,3,2,1]])
print(Y.shape)

#一些对张量的基本操作+-*/指数
X1=torch.tensor([1.0,2,4,8])
X2=torch.tensor([2,2,2,2])
print(f"X1+X2={X1+X2}")
print(f"X1-X2={X1-X2}")
print(f"X1*X2={X1*X2}")
print(f"X1/X2={X1/X2}")
print(f"X1**X2={X1**X2}")
print(f"X1.exp={X1.exp()}")

#张量连结,默认是按列方向拼接的
X_Y=torch.cat((X,Y),dim=1)#dim=0按列拼接,dim=1按行拼接
print(X_Y)

#还可以构建逻辑张量
X_equal_Y=(X==Y)
print(X_equal_Y)

#张量求和
X_sum=X.sum()
print(X_sum)

#类似于matlab可以按行或者列延展进行运算
#现在有了专业术语叫做广播机制

a=torch.arange(3).reshape((3,1))
b=torch.arange(2).reshape((1,2))
print(f"广播机制演示:\n{a+b}")

#张量元素的访问
print(f"访问最后一个元素{X[-1]}")
# 这里的最后一个元素指的是张量的最后一个元素
# 也就是说一个一阶张量的最后一个元素
#有可能是一个数，有可能是一个向量，有可能是一个矩阵
print(f"访问最后一个元素\n{X[1:3]}")#py的一些基本操作了

#索引张量部分进行操作
X[:2]=12
print(X)

#id(X)类似于指针

#张量与向量/标量的转换
A=X.numpy()#把X张量对应对应的标量弄过来
a=torch.tensor([3.5])
b=a.item()#1*1的张量变成标量
