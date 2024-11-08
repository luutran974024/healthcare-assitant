from bs4 import BeautifulSoup as soup
import requests
import json

class Mining():
    def __init__(self, url) -> None:
        self.url = url
        self.part_one = None
        self.part_two = None
        self.questions = []
        self.answers = []

    def find(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            page_content = soup(response.content, 'html.parser')
            self.part_one = page_content.find("div", class_="cat_section", id="cat_featured")
            self.part_two = page_content.find("div", id="cat_container")
        else:
            print("Failed to fetch page:", self.url)

    def crawl(self):
        if self.part_one:
            self.get_link(self.part_one)
        if self.part_two:
            self.get_link(self.part_two)

    def get_link(self, part):
        for i in part.find_all("div", class_="responsive_thumb"):
            links = i.find("a").get("href")
            self.extract_data(links)

    def extract_data(self, links):
        response = requests.get(links)
        answer_soup = soup(response.content, 'html.parser')
        question = answer_soup.find("h1").text.strip()
        divs = answer_soup.find_all("div", class_="step")
        full = []
        for div in divs:
            ul_elements = div.find_all("ul")
            for ul in ul_elements:
                li_items = ul.find_all("li")  # Tìm tất cả các thẻ <li> trong từng thẻ <ul>
                li_texts = [li.text.strip() for li in li_items]  # Tạo danh sách các văn bản từ các thẻ <li>
                b_element = div.find("b").text.strip()
                content = div.text.strip()
                combined_text = content + " "  + " ".join(li_texts)
                full.append(combined_text)
        # Thêm dữ liệu của từng câu hỏi vào danh sách
        self.questions.append(question)
        self.answers.append(full)


    def convert_to_json(self):
        data = []
        for question, answer in zip(self.questions, self.answers):
            data.append({
                "instruction": question,
                "input": "",
                "output": answer
            })
        return data

    def save_data(self):
        data = self.convert_to_json()
        file_name = input("Input your file name to save: ")
        file_path = f"./data/{file_name}.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
    @classmethod
    def main(cls):
        url = input("Enter URL: ")
        mining = cls(url)
        mining.find()
        mining.crawl()
        mining.save_data()  
