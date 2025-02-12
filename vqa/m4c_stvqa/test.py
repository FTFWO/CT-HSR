import torch

# 假设 a 是你的张量，b 是你的目标张量
a = torch.rand((128, 50, 100))
b = torch.ones((128, 100))


# 在 b 的最后插入一个新的维度，将其变为 (24, 200, 1)
b_expanded = b.unsqueeze(-1)

# 使用 expand 函数将第三个维度的大小扩展为与 a 的第二个维度相同
b_expanded = b_expanded.expand(-1, -1, a.size(1))

# 在第三个维度上连接 b 和填充的零
adjusted_b = torch.cat([b_expanded, torch.zeros_like(b_expanded)], dim=-1)

# adjusted_b 现在是一个 (24, 200, 100) 的三维张量，其第二个维度大小与 a 相同

print(adjusted_b.shape)

padding_size = b.size(1) - a.size(0)

adjusted_a = torch.zeros(b.size(0), b.size(1), a.size(2))

# 将 a 的数据复制到 adjusted_a 中
adjusted_a[:, :a.size(1), :] = a



print(adjusted_a.shape)
print("*********************************************")