import pandas as pd
import os


def read_files(directory):
    data = list()
    for sentiment in os.listdir(directory):
        sentiment_dir = os.path.join(directory, sentiment)

        if os.path.isdir(sentiment_dir):
            for filename in os.listdir(sentiment_dir):
                with open(
                    os.path.join(sentiment_dir, filename), "r", encoding="latin-1"
                ) as file:
                    try:
                        text = file.read()
                        data.append({"phrase": text, "sentiment": sentiment})
                    except UnicodeDecodeError:
                        print(f"Error:{filename}")

    return data


print(read_files("data/train"))
