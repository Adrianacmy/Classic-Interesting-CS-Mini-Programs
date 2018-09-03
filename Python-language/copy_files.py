'''
copy all files from one foler to another
not working well??
創建文件夾
獲取文件夾名稱
拷貝內容

'''

import os

from multiprocessing import Pool, Manager


def copy_files(file_name, old_foler_name, new_foler_name, queue):
    fr = open(old_foler_name+'/'+file_name, 'r')
    print('.....................', fr)
    fw = open(new_foler_name+'/'+name, 'w')
    content = fr.read()
    fr.write(content)

    fr.close()
    fw.close()

    queue.put(file_name)


def main():
    old_foler_name = input('enter the foler to copy: ')
    new_foler_name = old_foler_name + 'copy'

    os.mkdir(new_foler_name)

    # get all file name in olde foler
    file_names = os.listdir(old_foler_name)
    pool = Pool(2)
    queue = Manager().Queue()

    for name in file_names:
        pool.apply_async(copy_files, args=(
            name, old_foler_name, new_foler_name, queue))

    num = 0
    while num < len(file_names):
        queue.get()
        num += 1
        rate = num/len(file_names)
        print(rate*100, 'is done', end='')
        # print('{:.2f}% is done'.format(rate*100), end='')

    print('\ncopy is done')

    # pool.close()
    # pool.join()


if __name__ == '__main__':
    main()
