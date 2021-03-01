#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
wwwof - 2019-2021 - por jero98772
wwwof - 2019-2021 - by jero98772
"""
from core.wwwofPage import wwwof
from core.wwwofPage import app as wwwofapp
if __name__=='__main__':
	wwwofapp.run(debug=True,host="0.0.0.0",port=9600)