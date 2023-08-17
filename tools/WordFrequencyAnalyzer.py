import json
import os

Path = r".\static\data\voca_list"
FolderList = os.listdir(Path)
WordFrequencies = {}
ToRemove = []

def ReadWordFile(FolderName, FileName) :
    with open(f"{Path}\\{FolderName}\\{FileName}", 'r', encoding = "utf-8") as File :
        Content = File.read()
    
    return json.loads(Content)

for FolderName in FolderList :
    FileList = os.listdir(f"{Path}\\{FolderName}")

    for FileName in FileList :
        WordDict = ReadWordFile(FolderName, FileName)
        
        for KeyWord in WordDict.keys() :
            if KeyWord in WordFrequencies.keys() :
                WordFrequencies[KeyWord] += 1

            else :
                WordFrequencies.update({KeyWord:1})

for Key, Value in WordFrequencies.items():
    if Value == 1:
        ToRemove.append(Key)

for Key in ToRemove:
    WordFrequencies.pop(Key)

SortedFrequencies = dict(sorted(WordFrequencies.items(), key=lambda x: x[1], reverse=True))
print(SortedFrequencies)