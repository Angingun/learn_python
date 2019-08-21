# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

import random


def generate_code(code_len=4):
    all_chars = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    # all_chars = str([0: range(9)]) + ord(int([64:90] + [97:122])) 
    last_pos = len(all_chars)
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


if __name__ == "__main__":
    print(generate_code())
