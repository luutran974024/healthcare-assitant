import pandas as pd
from bs4 import BeautifulSoup
import requests

base_url = "https://nld.com.vn/suc-khoe/ban-gap-phai-van-de-hau-covid-19-hay-dat-cau-hoi-de-duoc-giai-dap-20220316073047351.htm"
data = []

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

groups = soup.find_all('div', class_='interview-item qna')  # Adjusted class name

for gr in groups:
    # Lấy nội dung của câu hỏi
    question_div = gr.find('div', class_='interview-qa interview-question')
    question = question_div.find('p', class_='content').get_text(strip=True) if question_div else "Question not found"
    
    # Lấy nội dung của câu trả lời
    answer_div = gr.find('div', class_='interview-qa interview-answer')
    if answer_div:
        content_div = answer_div.find('div', class_='content')
        answer = content_div.get_text(strip=True) if content_div else "Answer not found"
        data.append({'Question': question, 'Answer': answer})

# Tạo DataFrame từ dữ liệu thu thập được
df = pd.DataFrame(data)
df.to_excel("D:\\Work\\IVS_AI_Healthcare_intern\\mdattr\\suckhoe.xlsx", index=False)
print('done')
