#!/usr/bin/python
import sys
import urlparse
import cgi
import urllib2
import urllib
import cgitb
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


username = urllib.urlencode({'user': 0})
f = urllib.urlopen("http://www.cs.mcgill.ca/~zchen66/cgi-bin/query?%s" % username)

with open("members.csv") as list:
	for line in list:
		if username in line:
			name = line[:max(line.find(' '), 0) or None]



print"""       <h1 style="background-color:white">
           <FONT FACE="futura" color="black" size="26">
           <br><center>"""
print"%s" % f
print"""          </center> </FONT>
           <br>
           <FONT FACE="futura" size="4" color="black">
           <a href="http://cs.mcgill.ca/FIX THIS"><div align="right">Logout</div></a>
           </FONT>
       </h1>
       
       <h3 style="background-color:black">
           <FONT FACE="futura" size="5" color="white"><center>Status Update</center></FONT></h3>"""

print """ <center><form action="./feed.py" method="POST">
	<input type="text" name="status" size="200">
	<input type="hidden" name="username" value=" "><br>
           <input type="submit" value="Update Status">
       </form></center>"""

f = open('topics.csv', mode='at')

form = cgi.FieldStorage()
if not (form.has_key("status")):
        print "<center><H4>your status update appears to be blank</H4></center>"
	exit
else:
        message = form.getvalue("status")
        f.writelines('%s \n'%(message))
	exit
f.close()


print"""<h3 style="background-color:black">
            <FONT FACE="futura" size="5" color="white"><center>News Feed</center></FONT>
        </h3>"""
 
print """<center><h2><FONT FACE="futura" size="4" color="black">"""
 
with open('topics.csv') as news:
        for line in news:
                print "%s<br>" % line
print "</FONT> </h2></center>"
 
 
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
	<select size="8" width="200">	
	//PRINT OUT THE USERNAMES OF MEMBERES//

	</font></td>
        </tr>
        </tbody>
   </center> </table>
  </div>
 
        <h3 style="background-color:black">
           <FONT FACE="futura" size="5" color="white"><center>Kan-ye be my Friend?</center></FONT></h3>
       
<center><form action="NEW FRIEND" method="POST"><FONT FACE="futura"><small>Enter a user to add them to your feed</small><br> </FONT><input type="text" name="status" size="30"><br>
           <input type="submit" value="Add Friend">
       </form></center>
       
           <center><img src="http://cdn2.pitchfork.com/news/58263/547cb710.png"width="75" alt="North and West"></center>
   </body>
</html>"""

