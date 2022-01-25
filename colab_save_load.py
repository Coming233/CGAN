import torch
import os


def m_save_para(net_parameter, f_path, f_name):
    os.chdir(f_path)
    torch.save(net_parameter, f_name)


def m_load_para(net, f_path, f_name):
    os.chdir(f_path)
    temp = torch.load(f=f_name)
    return temp
