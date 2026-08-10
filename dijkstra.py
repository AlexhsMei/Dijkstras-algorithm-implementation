# στην λιστα li υπαρχουν σε tuples τα edges με τα weights τους αν θελετε να την χρησιμοποιησετε
# παιρνετε τα nodes του γραφου με το G.nodes
# παιρνετε τα edges του γραφου με το G.edges

import networkx as nx
import matplotlib as plt
import random

G = nx.Graph()
li = [(0, 0), (0, 0)]  # τα στοιχεια που εχει ειναι για να μη βγαζει ενα error δεν χρησιμευουν καπου
weight = 0

for i in range(14):
    weight = random.randint(1, 7)
    x = random.randint(1, 8)
    y = random.randint(1, 8)

    if x != y and (not any((i[:2] == (f'v{x}', f'v{y}') or i[:2] == (f'v{y}', f'v{x}')) for i in
                           li)):  # εδω ελεγχει αν υπαρχει ηδη το edge για να μην το βαλει διπλο
        li.append((f'v{x}', f'v{y}', weight))
    else:
        continue

del li[0:2]  # σβηνει τα δυο αρχικα μηδενικα tuples


# εδω φτιαχνει λεξικο με κλειδια τα edges και τιμες τα weights(αποστασεις) της λιστας li
dic = {}
for i in li:
    dic[i[:2]] = i[2]

edges = [i[:2] for i in li]

G.add_edges_from(edges)

pos = nx.spring_layout(G)

# με αυτα τον ζωγραφιζει
nx.draw_networkx_nodes(G, pos, node_size=400)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black', width=2)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=dic)
plt.pyplot.show()

for i in li:
    dic[i[1::-1]] = i[2]


# οριζει τον γραφο, την αρχη και το τελος του
class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.start = input('Ορισε την αρχη του γραφου: ')
        self.end = input(f'Ορισε το τελος του γραφου (η αρχη ειναι το {self.start}): ')
        self.dict = {}
        for node in self.graph.nodes:
            if node != self.start:
                self.dict[node] = ['-', float(
                    'inf')]  # εδω φτιαχνει λεξικο με (-,inf) για καθε node και (-,0) για αυτο που οριζουμε ως αρχη
            else:
                self.dict[node] = ['-', 0]
        self.unvisited_nodes = [x for x in self.graph.nodes]  # μπαινουν ολα στην λιστα αφου δεν εχουν επισκεφτει ακομα
        self.current_node = self.start
        while self.unvisited_nodes:
            self.neighbor_list = [n for n in self.graph.neighbors(
                self.current_node)]  # λιστα που περιεχει καθε φορα τους γειτωνες του current_node
            for neighbor in self.graph.neighbors(
                    self.current_node):  # αλλαγη της αποστασης των γειτωνων του current_node απο την αρχη
                temporary_value = self.dict[self.current_node][1] + dic[(str(self.current_node), str(neighbor))]
                if temporary_value < self.dict[neighbor][1]:
                    self.dict[neighbor][
                        1] = temporary_value  # αντικαθιστα τις παυλες σε καθε node με το προηγουμενο node (δηλαδη αποθηκευει την διαδρομη)
                    self.dict[neighbor][0] = self.current_node
            self.unvisited_nodes.remove(self.current_node)
            self.nearest_node()
        self.print_shortest_distance()
        nx.draw_networkx_nodes(G, pos, node_size=400)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black', width=2)
        nx.draw_networkx_edges(G, pos, edgelist=self.path_edges, edge_color='red', width=2)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=dic)
        plt.pyplot.show()

    def nearest_node(self):  # μεθοδος που οριστικοποιει καθε φορα το κοντινοτερο node και το επιστρεφει
        temp_dict = {}
        for node in self.unvisited_nodes:
            temp_dict[node] = self.dict[node][1]
        try:
            self.current_node = min(temp_dict, key=temp_dict.get)
        except ValueError:
            pass
        return self.current_node

    def print_shortest_distance(self):
        path = []
        node = self.end
        while node != self.start:
            path.append(node)
            node = self.dict[node][0]
        path.append(self.start)
        print('-->'.join(reversed((path))))
        # λιστα με τα nodes του μονοπατιου χρησιμευει στον χρωματισμο του μονοπατιου πανω στον γραφο
        self.path_edges = []
        for i in range(len(path) - 1):
            self.path_edges.append((path[i], path[i + 1]))


if __name__ == '__main__':
    Dijkstra(G)