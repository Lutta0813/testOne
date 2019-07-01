# 1. 最多輸入三次密碼
# 2. 錯誤的話，就印出“密碼輸入錯誤，還有_次機會“
# 3. 正確的話，就印出“登入成功”
# 4. 不能使用while True

password = 'a123456'
checkPasswordTimes = 3

while checkPasswordTimes > 0:
	pwd = input('請輸入密碼： ')
	if pwd == password:
		print('登入成功！')
		break
	else:
		checkPasswordTimes = checkPasswordTimes - 1
		print('密碼輸入錯誤，還有', checkPasswordTimes, '次機會')
		if checkPasswordTimes == 0:
			print('密碼輸入錯誤達三次，帳號已鎖定')