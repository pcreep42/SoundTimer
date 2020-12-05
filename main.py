import winsound
import time


def count_n_call(time_qty: int):
    for time_count in range(0, time_qty):
        time.sleep(1)
        print(time_count)
    winsound.PlaySound('bell.wav', winsound.SND_NOWAIT)


def prepare_to_exercise():
    count_n_call(10)


def start_iteration(beginning_text: str, iteration_duration: int = 60):
    print(beginning_text)
    count_n_call(iteration_duration)


def s_c_a_e():
    prepare_to_exercise()
    start_iteration('First iteration')
    start_iteration('5 seconds for rest', 30)
    start_iteration('Second iteration')
    start_iteration('5 seconds for rest', 30)
    start_iteration('Third iteration')
    start_iteration('5 seconds for rest', 30)
    start_iteration('Fourth iteration')


def superman():
    prepare_to_exercise()
    start_iteration('First iteration')
    start_iteration('5 seconds for rest', 5)
    start_iteration('Second iteration')


def count_half_minute_r(time_for_rest: int = 60):
    time_for_rest = time_for_rest
    start_input = input(f'Press Enter to start. Input time to change iteration time. {time_for_rest} seconds is set.  ')
    if start_input == '':
        start_iteration(f' -- get some rest for {time_for_rest} seconds -- ', time_for_rest)
        count_half_minute_r(time_for_rest)
    elif start_input[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        time_for_rest = int(start_input)
        start_iteration(f' -- get some rest for {time_for_rest} seconds -- ', time_for_rest)
        count_half_minute_r(time_for_rest)
    else:
        question = input('Do you want to leave the program?')
        if question[0].upper() == 'Y':
            pass
        else:
            start_iteration(f' -- get some rest for {time_for_rest} seconds -- ', time_for_rest)
            count_half_minute_r(time_for_rest)


def main():
    print("select a program which you'll do:\n"
          "1. Superman\n"
          "2. Stick-Cheburashka-Airplane-Eagle\n"
          "3. One minute breaks")
    selected_program = input()
    if selected_program == '1':
        superman()
    elif selected_program == '2':
        s_c_a_e()
    elif selected_program == '3':
        count_half_minute_r()


if __name__ == '__main__':
    main()
