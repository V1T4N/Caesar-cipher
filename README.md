# Simple substitution cipher

単一換字式暗号を使って文字列を暗号化．復元する

## Description
encrypt.pyを実行し，任意の文字列を入力されるとランダムに暗号化し，復元するためのCSVファイル(key.csv)を吐き出します．
decrypt.pyを実行し，暗号化された文字列を入力するとkey.csvを読み取り復元します．



encrypt_ReadFromText.py および analyze.py　は鍵なしで暗号化された文を復号するためのコードです．

encrypt_ReadFromText.pyを実行すると，ディレクトリ内のtext.txtを読み取って暗号化し，encryptedText.txtに吐き出します．

analyze.pyを実行すると，encryptedText.txtに記された暗号文を英文中のアルファベット出現頻度(http://www7.plala.or.jp/dvorakjp/hinshutu.html)に基づいて鍵なしで解析し復元します．
この結果はdecryptedText.txtに吐き出されます．

## Requirement
python2.7

## Author
Yuzuki Mimura
