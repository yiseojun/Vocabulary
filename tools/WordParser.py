WordDict = {}

with open("./tools/Frequency.txt", 'r', encoding = "utf-8") as File :
    Content = File.read().split('\n')

with open("./tools/Frequent.txt", "w", encoding = "utf-8") as f:
    for Word in Content :
        try :
            Key, Value = Word.split(" ")
            f.write("\n    \"{0}\":\"{1}\",".format(Key, Value))
            WordDict.update({Key:Value})
            
        except ValueError :
            print("Missing Content: ", Word)
    
print(WordDict)