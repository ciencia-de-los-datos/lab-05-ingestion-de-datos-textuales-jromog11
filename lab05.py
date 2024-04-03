import pandas as pd
import pyarrow
import glob


train_negative = glob.glob("data/train/negative/*.txt")
train_neutral = glob.glob("data/train/neutral/*.txt")
train_positive = glob.glob("data/train/positive/*.txt")

negative_file = [
    pd.read_csv(file, sep="\t", header=None, names=["phrase", "sentiment"])
    for file in train_negative
]
negative_concat = pd.concat(negative_file, ignore_index=True)

negative_concat["sentiment"] = "negative"

positive_file = [
    pd.read_csv(file, sep="\t", header=None, names=["phrase", "sentiment"])
    for file in train_positive
]

positive_concat = pd.concat(positive_file, ignore_index=True)

positive_concat["sentiment"] = "positive"

neutral_file = [
    pd.read_csv(file, sep="\t", header=None, names=["phrase", "sentiment"])
    for file in train_neutral
]

neutral_concat = pd.concat(neutral_file, ignore_index=True)

neutral_concat["sentiment"] = "neutral"

train = pd.concat((neutral_concat,positive_concat, negative_concat))


train.to_csv("train_dataset.csv", sep="\t", index=False, header=["phrase", "sentiment"])


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