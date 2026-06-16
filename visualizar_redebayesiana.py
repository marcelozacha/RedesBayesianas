#Este exemplo cria uma rede simples representando a influência de Marketing Digital sobre Leads e Compras.
#!pip install networkx matplotlib pgmpy -q


import networkx as nx
import matplotlib.pyplot as plt

# Criando um grafo direcionado
G = nx.DiGraph()

# Adicionando nós
G.add_nodes_from([
    "Marketing Digital",
    "Leads",
    "Compra"
])

# Adicionando conexões
G.add_edges_from([
    ("Marketing Digital", "Leads"),
    ("Leads", "Compra")
])

# Configuração da figura
plt.figure(figsize=(8, 5))

# Layout automático
pos = nx.spring_layout(G, seed=42)

# Desenhando a rede
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=4000,
    font_size=10,
    arrows=True
)

plt.title("Rede de Influência em Marketing")
plt.show()

#saída: Marketing Digital → Leads → Compra