import Gemini_API
import numpy as np
import pandas as pd
from  flask import jsonify

data = pd.read_csv('asos-e-commerce-dataset-30845-products.zip')
data['id'] = range(0,data.shape[0])
li=['id']
for i in data.columns[:-1]:
  li.append(i)
data=data[li]


def show_recommendation(Prompt):
    list=Gemini_API.give_indices(Prompt)
    print("Hello")
    list.append(1)
    print(list)

    li = {'li':str(list)}
    final_li=[int(i) for i in list]
    dic={}
    for i in final_li:
        row = data.iloc[i]
        dic[i]={
            'id':str(row.id),
            'name':str(row.name),
            'size':str(row.size),
            'description':str(row.description),
            'images':str(row.images),
            'sku':str(row.sku)
        }
    print(dic)
    return jsonify(dic)



