# - supergrepR2 V2
# - Written by: McB
# - Last modified: 04 Feb 2019
# - Designed to search multiple large text files using regex
# - Uses multiprocessing to search multiple files concurrently
# - To do's = add counters for total files, files remaining, number of matches
# - Add windows compatibility(currently linux only)

from multiprocessing import Pool, Queue
import os
import multiprocessing
import re
import shutil


def process(queue):
    while not queue.empty():
        filename = queue.get()
        print(multiprocessing.current_process())
        print(filename)
        regex = re.compile('{}'.format(searchString))
        searchfile = open(filename, encoding='ISO-8859-1', mode='r')
        for line in searchfile:
            if regex.search(line) is not None:
                results.append(line)
        searchfile.close()
    with open("superGrepResults/results.txt", encoding='ISO-8859-1', mode='a+') as result:
        for item in results:
            result.write(item)


# - Start

results = []
dir1 = 'superGrepResults'
if os.path.exists(dir1):
    shutil.rmtree(dir1)
    os.makedirs(dir1)
else:
    os.makedirs(dir1)
print('Run in same dir as text files to search')
searchString = input('Input regex search: ')
if __name__ == '__main__':
    queue = Queue()
    for dpaths, sdirs, files in os.walk('.'):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(dpaths, file)
                queue.put(filepath)
    pool = Pool(None, process, (queue,))
    pool.close()
    pool.join()


