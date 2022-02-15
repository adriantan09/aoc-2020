import re

def solution1(lines):
    graph = generate_graph(lines)
    return traverse(graph, 'shiny gold')

def generate_graph(lines):
    graph = {}
    for line in lines:
        parent_bag, child_bags = parse_input(line)

        if parent_bag not in graph:
            graph[parent_bag] = []

        for bag in child_bags:
            if bag not in graph:
                graph[bag] = []
            graph[bag].append(parent_bag)

    return graph

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

def parse_input(line):
    parent_bag = re.sub(' bags', '', line[0])

    child_bags = re.sub('[0-9] | bags| bag|[.]', '', line[1]).split(', ')
    if 'no other' in child_bags: child_bags.remove('no other')

    return [parent_bag, child_bags]