import os
def judgepath(path):
	return os.path.isdir(path)

def changepath():
	prompt1='Please import the path of lyric source files:\n'
	prompt0='Please import the path of music files downloaded in netease application:\n'
	prompt2='Please import the path of output location:\n'
	prompt_error='Path Error! Please import it again!'
	path=['','','']
	path[0]=input(prompt0)
	while not judgepath(path[0]):
		print(prompt_error)
		path[0]=input(prompt0)


	path[1]=input(prompt1)
	while not judgepath(path[1]):
		print(prompt_error)
		path[1]=input(prompt1)


	path[2]=input(prompt2)
	while not judgepath(path[2]):
		print(prompt_error)
		path[2]=input(prompt2)

	with open('finishproject.py','r',encoding='UTF-8') as f_obj:
		lines_list=[]
		for iline in f_obj:
			lines_list.append(iline)
	f_obj.close()
	i=0
	for i in range(0,3):
		lines_list[i]='dir_path'+str(i).strip()+'=r'+'\''+path[i]+'\''+'\n'

	with open('finishproject.py','w',encoding='UTF-8') as f_obj:
		for iline in lines_list:
			f_obj.write(iline)

changepath()
