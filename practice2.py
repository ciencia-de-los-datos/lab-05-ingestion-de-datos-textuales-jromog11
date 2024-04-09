import pandas as pd
import os.path
import glob


def dict_phrase_sentiment(ruta):
    data = list()
    lista_archivos = glob.glob(ruta)

    for file in lista_archivos:
        with open(file, "r", encoding="latin-1") as archivo:
            text = archivo.read()
            sentiment = os.path.basename(os.path.dirname(file))

            data.append(({"phrase": text, "sentiment": sentiment}))

    return data


def dataframe(negative, neutral, positive, output):
    negative_dict = dict_phrase_sentiment(negative)
    neutral_dict = dict_phrase_sentiment(neutral)
    positive_dict = dict_phrase_sentiment(positive)

    lista_final = negative_dict + neutral_dict + positive_dict

    df = pd.DataFrame(lista_final)

    return df.to_csv(output, sep=",", header=True, index=False)


neutral_train = "data/train/neutral/*.txt"
positive_train = "data/train/positive/*.txt"
negative_train = "data/train/negative/*.txt"

neutral_test = "data/test/neutral/*.txt"
positive_test = "data/test/positive/*.txt"
negative_test = "data/test/negative/*.txt"

dataframe(neutral_train, positive_train, negative_train, "train_dataset.csv")
dataframe(neutral_test, positive_test, negative_test, "test_dataset.csv")
