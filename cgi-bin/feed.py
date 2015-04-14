#!/usr/bin/python
import sys
import cgi
import csv
import cgitb
import os
cgitb.enable()
 
 
 
print "Content-Type: text/html"
print
 
print "<title>NEWS FEED</title>"
 
print """
<html>
   <head>
       <meta charset="utf-8">
       <title>Feed Page</title>
   </head>
   <body bgcolor="white">
   <center><img src="./Kanye.jpg"width="1250" alt="Image could not load, Kim sends her condolences"></center>
"""   

name = cgi.FieldStorage()
username = name.getvalue("user")

list = open('members.csv', mode='rt')
for line in list:
	if "%s"%username in line:
		text = line.split(' ')
		if username == text[1]:
			name = text[0]



print"""       <h1 style="background-color:white">
           <FONT FACE="futura" color="black" size="26">
           <br><center>"""
print"%s" % name
print"""          </center> </FONT>
       </h1>
       
       <h3 style="background-color:black">
           <FONT FACE="futura" size="5" color="white"><center>Status Update</center></FONT></h3>"""

print """ <center><form action="./feed.py" method="GET">
	<input type="text" name="status" size="200">"""
print"	<input type=\"hidden\" name=\"user\" value=\"%s\">" % username
print """           <input type="submit" value="Update Status">
       </form></center>"""

f = open('topics.csv', mode='at')



form = cgi.FieldStorage()
if not (form.has_key("status")):
        print "<center><H4>your status update appears to be blank</H4></center>"
	exit
else:
	message = form.getvalue("status")
	f.writelines('%s %s \n'%(name, message))
	exit
f.close()


print"""<h3 style="background-color:black">
            <FONT FACE="futura" size="5" color="white"><center>News Feed</center></FONT>
        </h3>"""
 
 
with open('topics.csv') as news:
        for line in news:
		who = line[:max(line.find(' '), 0) or None]
		print "<font face=\"futura\" size=\"4\"> <b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s: <br></b> </font> " %who
		info = line.split(' ',1)[1]
                print "<font face=\"futura\" size=\"4\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; %s<br><br>" % info
 
 
print """ 
<h3 style="background-color:black"><FONT FACE="futura" size="5" color="white"><center>All Current Members</center></FONT></h3>
 
<div>
   <center> <table>
            <tr>
                <th><font face="futura" color="gray"><span class="text"><u></u></span></font></th>
            </tr>
        
        <tbody>
        <tr><td>
	<font face="futura" color="black">
	<select size="8" width="300">	"""
	
with open("members.csv") as members:
        for line in members:
		text = line.split(' ')
		namee = text[0]
		usern = text[1]
		print "<option>%s -username: %s</option><br>"%(namee,usern)
print"""
	</font></td>
        </tr>
        </tbody>
   </center> </table>
  </div>
 
        <h3 style="background-color:black">
           <FONT FACE="futura" size="5" color="white"><center>Kan-ye be my Friend?</center></FONT></h3>
       
<center><form action="./feed.py" method="GET"><FONT FACE="futura"><small>Enter a USERNAME to follow them</small><br> </FONT><input type="text" name="friend" size="30"><br>"""
print "<input type=\"hidden\" name=\"user\" value=\"%s\">" % username
print """           <input type="submit" value="Add Friend">
       </form></center>"""
form = cgi.FieldStorage()

#addlist = open('members.csv', 'ra')


#if not(form.has_key("friend")):
#	print"<center><h4>You didn't enter a username.</h4></center>"
#else:
#	add = form.getvalue("friend")

#with open('members.csv', 'w+b') as addlist:	
#	lines = addlist.readlines()
#	for i, line in enumerate(lines):
#		if "%s"%username in line:
#			line[i] = line[i].strip() + "%s"%add
#	addlist.seek(0)
#	for line in lines:
#		addlist.write(line)
#addlist.close()

print"""<center><img src="http://cdn2.pitchfork.com/news/58263/547cb710.png"width="200" alt="North and West"></center>

<h3 style="background-color:black">
          <FONT FACE="futura" size="4" color="white"><center> <a href="http://cs.mcgill.ca/~zchen66">Logout</a></center></FONT></h3>

   </body>
</html>"""

