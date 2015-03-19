# coding=utf-8
import os

def t_dir2(path, prefix=u''):
	print u'{}(Dir){}'.format(prefix, os.path.basename(path))
	file_1.write('"'+str(os.path.basename(path))+'";'+'\n')
	for item in os.listdir(path):
		p = os.path.join(path, item)
		if os.path.isdir(p):
			file_1.write('"'+str(os.path.basename(path))+'"--')
			t_dir2(p, prefix + u'|   ')
		else:
			file_1.write('"'+str(item)+'"'+';'+'\n')
			print (str(os.path.join(path, item)))
			print u'{}| |--(f){}'.format(prefix, item)

file_1 = open ('file.dot','a')
file_1.write('graph graphname {')



t_dir2('/home/gorsing/script_afs_graf/test')
