import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file Excel
df = pd.read_excel("D:/Work/AI_ChatBot/1_CrawlData/Crawl_Data_100K.xlsx")

# Groupby theo chuyên khoa và đếm số lượng câu hỏi trong mỗi chuyên khoa
specialties_count = df.groupby("Label").size().reset_index(name='QuestionCount')
specialties_count = specialties_count.sort_values(by='QuestionCount', ascending=False)

# Tính tổng số lượng mẫu
total_samples = specialties_count['QuestionCount'].sum()

# Vẽ biểu đồ cột
plt.figure(figsize=(10, 6))
bars = plt.bar(specialties_count['Label'], specialties_count['QuestionCount'], color='blue')
plt.xlabel('Department')
plt.ylabel('Nums')
plt.title('Count of label')
plt.xticks(rotation=45, ha='right')

# Thêm số lượng lên từng thanh cột
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 2), ha='center', va='bottom')

# Thêm tổng số lượng mẫu lên góc phải trên của biểu đồ
plt.text(len(specialties_count['Label']) - 0.25, total_samples, f'Total: {total_samples}', fontweight='bold', ha='right', va='center')

plt.tight_layout()
plt.show()
