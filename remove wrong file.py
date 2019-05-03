import os
# ver 10
x = 23042
while x < 24000:
	x += 1
	str1 = str(x)
	path = "/content/gdrive/My Drive/" + "000" + str1 + ".jpg"
	print(path)
	os.remove(path)