try:
	with open("status.md" , "r") as f:
		text = f.readline()
		num = [int(x) for x in text.split() if x.isdigit()][0]
		num += 1
	
	if num<= 99999999999999999999999999999999:
		with open("status.md" , 'w') as f:
			if num in range(16):
				img = "![goal](PR.png)"
			elif num in range(128):
				img = "![goal](PR.png)"
			elif num in range(9999):
				img = "![goal](PR.png)"
			else:
				img = "![goal](PR.png)"
			
			f.write(f"{num} pull requests merged")
			f.write("<br>")
			f.write("Currently:")
			f.write("<br>")
			f.write(img)
except:
	with open("status.md" , "w") as f:
		f.write("1 pull request merged")
		f.write("<br>")
		f.write("Currently:")
		f.write("<br>")
		f.write("![goal](PR.png)")
