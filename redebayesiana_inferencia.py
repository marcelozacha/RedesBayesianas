#Neste exemplo, será calculada a probabilidade de uma pessoa realizar uma compra sabendo que ela clicou em um anúncio.
#usando pgmpy

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Estrutura da rede
modelo = DiscreteBayesianNetwork([
    ("Anuncio", "Clique"),
    ("Clique", "Compra")
])

# Probabilidade de visualizar um anúncio
cpd_anuncio = TabularCPD(
    variable="Anuncio",
    variable_card=2,
    values=[[0.4], [0.6]]
)

# Probabilidade de clicar dado o anúncio
cpd_clique = TabularCPD(
    variable="Clique",
    variable_card=2,
    values=[
        [0.8, 0.3],  # Não clica
        [0.2, 0.7]   # Clica
    ],
    evidence=["Anuncio"],
    evidence_card=[2]
)

# Probabilidade de compra dado o clique
cpd_compra = TabularCPD(
    variable="Compra",
    variable_card=2,
    values=[
        [0.9, 0.2],  # Não compra
        [0.1, 0.8]   # Compra
    ],
    evidence=["Clique"],
    evidence_card=[2]
)

# Adicionando CPDs ao modelo
modelo.add_cpds(
    cpd_anuncio,
    cpd_clique,
    cpd_compra
)

# Verificando consistência
print("Modelo válido:", modelo.check_model())

# Criando mecanismo de inferência
inferencia = VariableElimination(modelo)

# Probabilidade de compra sabendo que houve clique
resultado = inferencia.query(
    variables=["Compra"],
    evidence={"Clique": 1}
)

print("\nProbabilidade de Compra dado que houve Clique:")
print(resultado)


'''
Modelo válido: True

Probabilidade de Compra dado que houve Clique:
+-----------+---------------+
| Compra    |   phi(Compra) |
+===========+===============+
| Compra(0) |        0.2000 |
+-----------+---------------+
| Compra(1) |        0.8000 |
+-----------+---------------+

Nesse caso, a rede conclui que a probabilidade de compra é de 80% quando o usuário clicou no anúncio.
'''
