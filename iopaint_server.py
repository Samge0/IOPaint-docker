#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-06-03 18:25
# describe：iopaint的api服务，如果选择使用api方式调用iopaint，则需要先运行该服务

import subprocess
import argparse

def start_iopaint_server(device):
    """
    运行iopaint服务
    """
    model = "lama"
    host = "0.0.0.0"
    port = "8080"
    enable_interactive_seg = "--enable-interactive-seg"
    
    # 构建命令
    command = [
        "iopaint", "start",
        "--model={}".format(model),
        "--device={}".format(device),
        "--host={}".format(host),
        "--port={}".format(port),
        enable_interactive_seg,
        "--interactive-seg-device={}".format(device)
    ]
    
    # 运行命令
    process = subprocess.Popen(command)
    
    # 等待进程结束
    process.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Start iopaint server.')
    parser.add_argument('--device', type=str, required=True, help='Device to run the model on (e.g., cuda, cpu).')
    args = parser.parse_args()
    
    start_iopaint_server(args.device)
