import codecs
import os

def convert_encoding(file_name) :
    # 입력 파일을 ANSI (CP949)로 읽어서, utf-8로 인코딩하기
    with codecs.open(file_name, 'r', encoding='cp949') as file_in:
        file_content = file_in.read()

    # 인코딩 변환된 내용을 원본 파일에 덮어쓰기하기
    with codecs.open(file_name, 'w', encoding='utf-8') as file_out:
        file_out.write(file_content)

path = r".\static\data\voca_list"
folder_list = os.listdir(path)

print(f"folderlist: {folder_list}")

for folder_name in folder_list :
    file_list = os.listdir(f"{path}\\{folder_name}")
    print("filelist:", file_list)
    
    for file_name in file_list :
        try :
            convert_encoding(f"{path}\\{folder_name}\\{file_name}")

        except UnicodeDecodeError :
            break

        except NotADirectoryError:
            break