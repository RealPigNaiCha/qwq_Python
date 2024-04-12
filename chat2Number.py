def number_to_chinese(number):
    chinese_nums = {
        0: '零', 1: '一', 2: '二', 3: '三', 4: '四',
        5: '五', 6: '六', 7: '七', 8: '八', 9: '九'
    }
    if number == 0:
        return chinese_nums[0]
    result = ''
    while number > 0:
        result = chinese_nums[number % 10] + result
        number //= 10
    return result

# 用户输入部分
user_input = int(input("请输入一个正整数："))
if user_input <= 0:
    print("输入错误，请输入一个正整数。")
else:
    # 将数字转换为中文字符表示
    chinese_result = number_to_chinese(user_input)
    print(f"{user_input} 的中文字符表示是：{chinese_result}")