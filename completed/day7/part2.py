from part1 import parse_input

def count_containing_bags(lines):
    graph = generate_graph(lines)
    return traverse(graph, 'shiny gold') - 1

# Every parent node points to its children
def generate_graph(lines):
    graph = {}
    for line in lines:
        parent_bag, child_bags = parse_input(line)
        graph[parent_bag] = child_bags
    return graph

def traverse(graph, curr_node):
    total = 1
    for neighbour in graph[curr_node]:
        n_bags = neighbour['amount']
        total += n_bags * traverse(graph, neighbour['bag_type'])

    return total

