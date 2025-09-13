import os

os.makedirs(os.path.join('.','data'),exist_ok=True)
data_file=os.path.join('.','data','house_tiny.csv')
with open(data_file,'w') as f:
    f.write('NumRooms,Alley,Price\n') # 列名
    f.write('NA,Pave,127500\n') #每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')
        
import pandas as pd
data=pd.read_csv(data_file)
print(data)

inputs,outputs=data.iloc[:,0:2],data.iloc[:,2]
inputs=inputs.fillna(inputs.mean(numeric_only=True))


inputs=pd.get_dummies(inputs,dummy_na=True,dtype=int)
# inputs['Alley_Pave']=inputs['Alley_Pave'].astype(int)
# inputs['Alley_nan']=inputs['Alley_nan'].astype(int)
print(inputs)

import torch
#请注意张量中是不允许同时出现bool型和整型/浮点型的
#在上面的独热编码中如果你把类别转化为bool型，那就后续转换成int型
#要不热呢,你就一开始转换的时候就弄成int型
X,y=torch.tensor(inputs.values),torch.tensor(outputs.values)
print(f"X={X}")
print(f"y={y}")
