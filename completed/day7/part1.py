import re

def count_bags_containing(lines):
    graph = generate_graph(lines)
    return traverse(graph, 'shiny gold')

# Every child node points to its parent
def generate_graph(lines):
    graph = {}
    for line in lines:
        parent_bag, child_bags = parse_input(line)

        if parent_bag not in graph:
            graph[parent_bag] = []

        for bag in child_bags:
            if bag['bag_type'] not in graph:
                graph[bag['bag_type']] = []
            graph[bag['bag_type']].append(parent_bag)
    return graph

def parse_input(line):
    parent_bag = re.sub(' bags', '', line[0])

    child_bags = re.sub(' bags| bag|[.]', '', line[1]).split(', ')
    if 'no other' in child_bags: child_bags.remove('no other')

    for i, bag in enumerate(child_bags):
        bag_type = re.sub('[0-9] ', '', bag)
        amount = int(bag.split()[0])
        child_bags[i] = {'bag_type': bag_type, 'amount': amount}

    return [parent_bag, child_bags]

def traverse(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while len(queue) != 0:
        curr_node = queue.pop(0)
        for neighbour in graph[curr_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return len(visited) - 1
