import angr, claripy

proj = angr.Project("/bin/true", auto_load_libs=False)

state = proj.factory.entry_state()

a = state.solver.BVS('a', 64)
b = state.solver.BVS('b', 64)
c = state.solver.BVS('c', 64)


state.solver.add(a > 0)
state.solver.add(b > 0)
state.solver.add(c > 0)
state.solver.add(a < 10)
state.solver.add(b < 10)
state.solver.add(c < 10)


state.solver.add((a * 100 + b * 10 + c) * 3 == b * 111)

if state.solver.satisfiable():
    sol_a = state.solver.eval(a)
    sol_b = state.solver.eval(b)
    sol_c = state.solver.eval(c)

    print(f"a = {sol_a},b = {sol_b}, c = {sol_c}")
