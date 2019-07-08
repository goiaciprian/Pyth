#!usr/bin/env python

import threading
import time


def sleeper(n, thread_name):
    print(f'I am {thread_name} and I will sleep for {n}')
    time.sleep(n)
    print(f'{thread_name} woke up.')


t = threading.Thread(target=sleeper, name='Thread1', args=(5, 'Thread1'))

if __name__ == "__main__":
    t.run()
