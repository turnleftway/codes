import os
import shutil
top_path=input("type the path:")
new_postfix=input("type the new postfix (with .):")
origal=input("type the origal name (with postfix):")
store_path=input("type the store_path:")
n=0
for dirs,names,files in os.walk(top_path):
    for file in files:    #遍历指定目录下文件
        splited_files=os.path.splitext(file)
        if file==str(origal) and splited_files[1]!=new_postfix:    #检测后缀是否相同
            n+=1      
            new_files=str(splited_files[0]+str(n))+new_postfix    #更改为新后缀
            os.rename(os.path.join(dirs,file),os.path.join(dirs,new_files))
            print(os.path.join(dirs,new_files))
            shutil.copy(os.path.join(dirs,new_files),store_path)    #复制粘贴已更改的文件 
        elif file==str(origal):
            n+=1
            shutil.copy(os.path.join(dirs,new_files),store_path)
else:
    print("check in")

#去除{file==str(origal) and}，{origal=input("type the origal name (with postfix):")}及{elif file==str(origal):}以更改任意名称文件后缀，但仅能在指定目录下执行，无法对指定名称文件执行
#功能：更改指定目录下指定名称文件后缀，及复制转移更改后文件于另一指定目录
#问题：复制转移仅有一文件，是文件名重复导致