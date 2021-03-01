# __author__: "yudongyue"
# date: 2021/3/1
# with open('all.csv') as f:
# print(f.read(5))  # 读取5个字符，如果未给定或为负则读取所有
# print(f.readline(7))  # 读取7个字符
# print(f.read())  # 读取整个文件
# for i in f.readlines():  # 将文件读入一个数组然后按行输出
#     print(i)
# print(f.name)
write_in = ['1', '2', '3', 'h']
with open(file='all.csv', mode='r+', newline='\n', encoding='UTF-8') as f:
    # f.seek(1)  # 移动文件读取指针到指定位置
    # print(f.tell())  # 返回文件当前位置
    # print(f.read())
    # print(f.tell())
    # print(f.truncate(15))  # 从首字符开始截断15个字符剩下字符全部删除
    # print(f.read())
    # print(f.write('xxx========'))
    # print(f.read())
    f.writelines(write_in)
    print(f.writable())
