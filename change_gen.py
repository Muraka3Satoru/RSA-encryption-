from math import gcd
import random
import time
import sys

#秘密鍵をつかって暗号文から平文に変換
def change_canRead(text, sec):
	reg_list = []
	li = [ord(i) for i in text]

	#暗号文から平文のユニコードを生成
	for i in text:
		reg_list.append(pow(ord(i),sec[0],sec[1]))
	#平文のユニコードから文字列を復元
	reg_text = ''.join(chr(i) for i in reg_list)

	return reg_text

#ユニコードエラーを解消する
def sanitize(encrypted_text):

  return encrypted_text.encode('utf-8', 'replace').decode('utf-8')

if __name__ == '__main__':
	with open(sys.argv[1],'r') as f:
		text = f.read()
		seckey = tuple(map(int,input('秘密鍵を入力してください：').split()))
		#暗号文から平分のテキストに変換している
		gen_text = change_canRead(text,seckey)

		print(sanitize(gen_text))
