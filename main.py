from gets_logic import gets_sequentially as gs, gets_threads as gt, gets_processes as gp
from math_logic import math_sequentially as ms, math_threads as mt, math_processes as mp


if __name__ == '__main__':
    print('+ + + Start math tests of parallelism')
    ms.sequentially_function()
    mt.threading_function()
    mp.processes_function()
    print('+ + + Start gets tests of parallelism')
    gs.sequentially_function()
    gt.threading_function()
    gp.processes_function()
