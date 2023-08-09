# 모의고사 목록 & 문제 목록 수합 모듈
import os

# 폴더 스캔 모듈(모의고사 목록)
def scanFolder() :
    # 읽어올 폴더 경로
    path = 'static/data/voca_list'

    # 경로에서 하위 항목을 읽음
    items = os.listdir(path)
    folders = ''

    for item in items:
        # 항목이 폴더인지 확인하고 리스트에 추가
        if os.path.isdir(os.path.join(path, item)):
            folders += f'<a href="/단어목록/{ item }" class="linebreak">{ item }</a>\n'
    
    # 폴더 이름들이 들어있는 리스트 출력(문자열 맨 마지막에 공백이 있으므로 슬라이싱)
    return folders[:-1]


# 파일 스캔 모듈(문제 파일 목록)
def scanFile( qpath ) :
    # 파일 이름을 수집할 폴더 경로를 지정
    path = f'static/data/voca_list/{ qpath }'

    # 경로에서 하위 항목을 읽음
    items = os.listdir(path)
    txt_files = ''

    for item in items:
        # 항목이 파일인지 확인하고 .txt 확장자를 가진지 확인
        if os.path.isfile(os.path.join(path, item)) and os.path.splitext(item)[1] == '.txt':
            filename = os.path.splitext(item)[0]
            txt_files += f'<a href="/단어목록/{ qpath }/{ filename }" class="linebreak">{ filename }</a>\n'
    
    return txt_files[:-1]


if __name__ == "__main__" :
    print(scanFile("2023년도 3월 모의고사"))