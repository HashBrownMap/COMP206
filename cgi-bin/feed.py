#!/usr/bin/python
import sys
import cgi
import cgitb
cgitb.enable()



print "Content-Type: text/html"
print

print "<title>NEWS FEED</title>"

print """<head>
        <meta charset="utf-8">
        <title>Feed Page</title>
    </head>
    <body bgcolor="black">
        <h1 style="background-color:black">
            <FONT FACE="impact" color="white" size="24">
            <br>
                <center>WELCOME [username]</center>
            </FONT>
            <br>
            <FONT FACE="futura" size="4" color="black">
            <a href="http://cs.mcgill.ca/~ldunba/"><div align="right">Logout</div></a>
            </FONT>
        </h1>
        <h3 style="background-color:white">
            <FONT FACE="futura" size="5" color="black"><center>Status Update</center></FONT></h3>
        <center><form action="./cgi-bin/feed.py" method="POST"><input type="text" name="status" size="140" style="height:50px; width:500px"><br>
            <input type="submit" value="Update Status">
        </form></center>

<center><img src="./Kanye.jpg"width="1150" alt="Image could not load, Kim sends her condolences"></center>"""

print """<center><h2><font color="color">"""

with open('topics.csv') as news:
	for line in news:
		print "%s<br>" % line
print "</font> </h2></center>"
print """        <h3 style="background-color:white">
            <FONT FACE="futura" size="5" color="black"><center>Kan-ye be my Friend?</center></FONT></h3>
        <center><form action="NEW FRIEND" method="POST"><FONT FACE="futura"><small>Enter a user to add them to your feed</small><br> </FONT><input type="text" name="status" size="30"><br>
            <input type="submit" value="Add Frend">
        </form></center>


    </body>
</html>"""





