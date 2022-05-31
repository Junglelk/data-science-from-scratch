# 读写文件

# r 以只读方式打开文件
file_for_read = open('reading_file.txt', 'r')
# w 以写方式打开文件
file_for_write = open('writing_file.txt', 'w')
# a 以追加方式打开文件
file_for_append = open('appending_file.txt', 'a')
file_for_append.write('\nThis is a new line')

file_for_write.close()
file_for_append.close()

# 在 with 语句中使用文件,文件将自动关闭，感觉很像java的 try-with-resources
# with语句的格式大致为:
# with open(filename, mode) as f:
#     data = function_that_gets_data_from_file(f)
# process_data(data)
# 到process语句时，文件已经关闭，不需要再次关闭或者试图使用它
