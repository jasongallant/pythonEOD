#!/usr/bin/env python

import array
import struct
import sys
import pylab
import matplotlib.pyplot as plt

inputfile = sys.argv[1]
k=0
versions=[]
nchars=[]
wavetexts=[]
nbitss=[]
nbytess=[]
polarities=[]
userdatas=[]
samprates=[]
adranges=[]
nptss=[]
waves=[]

with open(inputfile, 'rb') as data:
	while True:
		try:
			version, nchar = struct.unpack('<ch', data.read(3))
			wavetext=data.read(nchar)
			nbits,nbytes,polarity=struct.unpack('<ccc', data.read(3))
			userdata=struct.unpack('<6f',data.read(24))
			samprate=struct.unpack('<L',data.read(4))[0]
			adrange=struct.unpack('<f',data.read(4))[0]
			npts=struct.unpack('<l',data.read(4))[0]
			mynpts="<"+str(npts)+"h"
			wave=struct.unpack(mynpts,data.read(2*npts))

			versions.append(version)
			nchars.append(nchar)
			wavetexts.append(wavetext)
			nbitss.append(nbits)
			nbytess.append(nbytes)
			polarities.append(polarity)
			userdatas.append(userdata)
			samprates.append(samprate)
			adranges.append(adrange)
			nptss.append(npts)
			waves.append(wave)

			# print "version=",version,"\n"
			# print "nchar=",nchar,"\n"
			# print wavetext,"\n"
			# print "nbits=",nbits,"\n"
			# print "nbytes=",nbytes,"\n"
			# print "userdata=",userdata,"\n"
			# print "samprate=",samprate,"\n"
			# print "adrange=", adrange, "\n"
			# print "npts=", npts, "\n"
			# print "wave=",wave,"\n"
			k=k+1
		except :
		  	break
		  	print "EOF Reached."

# print nchars
# print k

for i in range(0,k):
	fig = plt.figure()
	ax=fig.add_subplot(111)
	x_points=xrange(0,nptss[i])
	y_points=waves[i]
	p=ax.plot(x_points,y_points,'b')
	ax.set_xlabel('time')
	ax.set_ylabel('voltage')
	ax.set_title(wavetexts[i])
	fig.show()




