#!/usr/bin/python3

import os
import argparse
import graphviz

def main():
    parser = argparse.ArgumentParser(description = "CLI for graph visualization")
    parser.add_argument("-f","--file", type = str, nargs = 1, metavar = "file_name", default = None, help = "File which stores the graph")
    parser.add_argument("-d","--directed", action="store_true", help = "For directed graphs")
    parser.add_argument("-t","--tree", action="store_true", help = "For trees")
    parser.add_argument("-w","--weighted", action="store_true", help = "For weighted graphs")

    args = parser.parse_args()

    node_count, edge_count = 0, 0
    edgeList = []

    if args.file != None:
        # Read input from file
        file_name = args.file[0];
        input_file = open(file_name,"r")
        
        for line in input_file:
            line = line.split()
            if node_count == 0:
                if args.tree == True:
                    node_count = int(line[0])
                    edge_count = node_count - 1
                else:
                    node_count,edge_count = (int(i) for i in line)
                    
            elif args.weighted == True:
                edgeList.append((line[0], line[1], line[2]))
            else:
                edgeList.append((line[0],line[1]))
        
        input_file.close()

    else:
        # Read input from stdin
        if(args.tree == True):
            node_count = int(input())
            edge_count = node_count - 1
        else:
            node_count, edge_count = map(int, input().split())

        for _ in range(edge_count):
            if(args.weighted == True):
                u,v,w = input().split()
                edgeList.append((u,v,w))
            else:
                u,v = input().split()
                edgeList.append((u,v))
    
    
    # Build Graph
    if args.directed == True:
        graph = graphviz.Digraph('Graph')
    else:
        graph = graphviz.Graph('Graph')

    graph.format = 'png'

    for i in range(node_count):
        graph.node(str(i+1))
    
    if args.weighted == True:
        for u,v,w in edgeList:
            graph.edge(u,v,weight=w)
    else:
        for u,v in edgeList:
            graph.edge(u,v)

    output_directory = os.getcwd()
    graph.render(directory=output_directory)
    os.system('explorer.exe "Graph.gv.png"')

if __name__ == "__main__":
    main()


