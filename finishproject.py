dir_path0=r'C:\OrganicFish\Music\cloudmusic'
dir_path1=r'C:\Users\OrganicFish\AppData\Local\Netease\CloudMusic\webdata\lyric'
dir_path2=r'C:\OrganicFish\Music\done'



import re
import os
import time
import shutil


# 获取按时间顺序排序的文件名
def filesindirtodic(dir_path):
	dir_files=os.listdir(dir_path)
	dic={}
	for ifile in dir_files:
		f_path=dir_path+'\\'+ifile
		dic[f_path] = os.path.getctime(f_path)
	return sorted(dic)

#删除目录下所有文件
def deldir(dir_path):
	dir_files=os.listdir(dir_path)
	for ifile in dir_files:
		f_path=dir_path+'\\'+ifile
		os.remove(f_path)

#将文件转化成lrc文件
def disposefiles(file_path,file_name):
	s=''
	with open(file_path,'r',encoding='UTF-8') as file_obj:
		for line in file_obj:
			for iword in line.strip():
				s=s+iword
	file_obj.close()
	lyrics=re.split("\\\\n",s)
	del lyrics[0]
	if len(lyrics) != 0:
		lyrics.pop()

	newpath=file_name+'.lrc'
	nf_obj=open(newpath,'w',encoding='UTF-8')
	for lyric in lyrics:
		nf_obj.writelines(lyric+'\n')
	nf_obj.close()
	


dir_list1=filesindirtodic(dir_path0)
dir_list2=filesindirtodic(dir_path1)

for i in range(0,len(dir_list1)):
	f_name=dir_path2+'\\'+os.path.splitext(os.path.basename(dir_list1[i]))[0]
	targetpath=dir_path2+'\\'+os.path.basename(dir_list1[i])
	disposefiles(dir_list2[i],f_name)
	shutil.move(dir_list1[i],targetpath)
deldir(dir_path1)


