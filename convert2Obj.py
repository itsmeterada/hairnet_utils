#!/usr/bin/env python
#-*- coding:utf-8 -*-

#
# Usage: convert2Obj.py strands00001.data > strands00001.obj
#

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import struct


def convertToObj(filename):
	print("# ", filename)
	vertexNumber = 1
	prevVertNum = 1
	infile = open(filename, 'rb')
	data = infile.read(4)
	if data:
		numStride = struct.unpack('<i', data)[0]
		#print(numStride)
	for i in range(numStride):
		data = infile.read(4)
		if data:
			numVert = struct.unpack('<i', data)[0]
			#print(numVert)
			startVertNum = vertexNumber
			for j in range(numVert):
				d1 = infile.read(4)
				d2 = infile.read(4)
				d3 = infile.read(4)
				v1 = struct.unpack('<f', d1)[0]
				v2 = struct.unpack('<f', d2)[0]
				v3 = struct.unpack('<f', d3)[0]
				print("v ", v1, v2, v3)
				vertexNumber += 1
			print("l ", end="")
			for j in range(vertexNumber - startVertNum):
				print(j + prevVertNum, " ", end="")
			print("")
			prevVertNum = vertexNumber


def main(filename):
	convertToOBJ(filename)

if __name__ == "__main__":
	args = sys.argv
	filename = ''
	if 1 == len(args):
		print('Need a file')
		quit()
	else:
		filename = args[1]
	main(filename)
