#!/usr/bin/python3
ch = 97
while ch <= 122:
	if ch != 101:
		if ch != 113:
			print("{}" .format(chr(ch)), end='')
			ch += 1
