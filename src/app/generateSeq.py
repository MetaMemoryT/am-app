import random
def run():
    sessionKey = ""
    for i in range(0,5):
        x = random.randint(65,122)
        sessionKey += chr(x)
    print(sessionKey)
#print(ord('a'))
#print(ord('z'))
#print(ord('A'))
#print(ord('Z'))