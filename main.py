import winsound
import time


def count_n_call(time_qty: int):
    for time_count in range(0, time_qty):
        time.sleep(1)
        print(time_count)
    winsound.PlaySound('bell.wav', winsound.SND_NOWAIT)


def main():
    count_n_call(10)
    print('First iteration started')
    count_n_call(60)
    print('Iteration finished\nChange the position')
    count_n_call(5)
    print('Second iteration started')
    count_n_call(60)
    print('Well done!')


if __name__ == '__main__':
    main()
