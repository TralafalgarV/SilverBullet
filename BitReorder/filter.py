#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import sys
import getopt

def filterText(filepath, newFilepath):
  line_set = set()

  with open(filepath, "r") as file_read:
    lines = file_read.readlines()
  with open(newFilepath, "w") as file_write:
    for line in lines:
      if 'sname' in line:
        line = line.replace('sname=', '', 1)
        line = line.replace('__', '___', 1)

        if line not in line_set:
          line_set.add(line)
          file_write.write(line) #全部类名遍历完后再写

#main 
filepath = './BitReorder.txt'
newFilepath = './NewBitReorder.txt'
filterText(filepath, newFilepath)