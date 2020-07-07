from math import gcd
import random
import time
import sys

#公開鍵と秘密鍵の生成し、暗号文を作成する

#最小公倍数を求める
def lmc(num1,num2):
	i=1
	j=1
	while(1):
		if(num1*i < num2*j):
			i += 1
		elif(num1*i > num2*j):
			j += 1
		elif(num1*i == num2*j):
			break
	return num1*i

#互いに素である数を求める
def eachOther_only(num1):
	for i in range(2, num1):
		if(gcd(i,num1) == 1):
			return i

#余りが1になるようなdを求める
def mod_math(e,f):
	d = 1
	while(1):
		if(d*e % f == 1):
			return d
		d += 1

#公開鍵と秘密鍵の生成
def prime_pair(p ,q):
	#公開鍵の生成
	N = p*q
	F = lmc(p-1,q-1)
	E = eachOther_only(F)
	pubkey = (E,N)

	#秘密鍵の生成
	D = mod_math(E,F)
	seckey = (D,N)

	return pubkey, seckey

#ユニコードエラーを解消する
def sanitize(encrypted_text):

  return encrypted_text.encode('utf-8', 'replace').decode('utf-8')


if __name__ == '__main__':
	with open(sys.argv[1],'r') as f:
		text = f.read()
		#両方とも値が小さすぎると"！"とかで'狸'とかの文字化け起こすよ
		pubkey, seckey = prime_pair(317, 2837)
		print("公開鍵 ：",pubkey)
		print("秘密鍵 ：",seckey)
