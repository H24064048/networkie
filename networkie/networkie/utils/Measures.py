import pandas as pd

def compute_num_triangles(Gra):  # This is Prob. 3-e.
    '''
    Write your code documentation here.  # This is Prob. 4-a.

    Parameters
    ----------
    Gra: "networkx.classes.graph.Graph"
        the Graph object
    
    Returns
    -------
    result: "int"
        how much triangle exists in the graph
    
    '''
    def choose_2(data,i):  #選兩個點起來組對
        result=[]
        data1=list(data[i])
        while data1:
            a = data1.pop(-1)
            for m in data1:
                result.append((a,m))  #[(1,58)] [(2,56),(2,34),(2,25)]
        return result

    Graph=Gra.copy() #確定degree>2
    graph_changed=True
    while graph_changed:
        graph_changed=False
        for nodes , degree in list(Gra.degree):
            if degree<2:
                Gra.remove_node(nodes)
                graph_changed=True

    numbers_of_triangle=0 #calculate number of traingle
    for i in list(Graph):
        for j,k in choose_2(Graph,i):
            if j in Graph[k]:
                numbers_of_triangle+=1
        Graph.remove_node(i)
    return numbers_of_triangle
    return


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self, G):  # This is Prob. 3-d.   # the function aims to create a list which contains the degrees of each node.
        '''
        Write your code documentation here.  # This is Prob. 4-a.

        Parameters
        -----------
        G: "networkx.classes.graph.Graph"
            the Graph object

        Returns
        --------
        l: "list"
            a list with degrees of each node

        '''
        l = []
        for i in range(G.order()):
            l.append(G.degree(i))

        return l

 









