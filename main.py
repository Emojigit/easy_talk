#!/usr/bin/python3
"""
    Copyright (c) 2020 Cato Yiu
    
    This file is part of Easy Talk.

    Easy Talk is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 2.1 of the License, or
    (at your option) any later version.

    Easy Talk is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with Easy Talk.  If not, see <https://www.gnu.org/licenses/>.
"""
import os, sys, time, multiprocessing
from datetime import datetime
from etm import command, common
nickname = input("Please Choose a nickname: ")
if nickname == "":
    exit()
os.system("clear")
b = ""

def updated():
    while True:
        file_tunnel = open("/tmp/easytalk.tunnel", mode='r')
        global b
        d = ""
        try:
            d = file_tunnel.readlines()[-1]
        except IndexError:
            pass
        if d != b:
            print(d)
            b = d
        file_tunnel.close()

os.nice(1)

p = multiprocessing.Process(target=updated)
p.start()


common.send(nickname+" joined chat")
try:
    while True:
        try:
            x = input()
            print("\033[A                      \033[A")
            if x[0] == "/":
                sp = x.split("/",1)[1] 
                command.cmd_h(sp,p,nickname)
                continue
            common.send(x,nickname)
        except KeyboardInterrupt:
            print("\n")
            continue
except EOFError:
    p.kill()
    exit()
