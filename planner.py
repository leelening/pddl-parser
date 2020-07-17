#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from PDDL import PDDL_Parser
import pickle


def convert(list):
    return tuple(tuple(i) for i in list)


class Planner:

    #-----------------------------------------------
    # Solve
    #-----------------------------------------------

    def solve(self, domain, problem):
        # Parser
        parser = PDDL_Parser()
        parser.parse_domain(domain)
        parser.parse_problem(problem)
        # Parsed data
        state = parser.state
        goal_pos = parser.positive_goals
        goal_not = parser.negative_goals
        # Do nothing
        if self.applicable(state, goal_pos, goal_not):
            return []
        # Grounding process
        ground_actions = []
        for action in parser.actions:
            for act in action.groundify(parser.objects):
                ground_actions.append(act)
        # Search
        visited = [state]
        transitions = dict()
        while visited:
            state = visited.pop(0)
            transitions[convert(state)] = dict()
            for act in ground_actions:
                if self.applicable(state, act.positive_preconditions, act.negative_preconditions):
                    new_state = self.apply(state, act.add_effects, act.del_effects)
                    if new_state not in visited:
                        if self.applicable(new_state, goal_pos, goal_not):
                            return transitions
                        visited.append(new_state)
                        transitions[convert(state)][act.name] = new_state
        return None

    #-----------------------------------------------
    # Applicable
    #-----------------------------------------------

    def applicable(self, state, positive, negative):
        for i in positive:
            if i not in state:
                return False
        for i in negative:
            if i in state:
                return False
        return True

    #-----------------------------------------------
    # Apply
    #-----------------------------------------------

    def apply(self, state, positive, negative):
        new_state = []
        for i in state:
            if i not in negative:
                new_state.append(i)
        for i in positive:
            if i not in new_state:
                new_state.append(i)
        return new_state

# ==========================================
# Main
# ==========================================
if __name__ == '__main__':
    import sys, time
    start_time = time.time()
    domain = sys.argv[1]
    problem = sys.argv[2]
    # domain = 'examples/attackgraph/domain.pddl'
    # problem = 'examples/attackgraph/problem.pddl'
    planner = Planner()
    transitions = planner.solve(domain, problem)
    print('\nThe total number of states: ', '\t\t', len(transitions.keys()))
    print('\nTime: ','\t\t', str(time.time() - start_time) + 's')

    # count the transitions
    edge_count = 0
    for s in transitions:
        for a in transitions[s]:
            n_s = transitions[s][a]
            edge_count+=1
    print('\nThe total number of transitions: ', '\t\t', edge_count)


    with open('transitions.pickle', 'wb') as handle:
        pickle.dump(transitions, handle, protocol=pickle.HIGHEST_PROTOCOL)
