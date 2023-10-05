### 
### コマンドラインに形態素解析[語, 品詞, ...]
### 同じディレクトリにout_janome.txtを生成し、単語とその出現数を記録
###

# 以下janomeを利用
# !pip install janome

from janome.tokenizer import Tokenizer
import zipfile
import os.path, urllib.request as req

# ------------Change Here--------------
txt = "日本語の形態素解析は難しいものとされている。"

# 形態素解析オブジェクト
t = Tokenizer()

# テキストを一行ずつ処理
# txtに改行があるなら、複数行にも対応する
word_dic = {}
lines = txt.split("\r\n")
for line in lines:
    malist = t.tokenize(line)
    for w in malist:
        word = w.surface
        ps = w.part_of_speech
        print(word, ps)

        if not word in word_dic:
            word_dic[word] = 0
        word_dic[word] += 1

# 頻出単語を表示(keys[:50]が表示上限数)
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, cnt in keys[:50]:
    print("{0}({1}) ".format(word, cnt), end="")

#単語と出現数を見やすく改行してリストにする
word_list = [x[0] + "," for x in keys]
count_list = [str(x[1]) + "\n" for x in keys]
combined = [word_list[i] + count_list[i] for i in range(min(50, len(word_list)))]

#ファイル出力
with open("out_janome.txt", "w", encoding="utf-8") as f:
    f.writelines(combined)
