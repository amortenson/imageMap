#!/usr/bin/python
print 'Content-Type: text/html'
print

import os,sys
from PIL import Image

im = Image.open('image1.jpeg','r') #loads image to 'pic'
pic = im.load()

f=open('text1.txt','r') #reads text to 'text1'
text1=f.read()
f.close()
#text1=text1.replace('\n','<br>')

f = open('output.txt','w') #maps image into output.txt in the form of 1 for dark pixel, 0 for light pixel, and , for line break
width,height = im.size
for y in range (height):
    for x in range (width):
        a,b,c = pic[x, y]
        value = (a+b+c)/3
        if value<128:
            value=0
        else:
            value=1
        f.write(str(value))
    f.write(',')
f.close

f=open('output.txt','r') #reads output.txt to 'text'
text=f.read()
f.close()
text=text.strip(',')

head="<html><body><center>"

st="<table bgcolor='grey'><tr><td>"
a=0
for n in range(((len(text1)*51))/50):
   if text[n]=='1':
       st+= "<font face='Courier' color='white'>"+text1[a]+"</font>" #This font must be used because every character, including the space, is the same length.
       a+=1
   if text[n]=='0':
       st+= "<b><font face='Courier' color='black'>"+text1[a]+"</font></b>"
       a+=1
   if text[n]==',':
       st+= "<br>"
       text.replace(',','',1)
       if text[n]=='1':
           st+= "<font face='Courier' color='white'>"+text1[a]+"</font>"
       if text[n]=='0':
           st+= "<b><font face='Courier' color='black'>"+text1[a]+"</font></b>"
st+="</td></tr></table>"
    
bot= "</center></body></html>"

page=head+st+bot

print page #prints html text

f = open('page.html','w') #saves printed output to 'page.html' (to make testing easier)
f.write(page)
f.close()
