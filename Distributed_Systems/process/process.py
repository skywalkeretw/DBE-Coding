from multiprocessing import Process
import os

def slute(courcse):
    print('hello', courcse)
    print("parent process id", os.getppid())
    print("Process ID:", os.getpid())

if __name__ == '__main__':
    p = Process(target=slute, args=('DS',))
    p.start()
    p.join()