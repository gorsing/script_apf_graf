# coding=utf-8
import os

file_1 = open ('file.dot','a')
file_1.write('graph graphname {')
def print_dir(path, prefix=u''):
	print u'{}(Dir){}'.format(prefix, os.path.basename(path))
	file_1.write('}'+'\n'+u'subgraph '+str(os.path.basename(path))+u'{'+'\n')
	for item in os.listdir(path):
		p = os.path.join(path, item)
		if os.path.isdir(p):
			#file_1.write('}'+'\n'+u'graph '+str(os.path.basename(path))+u'{'+'\n')
			print_dir(p, prefix + u'|   ')
		else:
			file_1.write('"'+str(item)+'"'+';'+'\n')
			print (str(os.path.join(path, item)))
			print u'{}| |--(f){}'.format(prefix, item)


print_dir('/home/gorsing/test')
file_1.write('}')
