/Applications/Blender\ 4.0.app/Contents/MacOS/Blender '/Users/dufok/Projects/ASAP/WEY/Model/WEY_LOUNG_4.blend'  --background --python /Users/dufok/Projects/ASAP/WEY/Model/background_renred_loung_scene.py


ubuntu@gc-charming-merkle:~$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Thu_Nov_18_09:45:30_PST_2021
Cuda compilation tools, release 11.5, V11.5.119
Build cuda_11.5.r11.5/compiler.30672275_0
ubuntu@gc-charming-merkle:~$ nvidia-smi
Wed Feb  7 18:10:20 2024       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.154.05             Driver Version: 535.154.05   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3080        On  | 00000000:00:05.0 Off |                  N/A |
|  0%   24C    P8               6W / 320W |      1MiB / 10240MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
|   1  NVIDIA GeForce RTX 3080        On  | 00000000:00:06.0 Off |                  N/A |
|  0%   22C    P8               2W / 320W |      1MiB / 10240MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
ubuntu@gc-charming-merkle:~$ 