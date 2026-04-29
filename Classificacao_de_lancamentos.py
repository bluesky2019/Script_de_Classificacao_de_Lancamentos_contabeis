import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# 1. Simulação de Dados (Onde 'Descricao' é o histórico e 'Conta' é o alvo)
data = {
    'Descricao': [
        'PAGAMENTO NF 123 DISTRIBUIDORA DE AGUA', 
        'ALUGUEL SALA 402 EDIFICIO COMERCIAL', 
        'COMPRA PAPELARIA SULFITE E CANETAS',
        'CONTA DE LUZ MENSAL CELESC', 
        'PAGAMENTO INTERNET FIBRA',
        'REEMBOLSO VIAGEM COMBUSTIVEL',
        'COMPRA CAFE E ACUCAR MERCADO'
    ],
    'Conta_Contabil': [
        'Utilidades', 
        'Aluguel', 
        'Material de Escritorio', 
        'Utilidades', 
        'Telecomunicacoes', 
        'Despesas de Viagem', 
        'Copa e Cozinha'
    ]
}

df = pd.DataFrame(data)

# 2. Construção do Pipeline
# O CountVectorizer transforma o texto em números; o RandomForest faz a classificação.
modelo_contabil = Pipeline([
    ('vetorizador', CountVectorizer()),
    ('classificador', RandomForestClassifier(n_estimators=100))
])

# 3. Treinamento
X = df['Descricao']
y = df['Conta_Contabil']

modelo_contabil.fit(X, y)

# 4. Exemplo de Uso (Prevendo novos lançamentos)
novos_lancamentos = [
    'PGTO INTERNET VIVO',
    'COMPRA DE AGUA MINERAL',
    'ALUGUEL REFERENTE A MAIO'
]

previsoes = modelo_contabil.predict(novos_lancamentos)

for desc, conta in zip(novos_lancamentos, previsoes):
    print(f"Descrição: {desc} -> Sugestão de Conta: {conta}")
