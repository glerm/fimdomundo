#-*- coding: utf-8 -*-

import sys

search=str(sys.argv[1])

with open("formatado.txt", "r") as arq:
    for linha in arq:
        if linha.find(search) > -1:
            print linha
