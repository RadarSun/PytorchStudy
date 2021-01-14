#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:37:40 2020

@author: apple
"""

# import torch
# import numpy as np
# np_data = np.arange(6).reshape((2,3))
# torch_data = torch.from_numpy(np_data)
# tensor2array = torch_data.numpy()
# print(
#     '\nnp_data\n',np_data,
#     '\ntnorch_data\n',torch_data,
#     '\ntensor2array\n',tensor2array,
# )


# import torch
# import numpy as np
# data = [[1,2],[3,4]]
# tensor = torch.FloatTensor(data)

# print(
#     '\nnumpy\n',np.matmul(data,data),
#     '\ntorch\n',torch.mm(tensor,tensor)
# )


import torch
import numpy as np
data = [[1,2],[3,4]]
tensor = torch.FloatTensor(data)
data = np.array(data)
print(
    '\nnumpy\n',data.dot(data),
    '\ntorch\n',torch.mm(tensor,tensor)
)
