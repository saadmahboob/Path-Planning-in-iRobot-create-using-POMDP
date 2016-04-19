__author__ = 'Johny Kannan'

import CreateRobot.myRobot as model
import CreateRobot as funcs
import numpy as np


state = [ model.State(None, None, None, None) for i in range(0, 10) ]


graph = model.PomdpGraph(5,4)

graph.make_block(1,2)

graph.re_graph()


for y in range(0,graph.dimension['breadth']):
    for x in range(0,graph.dimension['length']):
        if graph.get_state(x,y).left_state is None:
            print('L',end='')
        if graph.get_state(x,y).top_state is None:
            print('T',end='')
        if graph.get_state(x,y).right_state is None:
            print('R',end='')
        if graph.get_state(x,y).bottom_state is None:
            print('D',end='')
        print('\t',end='')
    print()

graph.normalize()
# array = np.array([graph.states[i].belief for i in range(len(graph.states))]).reshape(graph.dimension['breadth'], graph.dimension['length'])
# print(array)
funcs.print_graph_belief(graph)

action = {'Left': True, 'Right': False, 'Up': False, 'Down': False}
evidence = {'Left': 0.0,'Right': 0.0,'Up': 0.0,'Down': 0.0,'Center': 1.0}
graph.update_beliefs(action)
#graph.normalize()
graph.update_evidence(evidence)
graph.normalize()
funcs.print_graph_belief(graph)

action = {'Left': True, 'Right': False, 'Up': False, 'Down': False}
evidence = {'Left': 1.0,'Right': 0,'Up': 0,'Down': 0,'Center': 0.0}
graph.update_beliefs(action)
graph.update_evidence(evidence)

graph.normalize()
funcs.print_graph_belief(graph)

action = {'Left': False, 'Right': False, 'Up': False, 'Down': True}
evidence = {'Left': 0,'Right': 0,'Up': 0,'Down': 1,'Center': 0}
graph.update_beliefs(action)
graph.update_evidence(evidence)
graph.normalize()
funcs.print_graph_belief(graph)

action = {'Left': True, 'Right': False, 'Up': False, 'Down': False}
evidence = {'Left': 0,'Right': 0,'Up': 0,'Down': 1,'Center': 0}
graph.update_beliefs(action)
graph.normalize()
funcs.print_graph_belief(graph)

action = {'Left': True, 'Right': False, 'Up': False, 'Down': False}
evidence = {'Left': 0,'Right': 0,'Up': 0,'Down': 1,'Center': 0}
graph.update_beliefs(action)
graph.normalize()
funcs.print_graph_belief(graph)


# action = {'Left': False, 'Right': False, 'Up': True, 'Down': False}
# evidence = {'Left': 1,'Right': 0,'Up': 0,'Down': 0,'Center': 0}
# graph.update_beliefs(action)
# graph.update_evidence(evidence)
# graph.normalize()
# funcs.print_graph_belief(graph)
#
# action = {'Left': False, 'Right': False, 'Up': True, 'Down': False}
# evidence = {'Left': 1,'Right': 0,'Up': 0,'Down': 0,'Center': 0}
# graph.update_beliefs(action)
# graph.update_evidence(evidence)
# graph.normalize()
# funcs.print_graph_belief(graph)
#
# action = {'Left': False, 'Right': False, 'Up': True, 'Down': False}
# evidence = {'Left': 1,'Right': 0,'Up': 0,'Down': 0,'Center': 0}
# graph.update_beliefs(action)
# graph.update_evidence(evidence)
# graph.normalize()
# funcs.print_graph_belief(graph)

