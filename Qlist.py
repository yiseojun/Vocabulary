# 모의고사 목록 & 문제 목록 수합 모듈
import os

class scanFolder :
    def __init__(self, type_path) :
        self.path = type_path

    # 폴더 스캔 모듈(모의고사 목록)
    def scan(self) :
        # 읽어올 폴더 경로
        path = 'static/data/voca_list'

        # 경로에서 하위 항목을 읽음
        items = os.listdir(path)
        folders = ''

        for item in items:
            # 항목이 폴더인지 확인하고 리스트에 추가
            if os.path.isdir(os.path.join(path, item)):
                folders += f'<a href="/{ self.path }/{ item }" class="linebreak">{ item }</a>\n'
        
        # 폴더 이름들이 들어있는 리스트 출력(문자열 맨 마지막에 공백이 있으므로 슬라이싱)
        return folders[:-1]

class scanFile :
    def __init__(self, type_path) :
        self.path = type_path

    # 파일 스캔 모듈(문제 파일 목록)
    def scan(self, qpath) :
        # 파일 이름을 수집할 폴더 경로를 지정
        path = f'static/data/voca_list/{ qpath }'

        # 경로에서 하위 항목을 읽음
        items = os.listdir(path)
        txt_files = ''

        for item in items:
            # 항목이 파일인지 확인하고 .txt 확장자를 가진지 확인
            if os.path.isfile(os.path.join(path, item)) and os.path.splitext(item)[1] == '.txt':
                filename = os.path.splitext(item)[0]
                txt_files += f'<a href="/{ self.path }/{ qpath }/{ filename }" class="linebreak">{ filename }</a>\n'
        
        return txt_files[:-1]

class makeTable :
    def readFile() :
        with open("./static/data/voca_list/Frequent.txt", 'r', encoding = "utf-8") as file :
            content = eval(file.read())

        return content
    
    def makeHTML() :
        wordDict = makeTable.readFile()
        htmlCode = ""

        for word in wordDict.keys() :
            htmlCode += f"<tr>\n<td>{word}</td>\n<td>{wordDict[word]}</td>\n</tr>\n"

        return htmlCode[:-1]

if __name__ == "__main__" :
    print(makeTable.makeHTML())