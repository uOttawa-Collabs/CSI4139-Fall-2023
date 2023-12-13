#!/usr/bin/env python

import angr
import sys
import claripy

def resolve_win(state):
    # if the bytes of "You in\n" are found in stdout it returns true
    return  b" You win !\n" in state.posix.dumps(1)



if __name__ == '__main__':
    print("starting...")
    p = angr.Project('./test2')
    arg1 = claripy.BVS('sym_arg', 8*4)  # maximum 4 * 8 bits

    state = p.factory.entry_state(args=['./test2', arg1])
    sm = p.factory.simgr(state)
    sm.explore(find=resolve_win)
    print("solution found")
    s = sm.found[0]
    print(s.posix.dumps(1)) # dump stdout

    # Print and eval the fist argument
    print("Arg1: ", s.solver.eval(arg1, cast_to=bytes))
