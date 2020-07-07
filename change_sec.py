from math import gcd
import random
import time
import sys

#公開鍵を使って平文を暗号化
def change_secVer(text,pubkey):
	sec_list = []
	#文字列ユニコードに変換し、それを暗号化した
	for i in text:
		sec_list.append(pow(ord(i),pubkey[0],pubkey[1]))
	#暗号化した数字列を文字列に変換し、連結したテキストを返す
	sec_text = ''.join(chr(i) for i in sec_list)

	return sec_text

#ユニコードエラーを解消する
def sanitize(encrypted_text):

  return encrypted_text.encode('utf-8', 'replace').decode('utf-8')


if __name__ == '__main__':
	with open(sys.argv[1],'r') as f:
		text = f.read()
		pubkey = tuple(map(int,input('公開鍵を入力してください：').split()))
		#平文から公開鍵を使って暗号
		sec_text = change_secVer(text,pubkey)
		save_text = './text/sec.txt'
		with open(save_text,mode='w') as f:
			f.write(sanitize(sec_text))
			print("暗号化が成功しました")
			print(save_text + "に暗号化した文が入っています")
