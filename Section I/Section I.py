import os
import jdcal
import et_xmlfile
import openpyxl

from tkinter import *
root = Tk()
root.filename = filedialog.askopenfilename()
txtfile = open(root.filename,'r+')

Filename = root.filename.split('Level I/',1)[1]

root.destroy()
Pythondata = txtfile.read()

from openpyxl import Workbook
wb = Workbook()
ws = wb.active

getHeaders = Pythondata.split('DF',1)[1]
getHeaders = getHeaders.split('\n;',1)[1]
getHeaders = getHeaders.split('\n',1)[0]
getHeaders = getHeaders.split()
getHeaders.extend(['line_number','file_name','config','sensor_number'])
getHeaders.insert(0,'TimeSys')
ws.append(getHeaders)

sensor_number = Pythondata.split('SSN=',1)[1]
sensor_number = sensor_number.split(',',1)[0]

if 'sync' in Pythondata:
    SplitString = Pythondata.split('sync ',1)
    line_number = 2+ SplitString[0].count('\n')

    Date_Time = SplitString[1].split('\n',1)[0]
    month = Date_Time[8:10]
    day = Date_Time[5:7]
    year = Date_Time[0:4]
    time = Date_Time[11:len(Date_Time)]
    seconds = time[6:8]

    newDate_Time = month+'/'+ day + '/' +year + ' ' + time

    realData = SplitString[1].split('\n',1)[1]
    numColumns = realData.count('\n')+1
else:
    SplitString = Pythondata.split('Messages',1)
    line_number = 2 + SplitString[0].count('\n')

    newDate_Time = '06/11/2015 08:00:00'
    time = '08:00:00'
    month = '06'
    day = '11'
    year = '2015'
    seconds = '00'
    
    realData = SplitString[1].split('\n',1)[1]
    numColumns = realData.count('\n')


for x in range(numColumns):
    currentline = realData.split('\n',1)[0]
    breakapart = currentline.split()
    breakapart.insert(0,newDate_Time)

    subarray = ['',str(line_number),Filename,'',sensor_number]
    breakapart.extend(subarray)
    line_number += 1
    
    newseconds = str(int(seconds)+1)
    if len(newseconds)==1:
        newseconds='0'+newseconds
    newtime = time[0:6]+newseconds
    newDate_Time = month+'/'+ day + '/' +year + ' ' + newtime
    seconds = newseconds

    
    ws.append(breakapart)
    if x<(numColumns-1):
        realData = realData.split('\n',1)[1]

wb.save(Filename+".xlsx")


