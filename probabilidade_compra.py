# Probabilidades iniciais
historico = {
    "Sim": 0.30,
    "Nao": 0.70
}

tempo_site = {
    "Pouco": 0.50,
    "Medio": 0.30,
    "Muito": 0.20
}

promocao = {
    "Sim": 0.40,
    "Nao": 0.60
}

# Tabela Condicional P(Compra | Historico, Tempo, Promocao)
compra = {
    ("Sim", "Muito", "Sim"): 0.95,
    ("Sim", "Medio", "Sim"): 0.85,
    ("Sim", "Pouco", "Sim"): 0.70,

    ("Nao", "Muito", "Sim"): 0.65,
    ("Nao", "Medio", "Sim"): 0.50,
    ("Nao", "Pouco", "Sim"): 0.30,

    ("Sim", "Muito", "Nao"): 0.75,
    ("Sim", "Medio", "Nao"): 0.60,
    ("Sim", "Pouco", "Nao"): 0.40,

    ("Nao", "Muito", "Nao"): 0.30,
    ("Nao", "Medio", "Nao"): 0.15,
    ("Nao", "Pouco", "Nao"): 0.05
}


# Função para calcular a probabilidade de compra com base no histórico, tempo e promoção, 
# chances de compra
def calcular_probabilidade_compra( historico_cliente, tempo_cliente, promocao_cliente ):
        return compra[(historico_cliente, tempo_cliente, promocao_cliente )]

# Função para calcular a probabilidade conjunta P(Historico, Tempo, Promocao, Compra)
# chances de encontrar um cliente com esse perfil
def probabilidade_conjunta( historico_cliente, tempo_cliente, promocao_cliente ):
    probabilidade_historico = historico[historico_cliente]
    probabilidade_tempo     = tempo_site[tempo_cliente]
    probabilidade_promocao  = promocao[promocao_cliente]

    probabilidade_compra = compra[(historico_cliente, tempo_cliente, promocao_cliente)]
            
    return probabilidade_historico * probabilidade_tempo * probabilidade_promocao * probabilidade_compra


# Função para analisar um cliente específico e imprimir a probabilidade de compra
def analisar_cliente(historico_cliente, tempo_cliente, promocao_cliente):
    probabilidade = calcular_probabilidade_compra(historico_cliente, tempo_cliente, promocao_cliente)

    print("\n===== ANALISE DO CLIENTE =====")
    print(f"Historico:  {historico_cliente}")
    print(f"Tempo Site: {tempo_cliente}")
    print(f"Promocao:   {promocao_cliente}")

    print(f"\nProbabilidade de Compra: {probabilidade:.0%}")
    print(f"Probabilidade de Nao Comprar: {(1-probabilidade):.0%}")


#Exemplo 1
# Se eu encontrar um cliente com essas características, qual a chance dele comprar?
# 100 clientes iguais
# ↓
# 5 compram
# 95 não compram
analisar_cliente(
    historico_cliente="Sim",
    tempo_cliente="Muito",
    promocao_cliente="Sim"
)

#Exemplo 2
analisar_cliente(
    historico_cliente="Nao",
    tempo_cliente="Pouco",
    promocao_cliente="Nao"
)


#Exemplo 3
# Aqui a pergunta é diferente: Qual a chance de encontrar no mundo um cliente que satisfaça TODAS essas condições ao mesmo tempo?
# Já comprou antes
# E
# Ficou muito tempo no site
# E
# Clicou na promoção
# E
# Comprou novamente

resultado = probabilidade_conjunta(
    "Sim",
    "Muito",
    "Sim"
)

print(f"Probabilidade conjunta: {resultado*100:.2f}%")