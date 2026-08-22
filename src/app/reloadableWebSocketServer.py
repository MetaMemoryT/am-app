import os
import json
from http.cookies import SimpleCookie
import sqlite3
import re
from decimal import Decimal, ROUND_05UP, ROUND_HALF_UP

cents = Decimal('0.01')

base_path = "../"

# sessionUsernameMap = {
#     "a1":"John Doe"
# }

conn= sqlite3.connect('data.db')
 
# cursor object
cur = conn.cursor()

base_path = "../"

def installFor(t,l):
    m = re.search("{for.+\n",t)
    header = t[0:m.start()]
    rest = t[m.end():]
    m2 = re.search("\{end for\}", rest)
    #print(m.end())
    inner = rest[0:m2.start()]
    #print(header)
    #print(rest)
    #print(inner)
    footer = rest[m2.end():]
    #print(footer)
    t2 = header
    for e in l:
        t2 += re.sub("{e}", e, inner)
    t2+=footer
    return t2

def setResponseOk():
	global responseOk
	responseOk = True

def basic_headers(self):
	self.send_response(200)
	self.send_header("Content-type", "text/html")
	self.end_headers()

def simpleCss(self, url):
	if self.path == url:
		setResponseOk()
		self.send_response(200)
		self.send_header('Content-type','text/css')
		self.end_headers()
		global base_path
		head, tail = os.path.split(url)
		file_path = base_path + "src/app/css/" + tail
		print("file_path: ",  file_path)
		f = open(file_path, "rb")
		self.wfile.write(f.read())
		f.close()

def simpleJs(self, url):
	if self.path == url:
		setResponseOk()
		self.send_response(200)
		self.send_header('Content-type','text/js')
		self.end_headers()
		global base_path
		head, tail = os.path.split(url)
		file_path = base_path + "src/app/js/" + tail
		print("file_path: ",  file_path)
		f = open(file_path, "rb")
		self.wfile.write(f.read())
		f.close()

def installVals(t, dict):
	t2 = t
	for k in dict:
		t = re.sub("{" + k + "}", dict[k], t2)
		t2 = t
	return t2

imgPathList = [
	"/img/brake_adjusting_screw.jpeg",
	"/img/brake_band_assembly.jpg",
	"/img/brake_drum.jpg",
	"/img/brake_lining.jpeg",
	"/img/brake_pivot_pin.jpeg"
]

def do_get(self, rMap):
	global responseOk
	responseOk = False
	if self.path == "/":
		basic_headers(self)
		cookies = SimpleCookie(self.headers.get('Cookie'))
		balance = "0.00"
		for morsel in cookies.values():
			if morsel.key == "session":
				if morsel.value != "":
					theStr =  "Session: " + morsel.value + "<br>"
					self.wfile.write(theStr.encode())

					res = cur.execute("select * from user where session=?", (morsel.value,))
					row = res.fetchone()
					firstName = row[1]
					lastName = row[2]
					balance = row[6]
					
					theStr2 = "Full Name: " + "<span style='color:#add8e6;'>" \
								+ firstName + " " + lastName + "</span>" + "<br>"
					self.wfile.write(theStr2.encode())
		t = rMap[""]
		decimal = Decimal(balance).quantize(cents, ROUND_HALF_UP)
		d = {"balance": str(decimal)}
		t = installVals(t, d)
		self.wfile.write(t.encode())
	if self.path == "/grabOrder":
		basic_headers(self)
		cookies = SimpleCookie(self.headers.get('Cookie'))
		balance = "0.00"
		ordersLeftToday = 0
		for morsel in cookies.values():
			if morsel.key == "session":
				if morsel.value != "":

					res = cur.execute("select * from user where session=?", (morsel.value,))
					row = res.fetchone()
					balance = row[6]
					ordersLeftToday = row[7]
		t = rMap["grabOrder"]
		decimal = Decimal(balance).quantize(cents, ROUND_HALF_UP)
		d = {"balance": str(decimal),
			"ordersLeftToday": str(ordersLeftToday)
		}
		t = installVals(t, d)
		self.wfile.write(t.encode())
	if self.path == "/login":
		self.send_response(200)
		cookie = SimpleCookie()
		cookie["session"] = ""
		for morsel in cookie.values():
			self.send_header("Set-Cookie", morsel.OutputString())
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(rMap["login"].encode())
	if self.path == "/register":
		self.send_response(200)
		cookie = SimpleCookie()
		cookie["session"] = ""
		for morsel in cookie.values():
			self.send_header("Set-Cookie", morsel.OutputString())
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(rMap["register"].encode())
	if self.path == "/editName":
		t = rMap["editName"]
		basic_headers(self)
		cookies = SimpleCookie(self.headers.get('Cookie'))
		for morsel in cookies.values():
			if morsel.key == "session":
				if morsel.value != "":
					res = cur.execute("select * from user where session=?", (morsel.value,))
					row = res.fetchone()
					firstName = row[1]
					lastName = row[2]
		d = {"firstname": firstName,
			"lastname": lastName
		}
		t = installVals(t, d)
		self.wfile.write(t.encode())

	if self.path == "/testMoney":
		basic_headers(self)
		t = rMap["testMoney"]
		value1 = Decimal('0.59').quantize(cents, ROUND_HALF_UP)
		value2 = Decimal('0.54').quantize(cents, ROUND_HALF_UP)
		d = {"value1": "$" + str(value1),
			"value2": "$" + str(value2),
			"sum": "$" + str(value1 + value2)
		}
		t = installVals(t, d)
		self.wfile.write(t.encode())
	if self.path == "/addFriend":
		basic_headers(self)
		t = rMap["addFriend"]
		l = []
		cur.execute("select * from user")
		for row in cur:
			firstName = row[1]
			lastName = row[2]
			l+= [firstName + " " + lastName]
		t2 = installFor(t,l)
		self.wfile.write(t2.encode())
	for key in imgPathList:
		if self.path == key:
			url = key
			self.send_response(200)
			self.send_header('Content-type','image/jpeg')
			self.end_headers()
			global base_path
			print("path: ", base_path + url)
			f = open(base_path + url, "rb")
			self.wfile.write(f.read())
			f.close()
	for key in rMap:
		if key not in ["", "grabOrder", "login", "register", "editName", "testMoney", "addFriend"]:
			if self.path == "/" + key:
				basic_headers(self)
				self.wfile.write(rMap[key].encode())
	simpleJs(self, "/js/webSockets.js")
	simpleJs(self, "/js/three.js")
	simpleJs(self, "/js/glassCrusher.js")
	simpleCss(self, "/css/style.css")


###
# def do_get(self, theDict):
# 	global responseOk
# 	responseOk = False
# 	if self.path == "/":
# 		basic_headers(self)
# 		self.wfile.write(theDict["homeTotal"].encode())
# 	if self.path == "/page1":
# 		basic_headers(self)
# 		self.wfile.write(theDict["page1"].encode())
# 	if self.path == "/page2":
# 		basic_headers(self)
# 		self.wfile.write(theDict["page2"].encode())
# 	if self.path == "/login":
# 		basic_headers(self)
# 		self.wfile.write(theDict["login"].encode())
# 	simpleJs(self, "/js/webSockets.js")
###

def create_response(self, message):
	print("message: ", message)
	j = json.loads(message)
	print("j: ", j)
	resultJ = {}
	if (j["messageType"]=="basicMessage"):
		resultJ = {"messageType":"basicMessage", "data":"hello websocket"}
	if (j["messageType"]=="thePart"):
		session = j["session"][8:]
		print("session: ", session)
		res = cur.execute("select * from user where session=?", (session,))
		row = res.fetchone()
		print("row: ", row)
		user_id = row[0]
		partState = row[8]
		balance = Decimal(row[6]).quantize(cents, ROUND_HALF_UP)
		profit = (balance * Decimal("0.02")).quantize(cents, ROUND_HALF_UP)

		res = cur.execute("select * from parts where part_id=?", (partState,))
		row = res.fetchone()
		name = row[1]
		img_path = row[2]
		price = row[3]
		# store in db
		sql = ''' UPDATE user
                    SET activeTradeProfit = ?
                        WHERE user_id = ?'''
		res = cur.execute(sql, (str(profit), user_id))
		conn.commit()
		resultJ = {"messageType":"thePart", "data":{"name":name, "img_path":img_path, "price":price, "profit":str(profit)}}
	if (j["messageType"]=="trade"):
		session = j["session"][8:]
		res = cur.execute("select * from user where session=?", (session,))
		row = res.fetchone()
		print("row: ", row)
		user_id = row[0]
		balance = Decimal(row[6]).quantize(cents, ROUND_HALF_UP)
		ordersLeftToday = row[7]
		partState = row[8]
		profit = Decimal(row[9]).quantize(cents, ROUND_HALF_UP)
		sql = ''' UPDATE user
                    SET activeTradeProfit = ?,
						balance = ?,
						ordersLeftToday = ?,
						partState = ?
                        WHERE user_id = ?'''
		newBalance = str(balance + profit)
		res = cur.execute(sql, ("0.00", newBalance, ordersLeftToday-1, partState+1, user_id))
		conn.commit()
		resultJ = {"messageType":"trade", "balance": newBalance, "ordersLeftToday":ordersLeftToday-1}
	return json.dumps(resultJ)

port = 8007