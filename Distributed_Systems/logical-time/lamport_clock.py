# Adopted and adapted from https://towardsdatascience.com/understanding-lamport-timestamps-with-pythons-multiprocessing-library-12a6427881c6
from multiprocessing import Process, Pipe
from time import sleep


def local_event(pid, clock):
    clock += 1
    print('Process {} performed local event. Lamport timestamp is {}'.format(pid, clock))
    return clock


def send_event(pipe, pid, clock):
    clock += 1
    pipe.send((pid, clock))
    print('Process {} sent message. Lamport timestamp is {}'.format(pid, clock))
    return clock


def receive_event(pipe, pid, clock):
    sender_id, ts = pipe.recv()
    clock = max(ts, clock) + 1
    print('Process {} received message from Process {}. Lamport timestamp is {}'.format(pid, sender_id, clock))
    return clock


def process_one(pipe12):
    pid = 1
    clock = 0
    clock = local_event(pid, clock)
    clock = send_event(pipe12, pid, clock)
    # sleep(3)
    clock = local_event(pid, clock)
    clock = receive_event(pipe12, pid, clock)
    clock = local_event(pid, clock)


def process_two(pipe21, pipe23):
    pid = 2
    clock = 0
    clock = receive_event(pipe21, pid, clock)
    clock = send_event(pipe21, pid, clock)
    clock = send_event(pipe23, pid, clock)
    clock = receive_event(pipe23, pid, clock)


def process_three(pipe32):
    pid = 3
    clock = 0
    clock = receive_event(pipe32, pid, clock)
    clock = send_event(pipe32, pid, clock)


if __name__ == '__main__':
    one_two, two_one = Pipe()
    two_three, three_two = Pipe()

    process1 = Process(target=process_one, args=(one_two,))
    process2 = Process(target=process_two, args=(two_one, two_three))
    process3 = Process(target=process_three, args=(three_two,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
