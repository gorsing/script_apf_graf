# coding=utf-8
import os

def print_dir(path, prefix=u''):
	print u'{}(Dir){}'.format(prefix, os.path.basename(path))
	file_1.write('}'+'\n'+u'subgraph '+'"'+str(os.path.basename(path))+'"'+u'{'+'\n'+'node [shape="circle", style="filled", fillcolor="blue",fontcolor="black"];'+'\n')
	for item in os.listdir(path):
		p = os.path.join(path, item)
		if os.path.isdir(p):
			#file_1.write('}'+'\n'+u'graph '+str(os.path.basename(path))+u'{'+'\n')
			print_dir(p, prefix + u'|   ')
		else:
			file_1.write('"'+str(item)+'"'+';'+'\n')
			print (str(os.path.join(path, item)))
			print u'{}| |--(f){}'.format(prefix, item)

def t_dir2(path, prefix=u''):
	print u'{}(Dir){}'.format(prefix, os.path.basename(path))
	file_1.write('"'+str(os.path.basename(path))+'";'+'\n')
	for item in os.listdir(path):
		p = os.path.join(path, item)
		if os.path.isdir(p):
			file_1.write('"'+str(os.path.basename(path))+'"--')
			t_dir2(p, prefix + u'|   ')
		else:
			#file_1.write('"'+str(item)+'"'+';'+'\n')
			print (str(os.path.join(path, item)))
			print u'{}| |--(f){}'.format(prefix, item)

file_1 = open ('file.dot','a')
file_1.write('graph graphname {node [shape="box", style="filled", fillcolor="green", fontcolor="black", fontsize="9"];'+'\n')


t_dir2('/home/gorsing/script_afs_graf/test')
print_dir('/home/gorsing/script_afs_graf/test')
file_1.write('}')



