import math


n = 2   #入力させる数値の数
input_number = []  #入力した数値を格納する配列

for i in range(n):
    input_number += [int(input(str(i+1) + "番目の数値入力 "))] #入力した数値をxに格納


#四則演算
#和
print('足し算の計算結果:{}'.format(input_number[0] + input_number[1]))

#差
print('引き算の計算結果:{}'.format(input_number[0] - input_number[1]))

#積
print('掛け算の計算結果:{}'.format(input_number[0] * input_number[1]))

#商
print('割り算の計算結果:{}'.format(input_number[0] / input_number[1]))


#追加機能
#最小公倍数
print('最小公倍数:{}'.format(math.lcm(input_number[0],input_number[1])))

#最大公約数
print('最大公約数:{}'.format(math.gcd(input_number[0],input_number[1])))