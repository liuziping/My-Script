#!/usr/bin/env  python
#coding:utf-8

def big_file(file):
    BLOCK_SIZE = 100
    with open(file, 'r') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
                #return block
            else:
                return 

if __name__ == "__main__":
    a = big_file("weixinapi.py")
    for i in a:
        print i

