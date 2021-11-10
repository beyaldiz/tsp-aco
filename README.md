# tsp-aco
Ant Colony Optimization for Traveling Salesman Problem

## Dependencies
- Python >3.8
- tqdm
- numpy
- matplotlib

To run the solver run main.py from the project directory as
```
python main.py --input data/{FILENAME}.tsp \
               --num-ants {NUM_ANTS} \
               --alpha {ALPHA_RANGE} \
               --beta {BETA_RANGE} \
               --evap-rate {EVAP_RATE} \
               --est-len {EST_LEN} \
               --num-iters {NUM_ITERS} \
               --plot-len \
               --plot-path
```

Example:
```
python main.py --input data/a280.tsp \
               --num-ants 10 \
               --alpha 1.0 3.0 \
               --beta 1.0 30.0 \
               --evap-rate 0.15 \
               --est-len 8000 \
               --num-iters 30 \
               --plot-len
```

Optional: To plot length over iterations add `--plot-len` and to plot the path add `--plot-path` to the arguments.

The data can be found at [tsplib](http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsplib.html)
