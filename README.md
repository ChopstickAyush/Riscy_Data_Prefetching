# Riscy_Data_Prefetching

This code is developed and maintained by Ayush Agarwal(210050023), Sankalan Baidya(210050141) and Soham Joshi(2100510004) as a part of the CS230 Computer Architecture course project under professor Biswanandan Panda in the spring semester of the academic year 2022-23.

All the testing and implementation are done using [Champsim](https://github.com/ChampSim/ChampSim.git)

```
Instructions for generating results:

 $ Install Champsim using the above link
 $ Place your prefetchers in the prefetcher folder
 $ ./build_champsim.sh ${BRANCH} ${L1I_PREFETCHER} ${L1D_PREFETCHER} ${L2C_PREFETCHER} ${LLC_PREFETCHER} ${LLC_REPLACEMENT} ${NUM_CORE} 
 $ ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION] 

```

Our project was improving Data Prefetching technique for SPEC, SAT Solvers, Graph Analytics and Server traces. 
This work is built upon IPCP 1.0 by Biswa, which uses a bouquet of prefetchers. We are proposing a series of specialized improvements for different categories like Graphs, Sat-solvers, SPEC traces and Server workloads, leading to a prefetcher which performs at par or better than IPCP for most traces. The ideas used in this work have been built upon from the 2nd placed and 3rd placed, DPC3 prefetchers that is Bingo and MLOP. 

Link to the contest: https://dpc3.compas.cs.stonybrook.edu/?final_programs

We made Python scripts to generate data and evaluate results. Because of time limitations, we tested 13 SPEC traces, 10 graph traces, 6 sat traces, and 9 server traces.
All of them except sat was tested on WARMUPS = 20M and SIMS = 30M, and sat was tested on WARMUPS = 10M and SIMS = 10M. Our prefetcher showed massive improvements on graphs(sometimes 1.25x speedup compared to IPCP), minor improvements in server/sat and a slight decrease in the SPEC subset. 



| Traces  | Speed-up |
|---------|----------|
| GRAPH   | 1.072    |
| SAT     | 1.007    |
| SPEC    | 0.999    |
| SERVER  | 1.001    | 

