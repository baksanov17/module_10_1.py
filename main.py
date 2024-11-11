import time
from threading import Thread


def write_words(word_count, file_name):
    count = 0
    file = open(file_name, 'w')
    for word in range(word_count):
        count += 1
        time.sleep(0.1)
        file.write(f'Денис №{count}\n')
    file.close()
    print(f'Завершилась запись в файл {file_name}')


start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish = time.time()
print(f'Работа потоков: {finish - start}')


start1 = time.time()
thread1 = Thread(target=write_words, args=(10, "example5.txt"))
thread2 = Thread(target=write_words, args=(30, "example6.txt"))
thread3 = Thread(target=write_words, args=(200, "example7.txt"))
thread4 = Thread(target=write_words, args=(100, "example8.txt"))
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
finish1 = time.time()
print(f'Работа потоков: {finish1 - start1}')
