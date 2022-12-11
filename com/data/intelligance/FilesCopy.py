i=1
while i<=3:
    try:
        print("-"*50)
        import time
        start = time.process_time()
        import os
        import shutil
        os.getcwd()
        os.chdir(r'C:\Users\bhanu\Desktop\output')
        for v in os.listdir():
            print(v)
        e=input("enter the folder u wanted to filter:")
        if e=="csv":
            os.chdir(r"C:\Users\bhanu\Desktop\output\csvfile")
            shutil.copytree(r"C:\Users\bhanu\Desktop\output\csvfile",r"C:\Users\bhanu\Desktop\csvfile")
        elif e=="json" :
            os.chdir(r"C:\Users\bhanu\Desktop\output\jsonfile")
            shutil.copytree(r"C:\Users\bhanu\Desktop\output\jsonfile",r"C:\Users\bhanu\Desktop\jsonfile")
        else:
            print("file not found!")
        print(time.process_time() - start)
    except FileExistsError:
        print("please try again the folder already exsists!")
        i=i+1
print("please come again tommorow")