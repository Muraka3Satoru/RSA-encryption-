# RSA-encryption-
pythonでRSA暗号を実装しました

注意：windowsでは暗号化できません。
　　：ubuntu-18.04.4ではできるので是非そちらでお楽しみください

使い方

手順1
>python make_key.py gen.txt
で公開鍵と秘密鍵を生成

手順2
>python change_sec.py gen.txt
で公開鍵の入力を求められるので
------------------------------------------
例)
公開鍵(3,899329)
公開鍵を入力してください:3 899329
------------------------------------------
のように入力する

手順3
>python change_gen.py ./text/sec.txt
で暗号化されてる文が読めるようになる
 
