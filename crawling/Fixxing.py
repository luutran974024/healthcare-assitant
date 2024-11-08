import pandas as pd
import re
import selenium
import bs4 as BeautifulSoup
def reading_name(f):
    with open(f, 'r', encoding= 'utf-8') as file:
        content = file.read()
    return content
def deploy_in_list(data):
    set_of_name = set()
    list_of_names = []
    for line in data.split('\n'):
        components = line.split()
        for i in range(len(components)):
            component = components[i]
            if component not in set_of_name:
                set_of_name.add(component)
                list_of_names.append(component)
        full_name = " ".join(components)
        list_of_names.append(full_name)
    return list_of_names
for i in range(0, 1):
    data = pd.read_csv(f'ivie_concatenated_from_1_to_300.csv')
    print(f"The before length of data: {len(data)}" )
    boys_f = 'D:/final advanced AI/boy.txt'
    girl_f = 'D:/final advanced AI/girl.txt'
    boy_name = reading_name(boys_f)
    girl_name = reading_name(girl_f)
    names = set()
    list_of_boys = deploy_in_list(boy_name)
    list_of_girls = deploy_in_list(girl_name)
    middle_name = ["Thị", "Mến", "Hai", 'Lucy', 'Dũ', 'Đa', 'Bao', 'Hanh', 'Doan','Thạnh', 'Đỗ',
                   'Phạm', 'Đàm', 'Tư', 'Lạng','Tuân','Thủy', 'Phuong', 'Hóa','Duong', 'Ha',
                   'Huong', 'Nhường', 'Bảng', 'Quoc', 'Thai','Pham', 'Đặng', 'Nghệ','Nguyen',
                   'Trần','Nụ', 'Phòng', 'Phan', 'Tĩnh','Chang', 'Xuyên', 'Vũ', 'Sam', "Đại",'Hang',
                   'Noi', 'Trì', 'Định', 'Đình', 'Ba', 'Bùi', 'Cạn', 'Ngô', 'Thúy','Trịnh', 'Phương',
                   'Thủ', 'Lành', 'Biên', 'Lệnh', 'Tam', 'Cầu', 'Giấy','Đồng','Nai', 'Long', 'Thái', 'An',
                   'Phú', 'Hinh', 'Chềnh', 'Mừng', 'Mã', 'Trị','Vũng', 'Tàu', 'Truong', 'Luong', 'Mơ', 'Thới',
                   'Huế', 'Tới', 'Diễn', 'Lào', 'Cai', 'California', 'Đà', 'Lạt', 'Nẵng', 'Mạnh', 'Đắc', 'Hằng', 'Lạng',
                   'Đàn', 'Doãn', 'Điện', 'Thao', 'Hòa',
                   ]
    Health_insurance = ['bảo hiểm y tế', 'thủ tục', 'gói cước', 'bảo hiểm',
                        'chính sách','công chứng', 'ĐKKH', 'hồ sơ', 'CMND',]

    money = [ "đồng", 'chi phí', 'phí', 'bảng giá', 'giá', 'lãi suất',
             'vay', 'trả góp','chi phi', 'tr', 'thanh toán', 'tín dụng', 'hóa đơn', "nghìn", 'ngàn']
    Question_start = [' Nếu còn bất kỳ thắc mắc','- HCM','           Nếu còn câu hỏi thắc mắc', " Tham khảo chi tiết",' Liên hệ', '   Liên hệ', '  Để đặt lịch khám',
                      '   Bạn có thể đặt lịch', '   Bạn có thể liên hệ', '    Nếu có thêm bất cứ thắc mắc',
                      '     Bạn có thể đến  liên hệ','       Xem thêm kiến thức', '        Xem thêm các kiến thức','          Tham khảo thêm:',
                      '           Hoặc liên hệ', '            Nếu còn câu hỏi thắc mắc','           Nếu còn bất cứ thắc mắc', '           Bạn có thể gọi lên tổng đài',
                      '           Để đặt lịch thăm','           Bạn có thể gọi lên', '           Chị có thể gọi lên', '           /Chị có thể gọi lên',
                      '            Chị có thể gửi câu hỏi',' Cháu có thể đặt lịch khám',' Để đặt lịch thăm khám',' Để đặt lịch khám',' Để có thể đặt lịch khám',
                      ' Chị có thể gọi đến',' Bạn hãy gọi đến', ' Ngoài ra bạn có thể tham khảo', ' Bạn có thể gọi điện',
                      ' Mời anh chị đến', 'Nếu có thể,', ' Bạn có thể đặt lịch',' Nếu có thể',' Cháu gọi điện', '  Để đặt lịch khám', ' Để được tư vấn',
                      ' Để đặt hẹn khám,',' Bạn có thể gọi đến', '  Bạn có thể gọi đến',' Tham khảo:',' Nếu có bất kỳ thắc mắc', ' Chị vui lòng gọi đến',
                      ' Chị có thể gọi điện',
                      ]
    comma_to_change = ['\n']
    list_of_other_words  = ["Đa khoa Tâm Anh",'Sanders T. Frank ', 'Nutrihome ','IVFTA','ISOFHCARE','ĐKTA',' Yaqoob Bhat', 'Aneurin Bevan ','nutrihome ','Nutrihome, ', 'Huyên','Hotline Hà Nội: 024 3872 3872, TP.HCM: 0287 102 6789', 'HỆ THỐNG BỆNH VIỆN ĐA KHOA TÂM ANH', 'hotline',
                            'Hồ Chí Minh','Hà Nội', '02871026789',' 0977748122','093 180 6858','0818467686','0868891318',' 0818467686  0868891318 ', 'TP HCM','TP.HCM',' - HCM', '028 7102 6789','024 3872 3872',' 0287 102 6789', 'Hotline: 0287 102 6789','1900 633 599 ' ,'(108 Hoàng Như Tiếp, P.Bồ Đề, Q.Long Biên, TP.Hà Nội)',
                            '(2B Phổ Quang, P.2, Q.Tân Bình, TP.HCM)', 'Hotline: 024 3872 3872', 'Tâm Anh', 'BVĐK','tại :','Trung tâm Hỗ trợ sinh sản',',    (108   , P.Bồ Đề, Q. Biên, TP.),  . ',
                            'Đánh giá bài viết', 'Hotline: 093 180 6858 – 0287 102 6789','3872.3872', '2B Phổ Quang, P.2, Q.Tân Bình, TP.HCM', '108 Hoàng Như Tiếp, P.Bồ Đề, Q.Long Biên, TP.Hà Nội', 'Fanpage: https://www.facebook.com/benhvientamanh',
                            'Chuyên khoa: https://tamanhhospital.vn/chuyen-khoa/san-phu/', 'Trân trọng!','0973311006' ,'108 Hoàng Như Tiếp, P.Bồ Đề, Q.Long Biên, TP.Hà Nội', '2B Phổ Quang, P.2, Q.Tân Bình, TP.Hồ Chí Minh',
                            '– 024 7106 6858', 'Hotline:', '093 180 6858 –', 'Trân trọng', '(2B Phổ Quang, P.2, Q.Tân Bình, TP.HCM),', '(108 Hoàng Như Tiếp, P.Bồ Đề, Q.Long Biên, TP.Hà Nội),', 'Trân trọng.', ' – lầu 2,','toà nhà A', ' số 2B Phổ Quang,'
                            ' quận Tân Bình,', ' TP.Hồ Chí Minh', '3802/QĐ-BYT','Trung tâm Hỗ trợ sinh sản',"Trung tâm Hỗ Trợ  Sản ()" ,'TRUNG TÂM TIM MẠCH TÂM ANH', '(TP.HCM)', '(Hà Nội)', 'hoặc', ' :  ()  ()', 'Lầu 2, Toà nhà A,  tâm Hỗ Trợ  Sản –   , số 2B đường Phổ , quận  , TP.  ',
                            'địa chỉ: 2B Phổ quang, phường 2, quận    ','- Quận  , TP .','H.','Q.','TP.',' ,  , ', '   (số 2B Phổ , phường 2, quận  ) ', '028.7102.6789','Hệ thống  . Tại  (2B Phổ , P.2, Q. , ), . Tại  (108   , P.Bồ Đề, Q. Biên, TP.),  . ',
                            'Tại  -HCM,','   ()  ()', ' :  (tại )  (tại )',' (), (Tp. )' ,'  (   và  , )','  :108   , P.Bồ Đề, Q. Biên, TP.  :2B Phổ , P.2, Q. , TP.                         :', '   hệ Bệnh viện Đa   theo thông tin sau đây để được tư vấn cụ thể',
                            ' tư 57/2015/TT-BYT  dẫn', '   tại 2B Phổ , P2, Q.','108   , P.Bồ Đề, Q. Biên, TP.      2B Phổ , P.2, Q. , TP.', 'Theo QĐ 3802 của Bộ Y tế,', 'Bạn có thể tham khảo thêm thông tin về   thông qua   ()  (TP. HCM).',
                            ' Bạn có thể tham khảo thêm thông tin về   thông qua  024.3872.3872 ()  (TP. HCM).','Tp.HCM',' Theo quyết định 3802 của Bộ Y tế:', ' PGS.TS.BS   ', ' tamanhhospital.vn.',' ThS.BS    – ',
                            '( định số 2763/QĐ-BYT) ', ' bản số 1158 của ', ', Hệ thống  . Tại  (2B Phổ , P.2, Q. , ), . Tại  (108   , P.Bồ Đề, Q. Biên, TP.),  .', '  . Tại  (2B Phổ , P.2, Q. , ), . Tại  (108   , P.Bồ Đề, Q. Biên, TP.),  .',
                            'Xem thêm trang kiến thức tim mạch của  tại đây.', 'Xem thêm trang kiến thức tim mạch .', 'Và xem thêm kiến thức tim mạch tại đây.','Xem thêm: Các kiến thức về tim mạch và huyết áp tại đây', ' Và cùng xem thêm nội dung trang kiến thức tim mạch .',
                            '   theo địa chỉ số 2B Phổ , phường 2, quận  ,  ', '   theo địa chỉ số 2B Phổ , phường 2, quận  ,  ', '  , TPHCM (số 2B, Phổ , Phường 2, quận  , )   Tim mạch,  ,  (số 108 Phố   , phường Bồ Đề, quận  Biên, )',
                            ' :108   , P.Bồ Đề, Q. Biên, TP.  :2B Phổ , P.2, Q. , TP.  khoa: https://tamanhhospital.vn/chuyen-khoa/trung-tam-tim-machWebsite: https://tamanhhospital.vn                        :                          ',
                            ', TPHCM   Tim mạch,  , ','  Xem thêm:  thức tim mạch',' Địa chỉ: Phòng 230 – Nhà C2 – 40 Tràng  –   – ', '(ESC/ESH 2018) ',
                            ' Để xêm thêm nội dung liên quan bạn có thể đọc thêm tại trang kiến thức Tim mạch .', ' Để thăm khám, em có thể tham khảo Trung tâm  thương chỉnh hình,  , TPHCM tại địa chỉ số 2B, Phổ , Phường 2, quận  , thành phố     thương chỉnh hình,  ,  tại địa chỉ số 108 Phố   , phường Bồ Đề, quận  Biên, thành phố . Hoặc liên hệ tổng đài của Hệ thống bệnh viện để được hỗ trợ. ',
                            'Tại  Phẫu thuật khớp và Y học thể thao – Bệnh viện  –  có Giáo sư Trần  , là chuyên gia hàng đầu về lĩnh vực này. Bạn có thể đăng ký lịch khám với Giáo sư để được tư vấn hỗ trợ.',
                            'TPHCM', ' Để thăm khám, bạn có thể tham khảo Trung tâm  thương chỉnh hình,  ,  tại địa chỉ số 2B, Phổ , Phường 2, quận  , thành phố     thương chỉnh hình,  ,  tại địa chỉ số 108 Phố   , phường Bồ Đề, quận  Biên, thành phố .',
                            ' Bạn có thể tham khảo Trung tâm  thương chỉnh hình,  ,  tại địa chỉ số 2B, Phổ , Phường 2, quận  , thành phố     thương chỉnh hình,  ,  tại địa chỉ số 108 Phố   , phường Bồ Đề, quận  Biên, thành phố .',
                            '  ,  tại địa chỉ số 2B, Phổ , Phường 2, quận  , thành phố     thương chỉnh hình,  ,  tại địa chỉ số 108 Phố   , phường Bồ Đề, quận  Biên, thành phố ',
                            ' Trung tâm  thương chỉnh hình,  ,  tại địa chỉ số 2B, Phổ , Phường 2, quận  , thành phố     thương chỉnh hình, Bệnh viện đa khoa ,  tại địa chỉ số 108 Phố   , phường Bồ Đề, quận  Biên, thành phố . ',
                            'Trung tâm  thương chỉnh hình,    tại địa chỉ số 2B, Phổ , Phường 2, quận  , thành phố     thương chỉnh hình,  ,  tại địa chỉ số 108 Phố   , phường Bồ Đề, quận  Biên, thành phố   ',
                            ' Tại , bạn có thể tìm đến 3 địa chỉ của là Số 3 Cầu Giấy, P. Láng   Số 180  , P.  , Q. Đống ,   Tầng 3, tòa nhà NewSkyline, lô CC2 khu đô thị mới  Quán –  , Q.  , ',
                            ' tại địa chỉ 108 Phố   , phường Bồ Đề, quận  Biên, thành phố ',
                            'Bạn có thể đến khoa Nhi chỉnh hình của Bệnh viện Chấn thương chỉnh hình  Bệnh viện Nhi đồng. Tại , bạn có thể tìm đến 3 địa chỉ của là Số 3 Cầu Giấy, P. Láng   Số 180 Trường , P.  , Q. Đống ,   Tầng 3, tòa nhà NewSkyline, lô CC2 khu đô thị mới  Quán –  , Q.  , .',
                            'Để hiểu hơn về phương pháp này, mời bạn tham khảo thông tin tại bài viết: https://tamanhhospital.vn/phuong-phap-chiropractic/',
                            '','BS.ISOFHCARE']
    concatenated_list = list_of_girls + list_of_boys + middle_name
    concatenated_list.remove('Tiểu')
    def replace_matching_words_specific_name(text):
        if isinstance(text, float):
            print(f"Find the None value in file {i}")
            return text
        words = re.findall(r'\b\w+\b', text)
        words_to_replace = set(words).intersection(concatenated_list)
        for word in words_to_replace:
            if word == "Trung" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'tâm':
                continue
            if word == "Trung" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'Ương':
                continue
            if word == "Thời" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'điểm':
                continue
            if word == "Thỉnh" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'thoảng':
                continue
            if word == "Thông" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'thường':
                continue
            if word == "Thông" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'tin':
                continue
            if word == "Phụ" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'thuộc':
                continue
            if word == "Hiệp" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'hội':
                continue
            if word == "Bình" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'thường':
                continue
            if word == "Quốc" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'tế':
                continue
            if word == "Quốc" and words.index(word) < len(words) -1 and words[words.index(word) -1] == 'Hàn':
                continue
            if word == "Từ" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'đó':
                continue
            if word == "Liên" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'hệ':
                continue
            if word == "Khả" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'năng':
                continue
            if word == "Tất" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'cả':
                continue
            if word == "Phụ" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'thuộc':
                continue
            if word == "Tiền" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'sử':
                continue
            if word == "Tổ" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'chức':
                continue
            if word == "Thời" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'gian':
                continue
            if word == "Trường" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'hợp':
                continue
            if word == "Gia" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'đình':
                continue
            if word == "Phương" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'pháp':
                continue
            if word == "Triệu" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'chứng':
                continue
            if word == "Hội" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'chứng':
                continue
            if word == "Sinh" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'sản':
                continue
            if word == "Thụ" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'tinh':
                continue
            if word == "Chấn" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'thương':
                continue
            if word == "Thế" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'giới':
                continue
            if word == "Việt" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'nam':
                continue
            if word == "Nhi" and words.index(word) < len(words) -1 and words[words.index(word) -1] == 'Ngoại':
                continue
            if word == "Nhi" and words.index(word) < len(words) -1 and words[words.index(word) -1] == 'khoa':
                continue
            if word == "Giao" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'hợp':
                continue
            if word == "Thông" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'liên':
                continue
            if word == "THời" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'điểm':
                continue
            if word == "Nguyên" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'nhân':
                continue
            if word == "Dinh" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'dưỡng':
                continue
            if word == "Thực" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'tế':
                continue
            if word == "Khi" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'đó':
                continue
            if word == "Tiểu" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'khó':
                continue
            if word == "Tiểu" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'gắt':
                continue
            if word == "Tinh" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'hoàn':
                continue
            if word == "Tinh" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'trùng':
                continue
            if word == "Dương" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'vật':
                continue
            if word == "Lạc" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'nội':
                continue
            if word == "Nam" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'khoa':
                continue
            if word == "Hạ" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'tinh':
                continue
            if word == "Đông" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'phôi':
                continue
            if word == "Đông" and words.index(word) < len(words) -1 and words[words.index(word) +1] == 'tinh':
                continue
            text = re.sub(r'\b' + word + r'\b', '', text)
        return text
    def replace_matching_words_specific_word(text):
        if isinstance(text, float):
            return text
        for word in list_of_other_words + comma_to_change:
            text = text.replace(word, "")
        return text


    data['Answers'] = data['Answers'].apply(replace_matching_words_specific_word)
    data['Description'] = data['Description'].apply(replace_matching_words_specific_word)
    data['Answers'] = data['Answers'].apply(replace_matching_words_specific_name)
    data['Description'] = data['Description'].apply(replace_matching_words_specific_name)
    for num in range(len(data['Answers'])):
        if isinstance(data['Answers'][num], float):
            continue
        lines = re.split(r'[.!?]', data['Answers'][num])
        lines = [line for line in lines if not any(line.startswith(Question) for Question in Question_start)]
        filtered_lines_for_insurance = []
        for value in lines:
            if not any(w in value for w in Health_insurance):
                filtered_lines_for_insurance.append(value)
        final_filtered_sentences = []
        for val in filtered_lines_for_insurance:
            count = sum(t in val for t in money)
            if count < 2:
                final_filtered_sentences.append(val)
        answer_demo = ' '.join(final_filtered_sentences)
        if len(final_filtered_sentences) <= 4 and len(answer_demo) <= 80:
            print("What I try to delete: ", answer_demo)
            answers_text = ""
        else:
            print(f"The text that passed with the length: {len(answer_demo)}")
            answers_text = ".".join(final_filtered_sentences)
            answers_text = re.sub('\.{2,}', '.', answers_text)

        if answers_text == "":
            data.drop(num, inplace=True)
        data["Answers"][num] = answers_text
    data.dropna(subset='Answers', inplace= True)
    print(f"The after length of data: {len(data)}" )
    data.to_csv(f'ivie_concatenated_from_1_to_300_new_fixed_1.csv', index= False)
    print(f"Done file {i}")