# This is a sample Python script.
import pandas as pd
import os
import shutil
'''
labels:内膜增厚1; 低回声2; 高回声3; 混合回声4
low: 1 and 3
high:2 and 4 
'''
def label2class(label_path, photo_path, class_root_path):
    #data = pd.read_csv(label_path, encoding='utf-8')
    data = pd.read_csv(label_path)
    isClassRootPath = os.path.exists(class_root_path)
    if not isClassRootPath:
        os.mkdir(class_root_path)
        os.mkdir(class_root_path+"/low")
        os.mkdir(class_root_path + "/high")
      #shutil.copyfile(“oldfile”,”newfile”) #oldfile和newfile都只能是文件
      #shutil.copy(“oldfile”,”newfile”) #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
    for line in data.values:
        file_name = str(line[1])+".jpg"  # 获取图像文件名，文件名在csv文件的第18列（从0开始）
        print(file_name)
        file_path = photo_path+"/"+file_name
        if str(line[0]) == "1":  # 获取文件label信息，csv文件共4个label
            shutil.copy(file_path, class_root_path+"/low/"+file_name)
        elif str(line[0]) == "2":
            shutil.copy(file_path, class_root_path+"/high/"+file_name)
        elif str(line[0]) == "3":
            shutil.copy(file_path, class_root_path+"/low/"+file_name)
        elif str(line[0]) == "4":
            shutil.copy(file_path, class_root_path+"/high/"+file_name)

if __name__ == '__main__':
#if __name__ == '__main__':
    label_path = 'D:/SHU/bioCenter/dataSet/huashan_data/labels.csv'
    photo_path = 'D:/SHU/bioCenter/dataSet/huashan_data/img310_CROP'
    class_root_path = 'D:/SHU/bioCenter/dataSet/huashan_data/huashan2class'
    label2class(label_path, photo_path, class_root_path)
