import re
import sys

# stdin 和 stdout 以管道的方式来传递数据
# sys.argv是命令行的参数列表
# sys.argv[0]是程序本身的名字
# sys.argv[1]是第一个参数
# 第一个参数指定一个正则表达式
regx = sys.argv[1]

for line in sys.stdin:
    # 匹配每一行，如果匹配成功，则输出结果
    if re.match(regx, line):
        sys.stdout.write(line)
