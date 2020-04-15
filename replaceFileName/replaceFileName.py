#-- coding:UTF-8 --
import os, re
import os.path

rootdir = '/Users/wangwei/Desktop/Project/mall/mall/mall'

print('absolute root path:\n*** ' + rootdir + ' ***')

# 先修改文件名,循环文件夹和子文件夹，文件名
for dirname, subdir, filenames in os.walk(rootdir):
  for filename in filenames:
    pathfile = os.path.join(dirname, filename)
    euroFilename = re.search(r'([a-zA-Z]+)(-|$)?([a-zA-Z]+)',filename)
    mvfile = euroFilename.group() + '.yml'
    mvpathfile = os.path.join(dirname,mvfile)
    if 'shtel' in filename:
        continue
    elif 'gateway' in filename:
        continue
    os.rename(pathfile, mvpathfile)

#在改文件夹名
for parent, dirnames, filenames in os.walk(rootdir, topdown=False):
  for dirname in dirnames:
    pathdir = os.path.join(parent, dirname)
    euroFilename = re.search(r"(\bstage\b)?-?([a-zA-Z1]+)(-[a-zA-Z1]+)?(-conf)?(-master)?", dirname)
    mvpathdir = os.path.join(parent, euroFilename.group())
    os.rename(pathdir, mvpathdir)
    pathname = [euroFilename.group(2), euroFilename.group(3), euroFilename.group(5)]
    if pathname[1] == None:
        continue
    pathdirs = ''.join(pathname)
    pathnames = os.path.join(parent, pathdirs)
    os.rename(mvpathdir, pathnames)     #去掉文件夹的stage字段
