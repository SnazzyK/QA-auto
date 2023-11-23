# var = input("Напиши текст ")
#
#
#
# fw = open('doc/file.txt', 'a')
#
# fw.write(var)
# fw.close()

#-----------------------------------------------------------------------------------------


# var = input("Напиши текст ")
# fw = open('doc/file2.txt', 'w+')
#
# fw.write(var)
# fw.close()

#-----------------------------------------------------------------------------------------
# var = input("Напиши текст ")
# fr = open('doc/file.txt', 'r+')
# text = fr.read()
# fr.close()
# print(text)

# a - запись новых данных , в файл , и помещение новых данных в конец файла
# w - запись новых данных ,но с удалением старых данных
# r - чтение ранее записанных данных .



rec = input("Введите имя ")
fl = open('doc/file_name.txt', 'w')
text = fl.write(rec)
fl.close()
#-----------------------------------------------------
rec = input("Введите имя")
fl = open('doc/file_name.txt', 'a')
text = fl.write(rec + '\n')
fl.close()
#-----------------------------------------------------
fl = open('doc/file_name.txt', 'r')
text = fl.read()
fl.close()
print(text)
#-----------------------------------------------------
rec = input("Введите имя ")
fl = open('doc/file_name.txt', 'r+')
text = fl.write(rec)
text = fl.read()
fl.close()
print(text)














