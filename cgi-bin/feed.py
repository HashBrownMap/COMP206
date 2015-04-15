#!/usr/bin/python
import sys
import cgi
import csv
import cgitb
import os
import shutil
cgitb.enable()

def usertousername(use):
	f = open('members.csv', mode = 'rt')
	for line in f:
		if "%s"%use in line:
			text = line.split(' ')
			if use == text[0]:
				user_name = text[1]
				
				return user_name

def findfriends(user):
    ref = open("members.csv", "r")
    lst = []
    friend_lst = []
    for line in ref:
        lst.append(line)
    ref.close()
    for x in range(0, len(lst)):
        lst[x] = lst[x].strip()
        lst[x] = lst[x].split(" ")
        if (lst[x][1] == user):
            for y in range(3, len(lst[x])):
                friend_lst.append(lst[x][y])
    return friend_lst

def isfriends(me, him):
    if him in findfriends(me):
        return True
    elif me==him:
        return True
    else:
        return False

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

form = cgi.FieldStorage()
username = form.getvalue("user")

list = open('members.csv', mode='rt')

if not(form.has_key("user")):
	print"<meta http-equiv=\"refresh\" content=\"0;url=http:\/\/www.cs.mcgill.ca/~zchen66\"\>"

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
	f.writelines('%s\n%s\n'%(name, message))
	exit
f.close()


print"""<h3 style="background-color:black">
            <FONT FACE="futura" size="5" color="white"><center>News Feed</center></FONT>
        </h3>"""

newsfeed = open("topics.csv", "r")
lst = []
who = []
status = []
for line in newsfeed:
	lst.append(line)
newsfeed.close()
for x in range(0, len(lst)):
	if x % 2 == 0:
		who.append(lst[x].strip())
	else:
		status.append(lst[x].strip())
who.reverse()
who.reverse()

del lst[:]
for x in range(0, len(who)):
	a = who[x]
	friend = usertousername(a)
	b = status[x]
	c = (a, b)
	if isfriends(username, friend):
		lst.insert(x, c)
lst=lst[0:10]


for i in range(0, len(lst)):
	lst[i]="\n:\n".join(lst[i])

string = "<br><br>".join(lst)

print "<center><h3>%s</h3></center>"%string





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

if not (form.has_key("friend")):
        print "<center><H4>please input an username</H4></center>"
        exit
else:
	friend = form.getvalue("friend")
	temp = open('temp', 'wb')
	with open('members.csv', 'r') as list:
		for line in list:
			if "%s"%username in line:
				if "%s"%friend in line:
					print "<center><H4>%s is already your friend</H4></center>"%friend
					exit
				else:
					line = line.strip() + " %s\n"%friend
			temp.write(line)
	temp.close()
	shutil.move('temp', 'members.csv')

print"""<center><img src="http://cdn2.pitchfork.com/news/58263/547cb710.png"width="200" alt="North and West"></center>

<h3 style="background-color:black">
          <FONT FACE="futura" size="4" color="white"><center> <a href="http://cs.mcgill.ca/~zchen66">Logout</a></center></FONT></h3>

   </body>
</html>"""

