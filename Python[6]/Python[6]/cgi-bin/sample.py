#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import html
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
numb1 = form.getfirst("numb1")
numb2 = form.getfirst("numb2")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
		<html>
		<head>
		<meta charset="utf-8">
		<title>Python[6]</title>
		<link rel="stylesheet" href="../styles.css">
		</head>
		<body>""")

print('<form action="/cgi-bin/sample.py">')
print("<table>")
print("<tr><th>Розрахунок частки:</th></tr>")
print('<tr><td><input type="number" name="numb1" step="0.01" value="{}"><br><hr>'.format(numb1))
print('<input type="number" name="numb2" step="0.01" value="{}">'.format(numb2))	
print('<div style="text-align:center;">')
print('<br><input type="submit" value="Обчислити"></div>')

if numb1 == None or numb2 == None:
	print('<br><input type="text" name="result" value="{}" disabled>'.format("не усі поля заповнені"))
if int(numb2) == 0:
	print('<br>')
	print('<input type="text" name="result" value="{}" disabled>'.format("знаменник = 0"))

else:
	result = float(numb1)/float(numb2)
	print('<br><input type="text" name="result" value="{}" disabled>'.format(result))
	form["numb1"].value = numb1
	form["numb2"].value = numb2

print("</td></tr></table></form>")
print("""</body></html>""")