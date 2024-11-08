import requests
from bs4 import BeautifulSoup
import pandas as pd


def extraction(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    list_answers = soup.find_all(class_='list-answer')
    questions_list = []
    for list_answer in list_answers:
        # Find question within each list-answer
        question_div = list_answer.find('div', class_='ask')
        question_text = question_div.find(
            'p').text.strip() if question_div else "Không có câu hỏi"
        # Find answer within each list-answer
        answer_div = list_answer.find(
            'div', class_='fck_detail block_traloi width_common')
        if answer_div:
            # Remove the element with class 'name user_traloi'
            answer_div.find('div', class_='name user_traloi').extract()
            answer_text = answer_div.find('div', class_='answer').text.strip()
        else:
            answer_text = "Không có câu trả lời"
        questions_list.append(
            {'Question': question_text, 'Answer': answer_text})
    return questions_list


# URL of the website section containing the Q&A pages
base_url = 'https://vnexpress.net/suc-khoe/cham-soc-nguoi-benh/hoi-dap-p'
total_pages = 50  # Number of pages to scrape

all_questions_list = []

for page_number in range(1, total_pages + 1):
    url = base_url + str(page_number)
    print("Lấy dữ liệu từ trang:", url)
    questions_list = extraction(url)  # Pass URL to extraction function
    all_questions_list.extend(questions_list)

# Create DataFrame from the list of question-answer pairs
df = pd.DataFrame(all_questions_list)

# Save DataFrame to an Excel file
excel_file_path = 'questions_and_answers6.xlsx'
df.to_excel(excel_file_path, index=False)

print("Dữ liệu đã được lưu vào file Excel:", excel_file_path)
