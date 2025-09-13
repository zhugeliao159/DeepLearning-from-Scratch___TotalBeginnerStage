****

**基础语法学习**

​		由于之前也没有python基础,学习起来确实比想象得多花了一些时间，不过问题不大。pytorch和matlab语法差不多,至少从矩阵操作方面看,前期理解起来不是太麻烦。

​	在pytorch中基本的操作元素是张量，我对它暂时的理解就是同一类型的数组，一些基本的张量创建方法如下:

`torch.zeros((2,3,4))`

`torch.ones((2,3,4))`

`Y=torch.tensor([[2,1,4,3],[1,2,3,4],[4,3,2,1]])`

`a=torch.arange(3).reshape((3,1))`

基本都是可以直接看懂的,这里的arrang(i)表示创建一个张量表示[0---i-1]

数据的读取,索引的使用以及赋值基本和matlab一样,那我昨天学了点啥,不是哥们,啥也没学啊

。。。。。明天开始一定不偷懒了

****

然后是今天的学习部分

学习了数据预处理，记得高三时在C++中尝试过文件操作,但是一直没有成功过

现在看py还挺轻松的,通过os库进行对csv文件的读写操作

`os.makedirs(os.path.join('.','data'),exist_ok=True)`创建路径,'.'表示在当前路径创建,'..'表示在上一路径下创建,exist_ok=True表示如果已经创建了这个路径给他覆盖掉

data_file=os.path.join('.','data','house_tiny.csv') 创建csv文件

`with open(data_file,'w') as f:`但看文件创建f对象进行写操作

  `f.write('NumRooms,Alley,Price\n') # 列名`

  `f.write('NA,Pave,127500\n') #每行表示一个数据样本`

  `f.write('2,NA,106000\n')`

  `f.write('4,NA,178100\n')`

  `f.write('NA,NA,140000\n')`

先对数据进行预处理，比如插值去Nan值,将类别变量变成数值变量

`inputs,outputs=data.iloc[:,0:2],data.iloc[:,2]`

`inputs=inputs.fillna(inputs.mean(numeric_only=True))`

`inputs=pd.get_dummies(inputs,dummy_na=True,dtype=int)`

然后需要注意的是张量一定是同类型的,你不能把一个既有bool型又有浮点型的数组转换成张量

在学习这些之后，看了一下张量的操作，基本就是求和求平均值，向量点积，矩阵乘法

`x=torch.arange(4,dtype=float)`

`y=torch.ones(4,dtype=float)`

`print(torch.dot(x,y))`

`A=torch.arange(12).reshape(3,4)`

`x=torch.tensor([3,1,2,4])`

`\#A的每一行与b的每个标量点积`

`b=torch.mv(A,x)`

`print(A)`

`print(b)`

`\# 矩阵的乘法`

`C=torch.tensor([[1,2,3],[3,2,1]])`

`D=torch.tensor([[1,1],[2,2],[3,3]])`

`E=torch.mm(C,D)`

`print(E)`

额，确实啥也没学哈哈哈哈，今天心情不太好有点乱，再加上还有算法要刷，找个借口

明天一定一定开始好好学