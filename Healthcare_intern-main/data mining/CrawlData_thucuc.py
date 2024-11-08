import pandas as pd
from bs4 import BeautifulSoup
import requests

base_url = "https://benhvienthucuc.vn/hoi-dap-chuyen-gia/chuyen-muc-khac/"
data = []
for page_number in range(1, 36):
    url = f"{base_url}page/{page_number}/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    questions = soup.find_all('h2', class_='entry-cau-hoi__h1') # duyệt qua từng câu hỏi

    for question in questions:
        # Lấy đường link của câu hỏi
        question_link = question.find('a')['href']

        # lấy trang câu hỏi để lấy nội dung câu trả lời
        response_question = requests.get(question_link)
        soup_question = BeautifulSoup(response_question.text, 'html.parser')
        # Lấy nội dung câu trả lời từ trang câu hỏi
        ques = soup_question.find('div', class_='entry-cau-hoi__content')
        content = soup_question.find('div', class_='entry-cau-hoi__content entry-content')
        data.append({
            "Question": ques.text.strip() if ques else "Không có câu hỏi",
            "Answer": content.text.strip() if content else "Không có câu trả lời"
        })
        print("Câu hỏi:", ques.text.strip())
        print("Câu trả lời:", content.text.strip() if content else "Không có câu trả lời")
        print("-" * 50)

df = pd.DataFrame(data)
df.to_excel("D:/Work/AI_ChatBot/1_CrawlData/auto2.xlsx", index=False)
print('done')
