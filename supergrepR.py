# - supergrepR V1
# - Written by: McB
# - Last modified: 03 Feb 2019
# - Designed to search multiple large text files using regex
# - Uses multiprocessing to search multiple files concurrently
# - To do's = add counters for total files, files remaining, number of matches
# - Add windows compatibility(currently linux only)

from multiprocessing import Pool, Queue
import os
import multiprocessing
import re


def process(queue):
    while not queue.empty():
        dir1 = 'results'
        if not os.path.exists(dir1):
            os.makedirs(dir1)
        filename = queue.get()
        print(multiprocessing.current_process())
        print(filename)
        regex = re.compile('{}'.format(searchString))
        searchfile = open(filename, 'r')
        for line in searchfile:
            if regex.search(line) is not None:
                with open("results/results.txt", "a+") as result:
                    result.write(line)
        searchfile.close()


if __name__ == '__main__':
    print('Run in same dir as text files to search')
    searchString = input('Input regex search: ')
    queue = Queue()
    for f in os.listdir('.'):
        if f.endswith('.txt'):
            queue.put(f)
    pool = Pool(None, process, (queue,))
    pool.close()
    pool.join()
    
