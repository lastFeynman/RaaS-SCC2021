import os

if __name__ == "__main__":
    lst = os.listdir(os.getcwd())  # 获取当前目录下所有的文件名
    for c in lst:
        if os.path.isfile(c) and c.endswith('.py') and c.find("batch_exec") == -1:  # 判断文件名是以.py结尾的，并且去掉run.py文件
            print(c)  # 查看文件
            os.system("start cmd /c python " + c)
            # os.system('python {}'.format(c))  # 相当于在终端执行文件  python main.py