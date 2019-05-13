#!/usr/bin/env pipenv run python


from sapy import displmethod
from sapy import element
from sapy import gmsh
from sapy import structure
from sapy import plotter
import matplotlib.pyplot as plt


mesh_file = 'new_idea'

bound = {3: [1, 1],
         4: [0, 1]}

nodal_load = {1: [0.0, -750.0],
              2: [0.0, -750.0]}

ele = element.Data()
for i in range(10):
    ele.E[i] = 10.
    ele.A[i] = 10.
    ele.TYPE[i] = 'Truss'

mesh = gmsh.Parse(mesh_file)
model = structure.Builder(mesh, ele, bound)

U, Q = displmethod.solver(mesh, model, ele, nodal_load)

# plotter.undeformed(model)

plotter.axialforce(model, Q)
plt.show()
