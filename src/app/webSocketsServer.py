#main program and imports for standalone purpose       
import sys
import threading
from socketserver import ThreadingMixIn
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
import http.cookies
from http.cookies import SimpleCookie
# import ssl
from io import BytesIO
from base64 import b64encode
from HTTPWebSocketsHandler import HTTPWebSocketsHandler
from importlib import reload
import reloadableWebSocketServer
import sqlite3
import random
from email.parser import BytesParser

if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = 8007
if len(sys.argv) > 2:
    secure = str(sys.argv[2]).lower()=="secure"
else:
    secure = False
if len(sys.argv) > 3:
    credentials = str(sys.argv[3])
else:
    credentials = ""
secure = False
global theDict
theDict = None
global theSession
theSession = {}

class WSResponse(HTTPWebSocketsHandler):

    def on_ws_message(self, message):
        if message is None:
            message = ''
        # echo message back to client
        print("reloading reloadableWebSocketServer...")
        reload(reloadableWebSocketServer)
        message2 = reloadableWebSocketServer.create_response(self, message)

        self.send_message(str(message2))
        self.log_message('websocket received "%s"',str(message2))

    def on_ws_connected(self):
        self.log_message('%s','websocket connected')

    def on_ws_closed(self):
        self.log_message('%s','websocket closed')
    
    def do_GET(self):
        global theDict
        if self.server.auth and not self.checkAuthentication():
            return
        if self.headers.get("Upgrade", None) == "websocket":
            self._handshake()
            #This handler is in websocket mode now.
            #do_GET only returns after client close or socket error.
            self._read_messages()
        else:
            print("reloading reloadableWebSocketServer...")
            reload(reloadableWebSocketServer)
            reloadableWebSocketServer.do_get(self, theDict)
    
    def do_POST(self):
        conn= sqlite3.connect('data.db')
 
        # cursor object
        cur = conn.cursor()

        print(self.path)
        if self.path == "/registerPost":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode("utf-8") 
            # print(body)
            l = body.split("&")
            print(l)
            username = l[0][9:]
            password = l[1][9:]
            password2 = l[2][9:]
            if password == password2:
                print("passwords match")
                sql = '''INSERT INTO user(first_name,last_name,username,password,session,balance,ordersLeftToday,partState,activeTradeProfit)
                            VALUES(?,?,?,?,?,?,?,?,?) '''
                sessionKey = ""
                for i in range(0,5):
                    x = random.randint(65,122)
                    # print("x: ", x)
                    sessionKey += chr(x)
                cur.execute(sql, ("Empty", "Name", username, password, sessionKey, "49.00", 20, 1, "0.00"))
                conn.commit()

                self.send_response(301)
                self.send_header('Location', '/')
                self.end_headers()
            else:
                print("passwords do not match")                 
        if self.path == "/loginPost":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode("utf-8") 
            # print(body)
            l = body.split("&")
            print(l)
            username = l[0][9:]
            password = l[1][9:]
            print("username:", username)
            print("password:", password)
            res = cur.execute("select * from user where username=? and password =?", (username, password))
            sessionID = res.fetchone()[5]
            print(sessionID)

            self.send_response(301)
            cookie = http.cookies.SimpleCookie()
            cookie["session"] = sessionID
            for morsel in cookie.values():
                self.send_header("Set-Cookie", morsel.OutputString())
            self.send_header('Location', '/')
            self.end_headers()
        if self.path == "/uploadLicensePost":
            content_length = int(self.headers['Content-Length'])
            print("test1")
            # note: cannot cgi.parse_multipart and read content
            # body = self.rfile.read(content_length)
            print("test1")
            # print(body)
            ctype = self.headers.get_content_type()
            pdict = {"boundary": self.headers.get_param("boundary")}
            print(pdict)
            if ctype == 'multipart/form-data':
                # the cgi module was removed in python 3.13, parse the form with email instead
                body = self.rfile.read(content_length)
                header = b"Content-Type: " + self.headers['content-type'].encode() + b"\r\n\r\n"
                postvars = {}
                for part in BytesParser().parsebytes(header + body).get_payload():
                    name = part.get_param("name", header="content-disposition")
                    postvars.setdefault(name, []).append(part.get_payload(decode=True))
                print(postvars)
            print("test2")
            print(self.headers)
            print("boundary: ", pdict["boundary"])
           

        if self.path == "/editNamePost":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode("utf-8") 
            # print(body)
            l = body.split("&")
            print(l)
            firstName = l[0][10:]
            lastName = l[1][9:]
            print("firstName:", firstName)
            print("lastName:", lastName)

            # todo get original session
            cookies = SimpleCookie(self.headers.get('Cookie'))
            for morsel in cookies.values():
                if morsel.key == "session":
                    if morsel.value != "":
                        res = cur.execute("select * from user where session=?", (morsel.value,))
                        row = res.fetchone()
                        user_id = row[0]
                        sql = ''' UPDATE user
                                    SET first_name = ? ,
                                        last_name = ?
                                    WHERE user_id = ?'''
                        res = cur.execute(sql, (firstName, lastName, user_id))
                        conn.commit()
                        
            self.send_response(301)
            self.send_header('Location', '/')
            self.end_headers()           
        # self.send_response(200)
        # response = BytesIO()
        # response.write(b'This is POST request. ')
        # response.write(b'Received: ')
        # response.write(body)
        # self.wfile.write(response.getvalue())

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

def run(theDict2):
    global theDict
    try:
        theDict = theDict2
        theDict["page1"]
        #Replace WSSimpleEcho with your own subclass of HTTPWebSocketHandler
        server = ThreadedHTTPServer(('', port), WSResponse)
        server.daemon_threads = True
        server.auth = b64encode(credentials.encode())
        if secure:
            server.auth = b64encode(credentials.encode())
            server.socket = ssl.wrap_socket (server.socket, certfile='./server.pem', server_side=True)
            print('started secure https server at port %d' % (port,))
        else: 
            print('started http server at port %d' % (port,))
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()

if __name__ == '__main__':
    run()