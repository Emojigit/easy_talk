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
from etm import common
import colorama
import os, sys, time, multiprocessing
from datetime import datetime
from colorama import Fore, Style
from termcolor import colored
def cmd_h(cmd,p,nickname):
    cmd_a = cmd.split(" ")
    cmd_m = cmd_a[0]
    if cmd_m == "exit":
        p.kill()
        exit(0)
    elif cmd_m == "color":
        color = cmd_a[1]
        text = cmd.split(" ",2)[2]
        try:
            common.send(colored(text,color),nickname)
        except KeyError:
            print("color: Color not found")
    else:
        print(sp+": Command not found")
