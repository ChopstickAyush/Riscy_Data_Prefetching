import os
import sys
import argparse
import numpy as np
import glob
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()

parser.add_argument("-t", "--traces", help="Traces Folder")
parser.add_argument("-w", "--warm", help="No of Warmups", type = int)
parser.add_argument("-s", "--sim", help="No of Sims", type= int)


args = parser.parse_args()

# os.system("./build_champsim.sh bimodal no ipcp ipcp ipcp lru 1")
# os.system("./build_champsim.sh bimodal no ipcp_o ipcp ipcp lru 1")
# os.system("./build_champsim.sh bimodal no mlop next_line next_line lru 1")

traces_folder = args.traces
traces = []
for file in glob.glob(traces_folder + "/*.xz"):
    traces.append(file.split("/")[-1])

for i in traces:
    os.system(f"./run_champsim.sh bimodal-no-ipcp-ipcp-ipcp-lru-1core {args.warm} {args.sim} {i}")
    os.system(f"./run_champsim.sh bimodal-no-ipcp_o-ipcp-ipcp-lru-1core {args.warm} {args.sim} {i}")
    #os.system(f"./run_champsim.sh bimodal-no-mlop-next_line-next_line-lru-1core {args.warm} {args.sim} {i}")


results_folder = f"results_{args.sim}M"
os.system("rm results.out")
for file in glob.glob(results_folder + "/*.txt"):
    filename = file.split("/")[-1]
    os.system(f''' echo File name is: {filename} >> results.out  ''' )
    os.system(f''' cat {file} | grep "CPU 0 cumulative IPC" >> results.out ''')
    os.system(f''' cat {file} | grep "L1D PREFETCH  ACCESS" >> results.out ''')
    os.system(f''' cat {file} | grep "L1D PREFETCH  REQUESTED" >> results.out ''')
    os.system(f''' cat {file} | grep "L2C PREFETCH  ACCESS" >> results.out ''')
    os.system(f''' cat {file} | grep "L2C PREFETCH  REQUESTED" >> results.out ''')
    os.system(f''' cat {file} | grep "LLC PREFETCH  ACCESS" >> results.out ''')
    os.system(f''' cat {file} | grep "LLC PREFETCH  REQUESTED" >> results.out ''')
    



