rot13 = {}
for i in range(ord("A"),ord("M")+1):
	rot13[i] = i+13
for i in range(ord("N"),ord("Z")+1):
	rot13[i] = 13-(26-i)
for i in range(ord("a"),ord("m")+1):
	rot13[i] = i+13
for i in range(ord("n"),ord("z")+1):
	rot13[i] = 13-(26-i)
inp = raw_input("Give string for translation :\n")
s = list(inp)
for i in range(len(inp)):
	try:
		s[i] = chr(rot13[ord(s[i])])
	except:
		continue
s = "".join(s)
print s