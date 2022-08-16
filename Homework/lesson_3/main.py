# my_file = open("words.txt", 'w')
# my_file.write("Leon")
# my_file.close()

# my_file = open('words.txt', 'r')
# for i in my_file.readlines():
#     print(i)
# my_file.close()

my_file = open('words.txt', 'w+', encoding='utf-8')
my_file.write("לאון")
my_file.close()

my_file = open('words.txt', 'r')
for i in my_file.readlines():
    print(i)
my_file.close()