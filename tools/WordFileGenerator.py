import re

class generator :
    def __init__(self, path) :
        self.path = path
    
    def generate(self) :
        question_num_list = parser.find_left_substrings()

        for index, content in zip(question_num_list, parser.split_word_list())  :
            with open(f"{self.path}\\{index}번.txt", "w") as f:
                f.write("{{\n    {1}\n}}".format(index, content.strip()))

class parser :
    def find_left_substrings() : # 문항 번호 리스트 생성 함수
        with open('word.txt', 'r', encoding='utf-8') as f:
            input_str = f.read()

        result = []

        for i, char in enumerate(input_str):
            if char == '번' and i >= 2:
                result.append(input_str[i-2:i])

        return result
    
    def replace() : # 이상 문자 대체 함수
        with open('word.txt', 'r', encoding='utf-8') as f:
            contents = f.read().replace('”', '"')
            contents = contents.replace('“', '"')
        with open('word.txt', 'w', encoding='utf-8') as f:
            f.write(contents)

    def split_word_list() : # 문항 별 단어 분리 함수
        with open('word.txt', 'r', encoding='utf-8') as f:
            input_str = f.read()

        pattern = r'\{([^}]+)\}'
        regex = re.compile(pattern)

        return regex.findall(input_str) # 문항별 단어가 담긴 리스트

if __name__ == "__main__" :
    path = r"C:\Users\Computer\Documents\repo\vcblry\static\data\voca_list\2022학년도 고3 9월 모의고사"
    textObj = generator(path)
    parser.replace()
    textObj.generate()