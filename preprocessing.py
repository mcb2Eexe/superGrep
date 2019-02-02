# - supergrep V1
# - Written by: McB
# - Last modified: 02 Feb 2019
# - Designed to search multiple large text files for a simple string match
# - Uses multiprocessing to search multiple files concurrently
# - To do's = add regex searching,
# - To do's = add counters for total files, files remaining, number of matches
# - Add Windows support (currently Linux only)

from multiprocessing import Pool, Queue
import os
import multiprocessing

def process(queue):
    while not queue.empty():
        dir1 = 'results'
        if not os.path.exists(dir):
            os.makedirs(dir1)
        filename = queue.get()
        print(multiprocessing.current_process())
        print(filename)
        searchfile = open(filename, 'r')
        for line in searchfile:
            if searchString in line:
                with open("results/results.txt", "a+") as result:
                    result.write(line)
        searchfile.close()

if __name__ == '__main__':
    searchString = input('Enter string to search: ')
    queue = Queue()
    for f in os.listdir('.'):
        if f.endswith('.txt'):
            queue.put(f)
    pool = Pool(None, process, (queue,))
    pool.close()
    pool.join()


