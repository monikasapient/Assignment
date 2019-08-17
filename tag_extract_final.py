#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 22:02:28 2019

@author: monahirw
"""

import sys
import re
import argparse

class tag_parser():
    def __init__(self, mainfile):
        self.mainfile = mainfile
        
        
    def extract_only_tag(self):
        f = open(self.mainfile)
        tag_set = []
        for line in f:
            extracted_tag = re.findall(r"<\w*>",line)
            if len(extracted_tag)!=0:
                opener = "<"
                closer = ">"
                i = line.index(opener)
                start =  i + len(opener)
                j = line.index(closer, start)
                tag_set.append(line[start:j])
        f.close()
        return tag_set
    
    def parent_of_child(list):
        print(list)
        return list
    
    
    def parent_of_tag(self):
        stack = []
        f = open(self.mainfile)
        for line in f:
            x=re.findall(r"<(.+?/*)>",line)
            for j in x:
                if(len(stack)==0):
                    stack.append(j)
                elif len(stack)!=0:
                    m = stack.pop()
                    if "/" +  m!=j:
                        stack.append(m)
                        stack.append(j)
                    else:
                        print("parent of",m)
                        parent_of_child(stack)
	
        f.close()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', type=str)
    args = parser.parse_args()
    mainfile = args.file
    extractor = tag_parser(mainfile)
    
    
    
    
    
    
    
    
    
    
    
    

    
        
        
        
        
        
