# - supergrep V1
# - Written by: McB
# - Date written: 01 Feb 2019
# - Last modified: 01 Feb 2019
# - Designed to search multiple large text files for a simple string match
# - Uses multiprocessing to search multiple files concurrently
# - To do's = add regex searching,
# - To do's = add counters for total files, files remaining, number of matches

from multiprocessing import Pool, Queue
import os

def process(queue):
    while not queue.empty():
        filename = queue.get()
        print(filename)
        searchfile = open(filename, 'r')
        for line in searchfile:
            if searchString in line:
                print(line)
                with open("results.txt", "a+") as result:
                    result.write(line)
        searchfile.close()

if __name__ == '__main__':
    searchString = input('Enter string to search: ')
    queue = Queue()
    for f in os.listdir('.'):
        if f.endswith('.txt'):
            print(f)
            queue.put(f)
    pool = Pool(None, process, (queue,))

    pool.close()
    pool.join()
