import pickle
import pandas as pd


df = pd.read_csv("./models/data/RadioJavan_Top.csv")

df = df.drop_duplicates()

indices = pd.Series(df.index, 
                    index=df['musicName']).drop_duplicates()

with open("./models/fainal_model/model.pkl", 'rb') as file:
    similarity = pickle.load(file)

def radio_javan_recommendation(title, similarity = similarity):
    index = indices[title]

    similarity_scores = list(enumerate(similarity[index].tolist()))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:11]

    movieindices = [i[0] for i in similarity_scores]
    return df[['musicName', 'artistName']].iloc[movieindices]

