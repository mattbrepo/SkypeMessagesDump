import os
import sqlite3
import time
import re
import sys

#
#
# Main
#
#

filename_db = "l__main.db"
filename_out = filename_db + ".txt"

fw = open(filename_out, 'w')

con = sqlite3.connect(filename_db)
cur = con.cursor()

cur.execute("SELECT id, author, chatname, body_xml FROM messages WHERE not body_xml = 'NULL'")
row = cur.fetchone()
while row is not None:
  # xml => txt
  text = re.sub('<[^<]+>', "", row[3])

  # newline => ','
  text = text.replace("\r\n", ",")
  text = text.replace("\n", "")

  # utf-8 encoding
  text = str(text.encode('ascii', 'ignore'))

  # compone line_out
  line_out = str(row[0]) + ";" + row[1] + ";" + row[2] + ";" + text

  # scrittura file
  fw.write("%s\n" % line_out)
  row = cur.fetchone()

fw.close()
cur.close()
con.close()

print("done!")