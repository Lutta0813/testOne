password = 'a123456'
checkPassword = 3

while True:
	enterPassword = input('請輸入密碼： ')
	if enterPassword == password:
		print('登入成功')
		break
	else:
		if checkPassword > 1:
			checkPassword = checkPassword - 1
			print('密碼輸入錯誤，還有', checkPassword, '次機會')
		else:
			print('密碼輸入錯誤達三次，帳號已鎖定。')
			break
