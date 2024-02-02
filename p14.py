import time

class NodeL:
    def __init__(self, identifier, information=None):
        self.identifier = identifier
        self.information = information
        self.successors = []  # Liste des successeurs
        self.predecessors = []  # Liste des prédécesseurs (pour un graphe orienté)

def constGraph1():
    # Création des nœuds
    node1 = NodeL("A", {"property": "value1", "other_property": 42})
    node2 = NodeL("B", {"property": "value2", "other_property": 56})
    node3 = NodeL("C", {"property": "value3", "other_property": 73})

    # Construction de la liste d'adjacence
    node1.successors = [node2, node3]
    node2.predecessors.append(node1)
    node2.successors.append(node3)
    node3.predecessors = [node1, node2]

    # Retourner la liste des nœuds
    return [node1, node2, node3]

def constGraph2():
    # Création des nœuds
    node1 = NodeL("X", {"property": "valueX", "other_property": 100})
    node2 = NodeL("Y", {"property": "valueY", "other_property": 200})
    node3 = NodeL("Z", {"property": "valueZ", "other_property": 300})

    # Construction de la liste d'adjacence
    node1.successors = [node2, node3]
    node2.predecessors.append(node1)
    node3.predecessors.append(node1)

    # Retourner la liste des nœuds
    return [node1, node2, node3]

# Utilisation des fonctions pour créer des exemples de graphes
graph1 = constGraph1()
graph2 = constGraph2()

# Affichage de la liste d'adjacence pour chaque graphe
print("Graph1:")
for node in graph1:
    print(f"Node {node.identifier}: Successors {[(n.identifier, n.information) for n in node.successors]}, " +
          f"Predecessors {[(n.identifier, n.information) for n in node.predecessors]}")

print("\nGraph2:")
for node in graph2:
    print(f"Node {node.identifier}: Successors {[(n.identifier, n.information) for n in node.successors]}, " +
          f"Predecessors {[(n.identifier, n.information) for n in node.predecessors]}")


def create_adjacency_matrix(nodes_list):
    # Utilisation de la liste de nœuds fournie
    num_nodes = len(nodes_list)

    # Initialisation de la matrice d'adjacence avec des zéros
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    # Mise à jour de la matrice d'adjacence en fonction des relations existantes entre les nœuds
    for node in nodes_list:
        for successor in node.successors:
            node_idx = nodes_list.index(node)
            successor_idx = nodes_list.index(successor)
            adjacency_matrix[node_idx][successor_idx] = 1
            adjacency_matrix[successor_idx][node_idx] = 1  # Ajoutez cette ligne pour un graphe non orienté

    return adjacency_matrix

# Utilisation de la fonction avec les graphes préparés
nodes_list1 = constGraph1()
nodes_list2 = constGraph2()
start_time = time.time()
adjacency_matrix1 = create_adjacency_matrix(nodes_list1)
end_time = time.time()
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour la création de la matrice d'adjacence : {execution_time:.2f} millisecondes")

adjacency_matrix2 = create_adjacency_matrix(nodes_list2)

# Affichage de la matrice d'adjacence
print("Adjacency Matrix 1:")
for row in adjacency_matrix1:
    print(row)

print("\nAdjacency Matrix 2:")
for row in adjacency_matrix2:
    print(row)


#####################################CREER UNE LISTE #############
def create_graph_list_from_input(nodes_list):
    # Utilisation de la liste de nœuds fournie
    num_nodes = len(nodes_list)

    # Mise à jour de la matrice d'adjacence en fonction des relations existantes entre les nœuds
    for node in nodes_list:
        for successor in node.successors:
            node.successors = [n for n in nodes_list if n.identifier == successor.identifier]
            successor.predecessors.append(node)

    return nodes_list

# Utilisation de la fonction avec les graphes préparés
nodes_list_input = create_graph_list_from_input(nodes_list1)
nodes_list_input2 = create_graph_list_from_input(graph2)

# Affichage de la liste d'adjacence
for node in nodes_list_input:
    print(f"Node {node.identifier}: Successors {[(n.identifier, n.information) for n in node.successors]}, " +
          f"Predecessors {[(n.identifier, n.information) for n in node.predecessors]}")
    
for node in nodes_list_input2:
    print(f"Node {node.identifier}: Successors {[(n.identifier, n.information) for n in node.successors]}, " +
          f"Predecessors {[(n.identifier, n.information) for n in node.predecessors]}")


###########################################


def calculate_graph_density(adjacency_matrix):
    num_nodes = len(adjacency_matrix)
    num_edges = sum(sum(row) for row in adjacency_matrix) // 2  # Divide by 2 for undirected graph
    max_possible_edges = (num_nodes * (num_nodes - 1)) // 2

    if max_possible_edges == 0:
        return 0  # Avoid division by zero for a graph with no edges

    density = num_edges / max_possible_edges
    return density



def calculate_graph_degree(adjacency_matrix):
    return [sum(row) for row in adjacency_matrix]



def is_eulerian_graph(adjacency_matrix):
    degrees = calculate_graph_degree(adjacency_matrix)
    odd_degrees = sum(1 for degree in degrees if degree % 2 == 1)
    return odd_degrees == 0 or odd_degrees == 2


def is_complete_graph(adjacency_matrix):
    num_nodes = len(adjacency_matrix)
    max_possible_edges = (num_nodes * (num_nodes - 1)) // 2
    num_edges = sum(sum(row) for row in adjacency_matrix) // 2  # Divide by 2 for undirected graph

    return num_edges == max_possible_edges


def is_tree(adjacency_matrix):
    num_nodes = len(adjacency_matrix)
    num_edges = sum(sum(row) for row in adjacency_matrix) // 2  # Divide by 2 for undirected graph

    return num_edges == num_nodes - 1


def search_node(graph_nodes, node_identifier):
    for node in graph_nodes:
        if node.identifier == node_identifier:
            return node
    return None



# Assuming adjacency_matrix1 and adjacency_matrix2 are the adjacency matrices for your graphs
start_time = time.time()
density1 = calculate_graph_density(adjacency_matrix1)
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")
density2 = calculate_graph_density(adjacency_matrix2)

start_time = time.time()
degree1 = calculate_graph_degree(adjacency_matrix1)
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")
density2 = calculate_graph_density(adjacency_matrix2)

start_time = time.time()
degree2 = calculate_graph_degree(adjacency_matrix2)
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")


start_time = time.time()
eulerian1 = is_eulerian_graph(adjacency_matrix1)
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")
eulerian2 = is_eulerian_graph(adjacency_matrix2)

start_time = time.time()
complete1 = is_complete_graph(adjacency_matrix1)
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")
complete2 = is_complete_graph(adjacency_matrix2)

start_time = time.time()
tree1 = is_tree(adjacency_matrix1)
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")
tree2 = is_tree(adjacency_matrix2)

# Assuming nodes_list_input is the list of nodes for your graph
node_a = search_node(nodes_list_input, "A")


# Printing the results
print("Graph 1:")
print(f"Density: {density1}")
print(f"Degree: {degree1}")
print(f"Eulerian: {eulerian1}")
print(f"Complete: {complete1}")
print(f"Tree: {tree1}")

print("\nGraph 2:")
print(f"Density: {density2}")
print(f"Degree: {degree2}")
print(f"Eulerian: {eulerian2}")
print(f"Complete: {complete2}")
print(f"Tree: {tree2}")

print("\nSearch for Node 'A' in the graph:")
if node_a:
    print(f"Node 'A' found with information: {node_a.information}")
else:
    print("Node 'A' not found in the graph.")



#########################################################################


def display_node_and_links(graph_nodes, node_identifier):
    node = search_node(graph_nodes, node_identifier)

    if node:
        print(f"Node {node.identifier}: {node.information}")
        print(f"Successors: {[n.identifier for n in node.successors]}")
        print(f"Predecessors: {[n.identifier for n in node.predecessors]}")
    else:
        print(f"Node {node_identifier} not found in the graph.")


def find_all_paths(graph_nodes, start_node_identifier, end_node_identifier, path=[]):
    start_node = search_node(graph_nodes, start_node_identifier)
    end_node = search_node(graph_nodes, end_node_identifier)
    path = path + [start_node]

    if start_node == end_node:
        return [path]

    if start_node not in graph_nodes:
        return []

    paths = []
    for node in start_node.successors:
        if node not in path:
            new_paths = find_all_paths(graph_nodes, node.identifier, end_node_identifier, path)
            for p in new_paths:
                paths.append(p)

    return paths



from queue import Queue

def shortest_path(graph_nodes, start_node_identifier, end_node_identifier):
    start_node = search_node(graph_nodes, start_node_identifier)
    end_node = search_node(graph_nodes, end_node_identifier)

    visited = set()
    queue = Queue()
    queue.put((start_node, [start_node]))

    while not queue.empty():
        current_node, path = queue.get()
        visited.add(current_node)

        for successor in current_node.successors:
            if successor not in visited:
                if successor == end_node:
                    return path + [successor]
                queue.put((successor, path + [successor]))

    return None



def find_connected_component(graph_nodes, start_node_identifier):
    start_node = search_node(graph_nodes, start_node_identifier)
    visited = set()

    def dfs(node, component):
        component.append(node)
        visited.add(node)

        for successor in node.successors:
            if successor not in visited:
                dfs(successor, component)

    component = []
    dfs(start_node, component)
    return component



def find_all_cycles(graph_nodes):
    cycles = []

    def dfs(node, path):
        if node in path:
            cycle = path[path.index(node):]
            cycles.append(cycle)
            return

        path.append(node)

        for successor in node.successors:
            dfs(successor, path.copy())

    for node in graph_nodes:
        dfs(node, [])

    return cycles




def add_node(graph_nodes, new_node):
    graph_nodes.append(new_node)
    return graph_nodes

def remove_node(graph_nodes, node_identifier):
    node = search_node(graph_nodes, node_identifier)

    if node:
        graph_nodes.remove(node)
        for other_node in graph_nodes:
            if node in other_node.successors:
                other_node.successors.remove(node)
            if node in other_node.predecessors:
                other_node.predecessors.remove(node)

    return graph_nodes



def add_link(graph_nodes, node_identifier1, node_identifier2):
    node1 = search_node(graph_nodes, node_identifier1)
    node2 = search_node(graph_nodes, node_identifier2)

    if node1 and node2:
        node1.successors.append(node2)
        node2.predecessors.append(node1)

    return graph_nodes




###################TESTER LES DERNIERES FONCTIONS#####################

# Create nodes
node_a = NodeL("A", {"property": "value1", "other_property": 42})
node_b = NodeL("B", {"property": "value2", "other_property": 56})
node_c = NodeL("C", {"property": "value3", "other_property": 73})

# Connect nodes
node_a.successors = [node_b, node_c]
node_b.predecessors.append(node_a)
node_b.successors.append(node_c)
node_c.predecessors = [node_a, node_b]

# Create graph
graph_nodes = [node_a, node_b, node_c]

# 1. Recherche d’un nœud a dans le graphe (afficher le nœud et ses liens)
start_time = time.time()
display_node_and_links(graph_nodes, "A")
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")



# 2. Recherche de tous les chemins entre un nœud a et un nœud b
start_time = time.time()
all_paths = find_all_paths(graph_nodes, "A", "C")
print("\nAll Paths between A and C:")
for path in all_paths:
    print([node.identifier for node in path])
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")

# 3. Recherche du chemin le plus court entre deux nœuds a et b
start_time = time.time()
shortest_path_result = shortest_path(graph_nodes, "A", "C")
print("\nShortest Path between A and C:")
print([node.identifier for node in shortest_path_result])
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")
# 4. Recherche d’une composante (fortement) connexe à partir d’un nœud a
start_time = time.time()
connected_component = find_connected_component(graph_nodes, "A")
print("\nConnected Component starting from A:")
print([node.identifier for node in connected_component])
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")
# 5. Trouver tous les cycles/circuits dans le graphe
start_time = time.time()
all_cycles = find_all_cycles(graph_nodes)
print("\nAll Cycles in the Graph:")
for cycle in all_cycles:
    print([node.identifier for node in cycle])
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")
# 6. Ajouter/Supprimer un nœud a avec ses liens
start_time = time.time()
new_node = NodeL("D", {"property": "value4", "other_property": 88})
graph_nodes = add_node(graph_nodes, new_node)
print("\nGraph after adding Node D:")
for node in graph_nodes:
    print(f"Node {node.identifier}: Successors {[n.identifier for n in node.successors]}")

graph_nodes = remove_node(graph_nodes, "A")
print("\nGraph after removing Node A:")
for node in graph_nodes:
    print(f"Node {node.identifier}: Successors {[n.identifier for n in node.successors]}")
execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")
# 7. Ajouter un lien (arc ou arête) entre deux nœuds existants
start_time = time.time()
graph_nodes = add_link(graph_nodes, "B", "D")
print("\nGraph after adding link between B and D:")
for node in graph_nodes:
    print(f"Node {node.identifier}: Successors {[n.identifier for n in node.successors]}")

execution_time = (end_time - start_time) * 1000  # Convertir en millisecondes
print(f"Temps d'exécution pour le calcul de la densité : {execution_time:.2f} millisecondes")



######################## le menu############ 
def afficher_menu():
    print("1. Construire un graphe")
    print("2. Affichage du graphe")
    print("3. calculer la densité du graphe")
    print("4. calculer le degré du graphe")
    print("5. Vérifier si le graphe est eulérien")
    print("6. Vérifier si le graphe est complet")
    print("7. Vérifier si le graphe est un arbre")
    print("8. Recherche d’un nœud a dans le graphe ")
    print("9.Recherche de tous les chemins entre un nœud a et un nœud b")
    print("10. Recherche du chemin le plus court entre deux nœuds a et b")
    print("11. Recherche d’une composante (fortement) connexe à partir d’un nœud a.")
    print("12. Trouver tous les cycles/circuits dans le graphe")
    print("13. Ajouter/ Supprimer un nœud a avec ses liens")
    print("14. Ajouter un lien (arc ou arête) entre deux nœuds existants")
    print("15. Quitter")
   

def option_1():
    print("Vous avez choisi l'option 1.")
    # Ajoutez le code correspondant à l'option 1 ici
    adjacency_matrix1 = create_adjacency_matrix(nodes_list1)
    print("Votre graphe a été créé! ")

def option_2():
    print("Vous avez choisi l'option 2.")
    # Ajoutez le code correspondant à l'option 2 ici
    print("Graph1:")
    for node in graph1:
         print(f"Node {node.identifier}: Successors {[(n.identifier, n.information) for n in node.successors]}, " +
               f"Predecessors {[(n.identifier, n.information) for n in node.predecessors]}")
    # Affichage de la matrice d'adjacence
    print("Adjacency Matrix 1:")
    for row in adjacency_matrix1:
          print(row)

    
    

def option_3():
    print("Vous avez choisi l'option 3.")
    # Ajoutez le code correspondant à l'option 3 ici
    density1 = calculate_graph_density(adjacency_matrix1)
    print(f"Density: {density1}")

def option_4():
    print("Vous avez choisi l'option 4.")
    # Ajoutez le code correspondant à l'option 4 ici
    degree1 = calculate_graph_degree(adjacency_matrix1)
    print(f"Degree: {degree1}")

def option_5():
    print("Vous avez choisi l'option 5.")
    # Ajoutez le code correspondant à l'option 5 ici
    eulerian1 = is_eulerian_graph(adjacency_matrix1)
    print(f"Eulerian: {eulerian1}")

def option_6():
    print("Vous avez choisi l'option 6.")
    # Ajoutez le code correspondant à l'option 6 ici
    complete1 = is_complete_graph(adjacency_matrix1)
    print(f"Complete: {complete1}")


def option_7():
    print("Vous avez choisi l'option 7.")
    # Ajoutez le code correspondant à l'option 7 ici
    tree1 = is_tree(adjacency_matrix1)
    print(f"Tree: {tree1}")


def option_8():
    print("Vous avez choisi l'option 8.")
    # Ajoutez le code correspondant à l'option 8 ici
    display_node_and_links(graph_nodes, "A")

def option_9():
    print("Vous avez choisi l'option 9.")
    # Ajoutez le code correspondant à l'option 9 ici
    all_paths = find_all_paths(graph_nodes, "A", "C")
    print("\nAll Paths between A and C:")
    for path in all_paths:
          print([node.identifier for node in path])


def option_10():
    print("Vous avez choisi l'option 10.")
    # Ajoutez le code correspondant à l'option 10 ici
    shortest_path_result = shortest_path(graph_nodes, "A", "C")
    print("\nShortest Path between A and C:")
    print([node.identifier for node in shortest_path_result])
    
def option_11():
    print("Vous avez choisi l'option 11.")
    # Ajoutez le code correspondant à l'option 11 ici
    connected_component = find_connected_component(graph_nodes, "A")
    print("\nConnected Component starting from A:")
    print([node.identifier for node in connected_component])

def option_12():
    all_cycles = find_all_cycles(graph_nodes)
    print("\nAll Cycles in the Graph:")
    for cycle in all_cycles:
          print([node.identifier for node in cycle])


def option_13():
    new_node = NodeL("D", {"property": "value4", "other_property": 88})
    graph_nodes = add_node(graph_nodes, new_node)
    print("\nGraph after adding Node D:")
    for node in graph_nodes:
          print(f"Node {node.identifier}: Successors {[n.identifier for n in node.successors]}")

    graph_nodes = remove_node(graph_nodes, "A")
    print("\nGraph after removing Node A:")
    for node in graph_nodes:
          print(f"Node {node.identifier}: Successors {[n.identifier for n in node.successors]}")


def option_14():
    graph_nodes = add_link(graph_nodes, "B", "D")
    print("\nGraph after adding link between B and D:")
    for node in graph_nodes:
          print(f"Node {node.identifier}: Successors {[n.identifier for n in node.successors]}")


    

# Boucle principale
while True:
    afficher_menu()
    choix = input("Entrez le numéro de votre choix : ")

    if choix == "1":
        option_1()
    elif choix == "2":
        option_2()
    elif choix == "3":
        option_3()
    elif choix == "4":
        option_4()
    elif choix == "5":
        option_5()
    elif choix == "6":
        option_6()
    elif choix == "7":
        option_7()
    elif choix == "8":
        option_8()
    elif choix == "9":
        option_9()
    elif choix == "10":
        option_10()
    elif choix == "11":
        option_11()
    elif choix == "12":
        option_12()
    elif choix == "13":
        option_13()
    elif choix == "14":
        option_14()
    elif choix == "15":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer un numéro valide.")
