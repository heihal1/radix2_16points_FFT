import math
import numpy as np

def fft_NoFunctionCalling(input_real, input_imag):
    N = int(16)  # 16点fft
    stages = int(4)# N = 2 ** stages

    # 输入重排
    bit_reverse_table = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    data_real = [input_real[i] for i in bit_reverse_table]
    data_imag = [input_imag[i] for i in bit_reverse_table]

    # 旋转因子 tf(twiddle_factor)
    tf_real = []
    tf_imag = []
    # 旋转因子通过欧拉公式分解为cos(x) + jsin(x)
    for k in range(8):
        tf_real.append(int(round(math.cos(-2 * math.pi * k / N) * 128))) #8位整数定点化
        tf_imag.append(int(round(math.sin(-2 * math.pi * k / N) * 128)))

    for s in range(stages): # N = 16，总共分为四级计算
        butterfly_calculation_span = 2 ** s #蝶形运算跨度(相隔多远的两个数据做蝶形运算)，第0级为1，第1级为2，第2级为4，第3级为8
        step = 2 * butterfly_calculation_span #步长，控制每个stage中，共有多少次蝶形运算
        for i in range(0, N, step):
            for j in range(butterfly_calculation_span):
                #旋转因子索引
                tf_idx = j * (2 ** (3 - s))

                #得到旋转因子的实部和虚部
                W_real = tf_real[tf_idx]
                W_imag = tf_imag[tf_idx]

                #输入数据索引
                data_idx_1 = i + j
                data_idx_2 = data_idx_1 + butterfly_calculation_span

                a_real, a_imag = data_real[data_idx_1], data_imag[data_idx_1]
                b_real, b_imag = data_real[data_idx_2], data_imag[data_idx_2]

                #蝶形运算data = a + W * b，data' = a - W * b，令其中c = W * b
                c_real = (b_real * W_real - b_imag * W_imag) // 128 #Descaling 反缩放
                c_imag = (b_real * W_imag + b_imag * W_real) // 128 #Descaling 反缩放

                data_real[data_idx_1] = a_real + c_real
                data_imag[data_idx_1] = a_imag + c_imag
                data_real[data_idx_2] = a_real - c_real
                data_imag[data_idx_2] = a_imag - c_imag

    return data_real, data_imag
# 共四级，每级8次蝶形运算，每次蝶形运算需要4个乘法器、6个加法器，共需要128个实数加法器，192个实数乘法器

if __name__ == "__main__":
    # 生成16点输入（实部为1-16，虚部为0）
    input_real = [i & 0xFF for i in range(0, 16)]  # 8位有符号整数
    input_imag = [0] * 16  # 虚部全零

    data_real, data_imag = fft_NoFunctionCalling(input_real, input_imag)

    complex_input = np.array(input_real) + 1j * np.array(input_imag)

    fft_result = np.fft.fft(complex_input)

    # 输入数据
    print("fft input: ")
    for i in range(16):
        print(f"x[{i}] = {input_real[i]} + j{input_imag[i]}")

    # 不调用函数结果
    print("fft_NoFunctionCalling output= ")
    for i in range(16):
        print(f"X[{i}] = {data_real[i]} + j{data_imag[i]}")

    # 调用函数结果
    print("fft_FunctionCalling output= ")
    for i in range(16):
        print(f"X[{i}] = {fft_result[i]}")

