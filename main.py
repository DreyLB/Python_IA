import pandas as pd
"""from transformers import pipeline"""
import pdfminer.high_level
from io import StringIO

# Carregar o pipeline para a tarefa de preenchimento de máscara (ou similar) que pode ajudar a inferir a função das colunas
"""classifier = pipeline("zero-shot-classification")
"""

"""def infer_column_meanings(tabular_string):
    # Transformar a string em um DataFrame
    from io import StringIO
    data = StringIO(tabular_string)
    df = pd.read_csv(data, sep="\t")

    # Definir possíveis categorias para as colunas
    candidate_labels = ["data", "nome", "idade", "endereço", "salário", "profissão", "identificação", "telefone",
                        "email"]

    column_meanings = {}

    for column in df.columns:
        # Para inferir o significado, usaremos os dados da coluna como contexto
        context = df[column].astype(str).tolist()
        context = " ".join(context[:min(5, len(context))])  # Pegar as primeiras 5 entradas para formar um contexto
        result = classifier(context, candidate_labels)

        # Atribuir o significado mais provável para a coluna
        column_meanings[column] = result['labels'][0]

    return column_meanings
"""

# Exemplo de uso
'''tabular_string = """nome\tidade\tsalário
João\t29\t2500
Maria\t34\t3200
Carlos\t40\t5000"""
'''

'''
column_meanings = infer_column_meanings(tabular_string)
print(column_meanings)
'''


documento = pdfminer.high_level.extract_text('ata2.pdf')
data = StringIO(documento)
df = pd.DataFrame.

print(df)

"""for i in range (0, 80):
    linha_2 = df.iloc[i]  # As linhas são indexadas a partir de 0
    print("\n\n\n", linha_2)"""
