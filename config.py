import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

input_nbr = 3
imsize = 128
batch_size = 64
lr = 0.0001
patience = 50
start_epoch = 200
epochs = 300
print_freq = 10
save_folder = 'models'
