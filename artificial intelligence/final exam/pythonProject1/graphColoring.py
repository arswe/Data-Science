colors = ["red", "green", "blue", "yellow", "orange", "purple"]

states = ["A", "B", "C", "D", "E", "F", "G"]

neighbors = {}
neighbors["A"] = ["B", "C"]
neighbors["B"] = ["A", "C", "D", "E"]
neighbors["C"] = ["A", "B", "D", "F"]
neighbors["D"] = ["B", "C", "E", "F"]
neighbors["E"] = ["B", "D", "G"]
neighbors["F"] = ["C", "D", "G"]
neighbors["G"] = ["E", "F"]

colors_of_states = {}


def find_color_for_state(state, color):
    for i in neighbors.get(state):
        neighbors_color = colors_of_states.get(i)
        if neighbors_color == color:
            return False
    return True

def get_color_for_state(state):
    for j in colors:
        if find_color_for_state(state, j):
            return j

def main():
    for k in states:
        colors_of_states[k] = get_color_for_state(k)
    print(colors_of_states)

main()