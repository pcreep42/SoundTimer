from Exercise import Exercise


class ProgramLogic:
    def __init__(self):
        self.program_init_text = """
            Input a program's number which you'll do:
            1. Superman
            2. Stick-Cheburashka-Airplane-Eagle
            3. One minute breaks
            ------------------------------------------------------------------------------
            -p                          for adding 10 seconds for prepare in the beginning
            -t time time                for adding specific time for exercise
            """
        self.exercise = None

    def run_the_program(self):
        if not self.exercise:
            self._run_exercise()

    def _get_init_info(self):
        initial_info = input(self.program_init_text)
        try:
            int(initial_info[0])
        except ValueError:
            print('Wrong input type. Exercise number should be the 1st.')
            self._get_init_info()
        return initial_info

    def _run_exercise(self):
        initial_info = self._get_init_info()
        self.exercise = Exercise(initial_info)
        self.exercise.execute_scenario()
        self._select_next_way()

    def _select_next_way(self):
        user_answer = input("""
            One more iteration?
            - Press: Enter or input: Y, yes                 for continuation
            - Input: Stop, s                                for selecting another exercise scenario
            - Input: Quit, q, exit                          for exiting the program
        """)
        if user_answer == '' \
                or user_answer.lower() == 'y' \
                or user_answer.lower() == 'yes':
            self.exercise.execute_scenario()
        elif user_answer.lower() == 's' \
                or user_answer.lower() == 'stop':
            self._run_exercise()
        elif user_answer.lower() == 'quit' \
                or user_answer.lower() == 'q' \
                or user_answer.lower() == 'exit':
            pass
        else:
            print('User answer was not recognized. Please try again.')
            self._select_next_way()
