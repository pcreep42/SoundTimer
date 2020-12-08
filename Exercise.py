from SoundTimer import SoundTimer


def parse_key_t(input_string: str) -> tuple:
    """
    :param input_string: gets starting string with -t key, and parse it to int values
    :return: a tuple where [1] int: exercise iteration time, [2] int: rest time
    """
    input_keys = input_string[input_string.find('-t'):].split()
    if len(input_keys) > 3 or len(input_keys) == 3 and '-' not in input_keys[2]:
        return int(input_keys[1]), int(input_keys[2])
    elif len(input_keys) == 3 and '-' in input_keys[3]:
        return int(input_keys[1]),
    elif len(input_keys) < 3:
        return int(input_keys[1]),


def parse_initial_info(initial_info: str) -> dict:
    parsed_info = {
        'selected_scenario': int(initial_info.split()[0]),
        'preparation': True if '-p' in initial_info else False,
        'specific_time': parse_key_t(initial_info) if '-t' in initial_info else False
    }
    return parsed_info


class Exercise:
    def __init__(self, initial_info: str):
        self._exercise_timer = SoundTimer()

        parsed_initial_info = parse_initial_info(initial_info)

        self._preparation = parsed_initial_info['preparation']
        self._selected_scenario = parsed_initial_info['selected_scenario']
        self._iterations_count = 0

        specific_time = parsed_initial_info['specific_time'] if parsed_initial_info['specific_time'] else (60, 30)
        if len(specific_time) == 2:
            self._iteration_time = specific_time[0]
            self._rest_time = specific_time[1]
        else:
            self._iteration_time = None
            self._rest_time = specific_time[0]

    def print_iteration_count_info(self):
        print(f'End of {self._iterations_count} iteration')

    def execute_scenario(self):
        if self._selected_scenario == 1:
            self._superman()
        elif self._selected_scenario == 2:
            self._s_c_a_e()
        elif self._selected_scenario == 3:
            self._rest_time_for_exercise()

    def _start_rest_time(self, rest_time_duration: int):
        self._exercise_timer.count_n_call(rest_time_duration)

    def _start_preparation_time(self):
        self._exercise_timer.count_n_call(10)

    def _start_iteration(self, iteration_duration: int):
        self._exercise_timer.count_n_call(iteration_duration)

    def _exercise_loop(self, exercise_qty: int, exercise_duration: int, rest_time_duration: int):
        if self._preparation:
            self._start_preparation_time()
        for exercise in range(exercise_qty - 1):
            # making loop smaller to not have rest time after whole __exercise_loop method
            self._start_iteration(exercise_duration)
            self._start_rest_time(rest_time_duration)
        self._start_iteration(exercise_duration)  # last iteration without rest_time in the end
        self._iterations_count += 1  # get whole circle quantity
        self.print_iteration_count_info()

    #  Exercises are lower:

    def _s_c_a_e(self):
        self._exercise_loop(4, self._iteration_time, self._rest_time)

    def _superman(self):
        self._exercise_loop(2, self._iteration_time, 10)

    def _rest_time_for_exercise(self):
        self._iterations_count += 1
        self.print_iteration_count_info()
        self._start_iteration(60)
