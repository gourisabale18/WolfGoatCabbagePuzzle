from search import *
class WolfGoatCabbage(Problem):
    def __init__(self, initial_state=frozenset({'G', 'F', 'W', 'C'}), goal_state=set()):
        super().__init__(initial_state, goal_state)

    def goal_test(self, state):
            return state == self.goal

    def result(self, state, action):
        next_state = state + action
        return frozenset(next_state)

    def actions(self, state):
        if state == {'G', 'F', 'W', 'C'}:
            return [{'G','F'}]
        if state == {'W', 'C'}:
            return [{'F'}]
        if state == {'F', 'W', 'C'}:
            return [{'W','F'},{'C','F'}]
        if state == {'C'}:
            return [{'G','F'}]
        if state == {'W'}:
            return [{'G','F'}]
        if state == {'G', 'F', 'C'}:
            return [{'C','F'}]
        if state == {'G', 'F', 'W'}:
            return [{'W','F'}]
        if state == {'G'}:
            return [{'F'}]
        if state == {'G', 'F'}:
            return [{'G','F'}]

    def result(self, state, actions):
        new_state = set()
        for a in state:
            new_state.add(a)

        for b in actions:
            if b not in state:
                new_state.add(b)
            else:
                new_state.remove(b)

        return frozenset(new_state)

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
