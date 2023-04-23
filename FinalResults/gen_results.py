import os
import sys
import argparse
import numpy as np
import glob
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()

parser.add_argument("-f", "--folder", help="Folder Name")


args = parser.parse_args()


results_folder = args.folder
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