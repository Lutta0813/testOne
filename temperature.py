f = int
c = int

def changToFah(c):
	c = int(c)
	f = c*9/5+32
	print('攝氏溫度', c,'度','轉換成華氏溫度為：', f, '度')

def changeToCelsius(f):
	f = int(f)
	c = (f-32)*5/9
	print('華氏溫度', f, '度', '轉換成攝氏溫度為：', c, '度')


question = input('請問你想轉換成攝氏溫度還是華氏溫度？')


if question == '華氏':
	c = input('請輸入目前攝氏溫度： ')
	changToFah(c)
elif question == '攝氏':
	f = input('請輸入目前華氏溫度： ')
	changeToCelsius(f)


