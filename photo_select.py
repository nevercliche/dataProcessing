import os, random, shutil
def moveFile(fileDir,tarDir):
        pathDir = os.listdir(fileDir)    #取图片的原始路径
        filenumber=len(pathDir)
        rate=1                       #自定义抽取图片的比例，比方说100张抽10张，那就是0.1
        picknumber=int(filenumber*rate) #按照rate比例从文件夹中取一定数量图片
        sample = random.sample(pathDir, picknumber)  #随机选取picknumber数量的样本图片

        for name in sample:
            shutil.move(fileDir+name, tarDir+str(name)+'.jpg')
            

if __name__ == '__main__':
    fileDir = "D:/SHU/bioCenter/dataSet/renji_data/doctor_confirmed/renji2class/high/"    #源图片文件夹路径
    tarDir  = "D:/SHU/bioCenter/dataSet/renji_data/doctor_confirmed/seg_renji2class/test/high/"       #移动到新的文件夹路径
    
    '''for oneDir in os.listdir(fileDir):
        onefileDir = fileDir+oneDir+"/"  # A的二级目录
        # 判断文件夹是否存在，不存在则创建
        if not os.path.exists(onefileDir):
            os.makedirs(onefileDir)
        if not os.path.exists(tarDir):
            os.makedirs(tarDir)

        i = moveFile(onefileDir,tarDir,i)+1'''
    if not os.path.exists(tarDir):
            os.makedirs(tarDir)
    moveFile(fileDir,tarDir)
