#!/usr/bin/env python

import array
import struct
import sys

inputfile = sys.argv[1]

with open(inputfile, 'rb') as data:
	version, nchar = struct.unpack('<ch', data.read(3))
	wavetext=data.read(nchar)
	nbits,nbytes,polarity,=struct.unpack('<ccc', data.read(3))
	userdata=struct.unpack('<6f',data.read(24))
	samprate=struct.unpack('<L',data.read(4))[0]
	adrange=struct.unpack('<f',data.read(4))[0]
	npts=struct.unpack('<l',data.read(4))[0]
	wave=struct.unpack('<1024h',data.read(2*npts))


	print "version=",version,"\n"
	print "nchar=",nchar,"\n"
	print wavetext,"\n"
	print "nbits=",nbits,"\n"
	print "nbytes=",nbytes,"\n"
	print "userdata=",userdata,"\n"
	print "samprate=",samprate,"\n"
	print "adrange=", adrange, "\n"
	print "npts=", npts, "\n"
	print "wave=",wave,"\n"



