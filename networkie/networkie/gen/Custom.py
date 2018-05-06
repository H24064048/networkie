import networkx as nx
import pandas as pd



class LoadFromFile(object):
    def __init__(self):
        '''
        Initiate variables for the class.
        '''
        self.g = nx.Graph()

        pass

    def from_edgelist(self, path):
        '''
        Read graph in edgelist txt format from `path`.

        Parameters
        ----------
        path: `str`
            The path to the edgelist text file. Note that the node index must start from 0.

        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.

        '''

        edgelist = []
        with open(path, 'r') as f:
            for line in f:
                node_pair = line.replace('\n', '').split(' ')
                edgelist += [node_pair]
        self.g.add_edges_from(edgelist)
        print(nx.info(self.g))
        print('Edgelist txt data successfully loaded into a networkx Graph!')
        return self.g

    def from_in_class_network(self, path):  # This is Prob. 3-a.
        '''
        Write your code documentation here.  # This is Prob. 4-a.

        Parses the file to a Graph object
         --------
        Returns
        -------
        result: networkx.classes.graph.Graph
             Graph object
        '''
        df = pd.read_csv(path,delimiter='\t')
        dic = df.set_index('ID')['IDs-of-acquaintances'].to_dict()
        for i,j in dic.items():   #dic index + 對應內容   i -> key  j -> info
        	dic[i] = j.split(',')
        for i,j in dic.items():   #dic index + 對應內容   i -> key  j -> info
        	l=[]
        	for k in j:
        		if k != ' ':
        			l.append(int(k))
        	dic[i]=l
        self.g.add_nodes_from(dic.keys())
        for k,v in dic.items():
        	for z in v:
        		self.g.add_edge(k,z)
        return self.g

'''
Gra =nx.Graph()
Gra = LoadFromFile().from_in_class_network()
nx.draw(Gra)
plt.show()
'''