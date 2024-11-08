import re
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

df_concat = pd.DataFrame(columns=["Description", "Answers"])

for href_url in range(9001, 12001):
    link_reference = f'https://ivie.vn/cong-dong?id={href_url}'
    print("Initiating: ", link_reference)
    ref = requests.get(link_reference)
    so = BeautifulSoup(ref.content, 'html.parser')
    card_body_from_ref = so.find_all('div', class_='card-body')
    Description = []
    Each_answer = []

    for card_ref in card_body_from_ref:
        Doc_or_patient_tag = card_ref.find('p', {'class': 'font-weight-bold'})
        Doc_or_patient = Doc_or_patient_tag.find('div', {'class': 'sc-eDPEul sc-eldPxv AbVrp jbkqVE'})

        if Doc_or_patient is None:
            texts = card_ref.find('p', {'class': 'description'}).text
            Description.append(texts)
        else:
            Answer_from_doc = card_ref.find('p', {'class': 'description'}).text
            Each_answer.append(Answer_from_doc)

    Description_text = " ".join(Description)
    answer_text = ". ".join(Each_answer)
    data = {
        "Description": Description_text,
        "Answers": answer_text
    }
    # Create a temporary DataFrame for the current iteration
    df_temp = pd.DataFrame(data, index=[0])
    # Append the temporary DataFrame to the concatenated DataFrame
    df_concat = pd.concat([df_concat, df_temp], ignore_index=True)

# Export the concatenated DataFrame to a single Excel file
excel_file_path = f"ivie_concatenated_from_9001_to_12001.csv"
df_concat.to_csv(excel_file_path, encoding='utf-8', index=False)
print("DataFrame has been exported to csv successfully.")