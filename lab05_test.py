import pandas as pd
import glob
import pyarrow

neutral_path = "data/test/neutral/*.txt"
positive_path = "data/test/positive/*.txt"
negative_path = "data/test/negative/*.txt"

archivos_neutrales = glob.glob(neutral_path)
archivos_positivos = glob.glob(positive_path)
archivos_negativos = glob.glob(negative_path)

neutral = [
    pd.read_csv(file, sep="\t", header=None, names=["phrase", "sentiment"])
    for file in archivos_neutrales
]

positivo = [
    pd.read_csv(file, sep="\t", header=None, names=["phrase", "sentiment"])
    for file in archivos_positivos
]

negativo = [
    pd.read_csv(file, sep="\t", header=None, names=["phrase", "sentiment"])
    for file in archivos_negativos
]

df_neutral = pd.concat(neutral)
df_neutral["sentiment"] = "neutral"

df_positivo = pd.concat(positivo)
df_positivo["sentiment"] = "positivo"

df_negativo = pd.concat(negativo)
df_negativo["sentiment"] = "negativo"

test = pd.concat((df_neutral, df_positivo, df_negativo))

test.to_csv("test_dataset.csv", sep="\t", header=True)

