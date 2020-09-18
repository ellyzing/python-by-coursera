import os.path
import tempfile
import random
import string

class File:
    def __init__(self, path_to_file):
        self.path = path_to_file
        if not os.path.isfile(self.path):
            open(self.path, 'tw', encoding='utf-8')
            self.text=""
        else:
            with open(self.path, 'r', encoding='utf-8') as f:
                self.count=f.readlines()
                self.text=""
                for line in self.count:
                    self.text+=line
                self.end = len(self.count)
            f.closed
        self.current = 0

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.count=f.readlines()

            self.text=""
            for line in self.count:
                self.text+=line
            self.end = len(self.count)
            return(self.text)
        f.closed
    def write(self, text):
        with open(self.path, 'w') as f:
            self.text=text
            f.write(self.text)
            self.count = self.text.split("\n")
            self.end = len(self.count)
        f.closed

    def __add__(self, file1):
        if isinstance(file1, File):
            new_text = self.text + file1.text
        else:
            new_text=""
        name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))+".txt"
        new_path = os.path.join(tempfile.gettempdir(), name)
        new_file = File(new_path)
        new_file.text=new_text
        new_file.write(new_text)
        return(new_file)

    def __str__(self):
        return self.path

    def __iter__(self):
        self.temp=self.current
        return self
    def __next__(self):
        if self.temp >= self.end:
            raise StopIteration
        result = self.count[self.temp]
        self.temp+=1
        if result != "":
            return result
        else:
            raise StopIteration


# #Отладка
path_to_file = 'some_filename.txt'
path_to_file1 = 'some_filename1.txt'
# # # print(os.path.exists(path_to_file))
# # # file_obj = File("multiline1.txt")
# # # print(os.path.exists(path_to_file))
# # # print(file_obj.read())
# # # file_obj.write('71c82033d6464c7cab03aa48528e8b8f \n 74e9683e5aae4e8bb2278b25a13d745c \n b79c2a10f2394ac4a51d21f6a65e6809')
# # # print(file_obj.read())
file_obj_1 = File(path_to_file1)
file_obj_2 = File(path_to_file)
file_obj_1.write('line 1\nline 2\nline 3\n')
file_obj_2.write('line 2\n')
new_file_obj = file_obj_1 + file_obj_2
# print(file_obj_1.read())
for line in file_obj_1:
    print(ascii(line))

for line in file_obj_1:
    print(ascii(line))
