with open("../myfile.txt", "w") as f:
    f.write("Hello file world!\n")
f.close()


# file_name=r'C:/Users/olgac/PycharmProjects/PythonProject/myfile.txt'
with open("../myfile.txt", encoding="utf-8") as f:
    read_data=f.read()
    print(read_data)


with open("../my_dir/myfile.txt", "w") as f:
    f.write("Hello file world!\n")

