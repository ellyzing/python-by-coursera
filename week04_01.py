import os.path
import tempfile
import random
import string

class File:
    def __init__(self, path_to_file):
        self.path = os.path.join(tempfile.gettempdir(), path_to_file)
        self.name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        if not os.path.isfile(self.path):
            try:
                os.mkdir(self.path)
            except:
                pass
            open(self.path+"\\" + self.name + ".txt", 'tw', encoding='utf-8')
            self.text=""
        else:
            with open(self.path+"\\" + self.name + ".txt", 'tw', encoding='utf-8') as f:
                self.text=f.read()
                self.count = self.text.split("\n")

                self.end = len(count)
        self.current = 0

    def read(self):
        with open(self.path+"\\" + self.name + ".txt", 'r') as f:
            self.text=f.read()
            self.count = self.text.split("\n")
            self.end = len(self.count)
            return self.text
    def write(self, text):
        with open(self.path+"\\" + self.name + ".txt", 'w') as f:
            self.text=text
            f.write(text)
            self.count = self.text.split("\n")
            self.end = len(self.count)

    def __add__(self, file1):
        if isinstance(file1, File):
            new_text = self.text + file1.text
        else:
            new_text=""
        new_file = File(path_to_file)
        new_file.text=new_text
        new_file.write(new_text)
        self.count = new_file.text.split("\n")
        new_file.end = len(self.count)
        return(new_file)

    def __str__(self):
        return self.path

    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.count[self.current]
        self.current+=1
        return result

#Отладка
# path_to_file = 'some_filename'
# print(os.path.exists(path_to_file))
# file_obj = File(path_to_file)
# print(os.path.exists(path_to_file))
# print(file_obj.read())
# file_obj.write('some text')
# print(file_obj.read())
# file_obj.write('other text')
# print(file_obj.read())
# file_obj_1 = File(path_to_file + '_1')
# file_obj_2 = File(path_to_file + '_2')
# file_obj_1.write('line 1\n')
# file_obj_2.write('line 2\n')
# new_file_obj = file_obj_1 + file_obj_2
# print(isinstance(new_file_obj, File))
# print(new_file_obj)
# for line in new_file_obj:
#      print(ascii(line))
