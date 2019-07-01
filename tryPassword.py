password = 'a123456'
checkPasswordTimes = 3

while True:
	enterPassword = input('請輸入密碼： ')
	if enterPassword == password:
		print('登入成功')
		break
	else:
		if checkPasswordTimes > 1:
			checkPasswordTimes = checkPasswordTimes - 1
			print('密碼輸入錯誤，還有', checkPasswordTimes, '次機會')
		else:
			print('密碼輸入錯誤達三次，帳號已鎖定。')
			break
