# Redes Bayesianas

##Principais conceitos de uma Rede Bayesiana:
- probabilidades a priori,
- tabela condicional (CPT),
- inferência simples e cálculo de probabilidade conjunta

**Usando apenas dicionários e funções Python.**

baseado em:
- Histórico de compras
- tempo no site
- interação com promoção

**objetivo: prever se o cliente irá comprar ou não um produto **

'tabela condicional P(Compra | Historico, Tempo, Promocao)'

Observação importante:

**Qual é mais importante probabilidade de compra ou probalidade conjunta?**

**Para prever vendas: **

**Probabilidade de Compra é muito mais útil.**

Exemplo:

Cliente entrou no site.

Você observa:
- Histórico = Sim
- Tempo = Muito
- Promoção = Sim

Pergunta: Ele vai comprar?
Resposta: 95%

**A probabilidade de compra é o que realmente importa para tomar decisões de marketing e vendas.**

**E a probabilidade conjunta?**

Ela é a base matemática da Rede Bayesiana.

Ela permite responder perguntas mais sofisticadas:

- Qual a chance de encontrar esse perfil de cliente?
- Qual variável influencia mais?
- Qual a probabilidade de ter clicado na promoção sabendo que comprou?
- Qual a probabilidade de já ser cliente sabendo que comprou?

Essas perguntas usam o **Teorema de Bayes**.

Em **Redes Bayesianas**, quando estamos **fazendo previsão ou classificação**, quase sempre o número que mais nos interessa é:

**Probabilidade de Conjunta**, exemplo, probalidade de compra dado que o cliente tem um histórico de compras, passou muito tempo no site e clicou na promoção:
'P(Compra | Histórico, Tempo, Promoção)'

ou seja:

Dadas as evidências que observei, qual a chance de compra?
Esse é exatamente o tipo de cálculo que sistemas de recomendação, análise de fraude e diagnóstico médico utilizam no dia a dia.


Se quiser aprofundar ainda mais, algumas boas práticas são:

- **Validação com dados reais:** testar o modelo com históricos de clientes para verificar a precisão das previsões.
- **Ajuste dinâmico:** atualizar probabilidades conforme novos dados entram, mantendo o sistema adaptativo.
- **Visualização gráfica:** usar bibliotecas como networkx ou pgmpy para representar a rede e facilitar a interpretação.

As fontes das probabilidades poderiam ser das campanhas de anúncios no Meta Ads (anúncios no Instagram e Facebook), por exemplo.
O profissional de dados iria analisar as campanhas junto ao gestor de tráfego e concluir esses números de probablidade com base nas estatísticas que eles têm em mão (CPA, CPC, CPM...) e modelar a rede para inferencia e visualização.

Meu post original na Alura para empresas https://cursos.alura.com.br/forum/topico-projeto-faca-como-eu-fiz-construindo-uma-rede-bayesiana-568527
