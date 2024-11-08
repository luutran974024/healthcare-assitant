import pandas as pd
import json

df = pd.read_excel(
    'D:\\Work\\IVS_AI_Healthcare_intern\\questions_and_answers6.xlsx')
json_list = []
for index, row in df.iterrows():
    json_obj = {
        "id": index + 1,
        "question": row['Question'],
        "answer": row['Answer'],
        # "label": row['Label']
    }
    json_list.append(json_obj)

with open('vnexpress2.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_list, json_file, ensure_ascii=False, indent=2)
