# Riscy_Data_Prefetching

This code is developed and maintained by Ayush Agarwal(210050023), Sankalan Baidya(210050141) and Soham Joshi(2100510004) as a part of the CS230 -course project as a part of the spring semester of the academic year 2022-23.

All the testing and implementation are done using [Champsim](https://github.com/ChampSim/ChampSim.git)

Instructions for generating results:
<ol>
  <li>Install Champsim using the above link</li>
  <li>Place your prefetchers in the prefetcher folder</li>
  <li></li>
  <li>Fourth item</li>
</ol>

```
# Run simulation

Execute `run_champsim.sh` with proper input arguments. The default `TRACE_DIR` in `run_champsim.sh` is set to `$PWD/dpc3_traces`. <br>

* Single-core simulation: Run simulation with `run_champsim.sh` script.
```

```
Usage: ./run_champsim.sh [BINARY] [N_WARM] [N_SIM] [TRACE] [OPTION]
$ ./run_champsim.sh bimodal-no-no-no-no-lru-1core 1 10 400.perlbench-41B.champsimtrace.xz
${BINARY}: ChampSim binary compiled by "build_champsim.sh" (bimodal-no-no-lru-1core)
${N_WARM}: number of instructions for warmup (1 million)
${N_SIM}:  number of instructinos for detailed simulation (10 million)
${TRACE}: trace name (400.perlbench-41B.champsimtrace.xz)
${OPTION}: extra option for "-low_bandwidth" (src/main.cc)
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

