#!/usr/bin/python
# -*- coding: utf-8 -*-

# python replaceFileName.py /Users/wangwei/Desktop/Project/mall/mall/SDFG/SDFGClasses /Users/wangwei/Desktop/Project/mall/mall/qwerasdf.xcodeproj/project.pbxproj UUIO 

import os, re
import os.path
import sys
import getopt

FILTER = ['XIB','Assist','Controller','Model','Xib','View','ViewModel','web','pdf','minified']

def pbRule(cn):
    rule_1 = '/* ' + cn + ' */'
    rule_2 = '= ' + cn + ';'
    rules = []
    rules.append(rule_1)
    rules.append(rule_2)
    return rules

def replaceName(dirname, prefix):
  newDirname = prefix + dirname
  return newDirname

def changePBFile(pbPath, fileDirs, prefix):
    with open(pbPath,"r") as file_read:
        lines = file_read.readlines()
    with open(pbPath,"w") as file_write:
        for line in lines:
            for fileDir in fileDirs:
                oldRules = pbRule(fileDir)
                newRules = pbRule(replaceName(fileDir, prefix))
                for x in range(0,len(oldRules)):
                    if oldRules[x] in line:
                        line = line.replace(oldRules[x],newRules[x])
                        print(line)
            file_write.write(line) #全部类名遍历完后再写

def changeFileName(filePath,pbPath,prefix,suffix):
  fileDirs = []
  #在改文件夹名
  for parent, dirnames, filenames in os.walk(filePath, topdown=True):
    for dirname in dirnames:

      if dirname in FILTER:
        continue
      fileDirs.append(dirname)
      pathdir = os.path.join(parent, dirname)

      newDirname = replaceName(dirname,prefix)
      newPathDir = os.path.join(parent, newDirname)

      os.rename(pathdir, newPathDir)
      print(newPathDir)
  # 修改pb文件内容
  print("-------开始修改pb文件-------")
  changePBFile(pbPath, fileDirs, prefix)
  print("-------处理pb文件完成--------")

#main
opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
filePath = ""
pbPath = ""
prefix = ""
suffix = ""
filePath = args[0]
filePathExist = os.path.exists(filePath)
if filePathExist != 1:
    print("error：" + filePath + "不是有效路径")
    os._exit(0)
pbPath = args[1]
pbPathExist = os.path.isfile(pbPath)
if pbPathExist != 1:
    print("error：" + pbPath + "不是有效文件")
    os._exit(0)
prefix = args[2]
suffix = ""
if prefix == "" and suffix == "":
    print("前缀后缀都为空字符串。。。")
    os._exit(0)
changeFileName(filePath,pbPath,prefix,suffix)
