import cmath

#输入数据重新排列
def bit_reverse(data_in):
    bit_reverse_table = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    data_bit_reverse = [data_in[i] for i in bit_reverse_table]
    return data_bit_reverse

#第0级蝶形运算(s0)，蝶形跨度为1
def butterfly_0(X_0,X_1):
    Y_0 = X_0 + X_1
    Y_1 = X_0 - X_1
    return Y_0,Y_1

#第1级蝶形运算(s1)，蝶形跨度为2
def butterfly_1(X_0,X_1,X_2,X_3):
    Y_0 = X_0 + X_2
    Y_1 = X_1 + (cmath.exp(-1j * cmath.pi / 2)) * X_3
    Y_2 = X_0 - X_2
    Y_3 = X_1 - (cmath.exp(-1j * cmath.pi / 2)) * X_3
    return Y_0,Y_1,Y_2,Y_3

#第2级蝶形运算(s2)，蝶形跨度为4
def butterfly_2(X_0,X_1,X_2,X_3,X_4,X_5,X_6,X_7):
    Y_0 = X_0 + X_4
    Y_1 = X_1 + (cmath.exp(-1j * cmath.pi / 4)) * X_5
    Y_2 = X_2 + (cmath.exp(-1j * cmath.pi / 2)) * X_6
    Y_3 = X_3 + (cmath.exp(-1j * (3 * cmath.pi) / 4)) * X_7
    Y_4 = X_0 - X_4
    Y_5 = X_1 - (cmath.exp(-1j * cmath.pi / 4)) * X_5
    Y_6 = X_2 - (cmath.exp(-1j * cmath.pi / 2)) * X_6
    Y_7 = X_3 - (cmath.exp(-1j * (3 * cmath.pi) / 4)) * X_7
    return Y_0, Y_1, Y_2, Y_3,Y_4,Y_5,Y_6,Y_7

#第3级蝶形运算(s3)，蝶形跨度为8
def butterfly_3(X_0,X_1,X_2,X_3,X_4,X_5,X_6,X_7,X_8,X_9,X_10,X_11,X_12,X_13,X_14,X_15):
    Y_0 = X_0 + X_8
    Y_1 = X_1 + (cmath.exp(-1j * cmath.pi / 8)) * X_9
    Y_2 = X_2 + (cmath.exp(-1j * cmath.pi / 4)) * X_10
    Y_3 = X_3 + (cmath.exp(-1j * (3 * cmath.pi) / 8)) * X_11
    Y_4 = X_4 + (cmath.exp(-1j *  cmath.pi / 2)) * X_12
    Y_5 = X_5 + (cmath.exp(-1j * (5 * cmath.pi) / 8)) * X_13
    Y_6 = X_6 + (cmath.exp(-1j * (3 * cmath.pi) / 4)) * X_14
    Y_7 = X_7 + (cmath.exp(-1j * (7 * cmath.pi) / 8)) * X_15
    Y_8 = X_0 - X_8
    Y_9 = X_1 - (cmath.exp(-1j * cmath.pi / 8)) * X_9
    Y_10 = X_2 - (cmath.exp(-1j * cmath.pi / 4)) * X_10
    Y_11 = X_3 - (cmath.exp(-1j * (3 * cmath.pi) / 8)) * X_11
    Y_12 = X_4 - (cmath.exp(-1j *  cmath.pi / 2)) * X_12
    Y_13 = X_5 - (cmath.exp(-1j * (5 * cmath.pi) / 8)) * X_13
    Y_14 = X_6 - (cmath.exp(-1j * (3 * cmath.pi) / 4)) * X_14
    Y_15 = X_7 - (cmath.exp(-1j * (7 * cmath.pi) / 8)) * X_15
    return Y_0,Y_1,Y_2,Y_3,Y_4,Y_5,Y_6,Y_7,Y_8,Y_9,Y_10,Y_11,Y_12,Y_13,Y_14,Y_15

#输入数据
data_in = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#重排后输入数据
output = bit_reverse(data_in)

#第0级蝶形运算
z0_s0,z1_s0 = butterfly_0(output[0] , output[1])
z2_s0,z3_s0 = butterfly_0(output[2] , output[3])
z4_s0,z5_s0 = butterfly_0(output[4] , output[5])
z6_s0,z7_s0 = butterfly_0(output[6] , output[7])
z8_s0,z9_s0 = butterfly_0(output[8] , output[9])
z10_s0,z11_s0 = butterfly_0(output[10] , output[11])
z12_s0,z13_s0 = butterfly_0(output[12] , output[13])
z14_s0,z15_s0 = butterfly_0(output[14] , output[15])

#第1级蝶形运算
z0_s1,z1_s1,z2_s1,z3_s1 = butterfly_1(z0_s0,z1_s0,z2_s0,z3_s0)
z4_s1,z5_s1,z6_s1,z7_s1 = butterfly_1(z4_s0,z5_s0,z6_s0,z7_s0)
z8_s1,z9_s1,z10_s1,z11_s1 = butterfly_1(z8_s0,z9_s0,z10_s0,z11_s0)
z12_s1,z13_s1,z14_s1,z15_s1 = butterfly_1(z12_s0,z13_s0,z14_s0,z15_s0)

#第2级蝶形运算
z0_s2,z1_s2,z2_s2,z3_s2,z4_s2,z5_s2,z6_s2,z7_s2 = butterfly_2(z0_s1,z1_s1,z2_s1,z3_s1,z4_s1,z5_s1,z6_s1,z7_s1)
z8_s2,z9_s2,z10_s2,z11_s2,z12_s2,z13_s2,z14_s2,z15_s2 = butterfly_2(z8_s1,z9_s1,z10_s1,z11_s1,z12_s1,z13_s1,z14_s1,z15_s1)

#第3级蝶形运算
z0_s3,z1_s3,z2_s3,z3_s3,z4_s3,z5_s3,z6_s3,z7_s3,z8_s3,z9_s3,z10_s3,z11_s3,z12_s3,z13_s3,z14_s3,z15_s3 = butterfly_3(z0_s2,z1_s2,z2_s2,z3_s2,z4_s2,z5_s2,z6_s2,z7_s2,
                                                                                                                    z8_s2,z9_s2,z10_s2,z11_s2,z12_s2,z13_s2,z14_s2,z15_s2)
print(z0_s3, z1_s3, z2_s3, z3_s3, z4_s3, z5_s3, z6_s3, z7_s3,
      z8_s3, z9_s3, z10_s3, z11_s3, z12_s3, z13_s3, z14_s3, z15_s3,
      sep='\n')




