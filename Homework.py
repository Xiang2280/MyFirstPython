import os
import sys
import jieba

root_dir = r"G:\Python Learning\201808"
with open("問卦Title.csv", "w") as abstract:
   
    for file in os.listdir(root_dir):
        file_name = root_dir + "\\" + file
        filein = open(file_name,'r', encoding = 'utf-8')
       

        string = ""
        for category in filein.readlines()[3]:
            string += category.rstrip("\n")
        try:
            if "問卦" in string:
                filein.seek(0)
                for title in filein.readlines()[2][6:]:
                    abstract.write(title.rstrip("\n"))
            else:
                continue
        except UnicodeEncodeError:
            print(file_name)

        abstract.write("\n")
    filein.close()

fileTitle = open("問卦Title.csv",'r').read()
seglist = jieba.cut(fileTitle, cut_all = False) 
test = open('問卦jieba.csv','wt')
for i in seglist:
    test.write(i + '\n')
test.close()