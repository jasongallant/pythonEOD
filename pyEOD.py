#!/usr/bin/env python

import array
import struct
import sys
import pylab
import matplotlib.pyplot as plt
import collections
import array
import struct
import sys
import numpy

eod = collections.namedtuple('eod',['version','nchar','wavetext','nbits','nbytes','polarity','userdata','samprate','adrange','npts','wave','time'])

def openeod(inputfile):
	eod_files=[]
	k=0
	with open(inputfile, 'rb') as data:
		while True:
			try:
				print k
				# read all of the data in from binary
				version, nchar = struct.unpack('<ch', data.read(3))
				wavetext=data.read(nchar)
				nbits,nbytes,polarity=struct.unpack('<ccc', data.read(3))
				userdata=struct.unpack('<6f',data.read(24))
				samprate=struct.unpack('<L',data.read(4))[0]
				adrange=struct.unpack('<f',data.read(4))[0]
				npts=struct.unpack('<l',data.read(4))[0]
				mynpts="<"+str(npts)+"h"
				wave=struct.unpack(mynpts,data.read(2*npts))
				time=numpy.linspace(0,1000*npts/samprate,num=npts)

				#place the data in a named tuple, as defined above...
				myeod=eod(version=version,nchar=nchar,wavetext=wavetext,nbits=nbits,nbytes=nbytes,polarity=polarity,userdata=userdata,samprate=samprate,adrange=adrange,npts=npts,wave=wave,time=time)
				eod_files.append(myeod)
				k=k+1
			except :
			  	break
			  	#Stop When I Reach the End of File...
		return eod_files

def printalleods(eod_files):
	k=len(eod_files)

	for i in range(0,k):
		fig = plt.figure()
		ax=fig.add_subplot(111)
		x_points=eod_files[i].time
		y_points=eod_files[i].wave
		p=ax.plot(x_points,y_points,'b')
		ax.set_xlabel('time')
		ax.set_ylabel('voltage')
		ax.set_title(eod_files[i].wavetext)
		fig.show()
	#raw_input() # hold open until return is pressed.

def printeod(eod_files,i):
	fig = plt.figure()
	ax=fig.add_subplot(111)
	x_points=eod_files[i].time
	y_points=eod_files[i].wave
	p=ax.plot(x_points,y_points,'b')
	ax.set_xlabel('time')
	ax.set_ylabel('voltage')
	ax.set_title(eod_files[i].wavetext)
	fig.show()
	
	#raw_input() # hold open until return is pressed.

def normalizeall_p1(eod_files):
	k=len(eod_files)
	norm_eods=[]
	for i in range (0,k):
		baseline = numpy.mean(eod_files[i].wave[1:100]) #changed to 40 JRG
		newwave = eod_files[i].wave-baseline
		ymax= numpy.max(newwave)
		ymin = numpy.min(newwave)
		ivmax=numpy.argmax(newwave)
		ivmin=numpy.argmin(newwave)
		newwave = newwave/(ymax-ymin)
		newtime = eod_files[i].time - (eod_files[i].time[ivmax])
		thenewnorm=eod(version=eod_files[i].version,nchar=eod_files[i].nchar,wavetext=eod_files[i].wavetext,nbits=eod_files[i].nbits,nbytes=eod_files[i].nbytes,polarity=eod_files[i].polarity,userdata=eod_files[i].userdata,samprate=eod_files[i].samprate,adrange=eod_files[i].adrange,npts=eod_files[i].npts,wave=newwave,time=newtime)
		norm_eods.append(thenewnorm)

	return norm_eods




