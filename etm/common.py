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
def send(msg,nickname=""):
    file_tunnel = open("/tmp/easytalk.tunnel", mode='a+')
    p_send = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+" <"+nickname+"> "+msg+"\n"
    file_tunnel.write(p_send)
    file_tunnel.close()

