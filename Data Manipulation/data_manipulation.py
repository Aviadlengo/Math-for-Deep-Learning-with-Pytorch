#%%
import torch
torch.cuda.is_available()
# %%
import os
os.getcwd()
# %%
print(dir(torch.distributions))

# %%
os.makedirs(os.path.join('..', 'data'), exist_ok=True)
data_file=os.path.join('..', 'data','house_tiny.csv')
# %%
with open (data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')  # Column names
    f.write('NA,Pave,127500\n')  # Each row represents a data example
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

# %%
import pandas as pd 
data=pd.read_csv(data_file)
print(data)
# %%
