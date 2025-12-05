class DoorLock:
    def __init__(self):
        self.lower_bound = 0
        self.upper_bound = 99
        self.starting_point = 50
        self.current_point = self.starting_point
        self.range_size = self.upper_bound - self.lower_bound + 1
        self.total_zeroes = 0
        self.inputs_file_path = "Day1/resources/input.txt"
        self.instructions = []

        self.load_instructions()

    def spin(self, instruction: str, part: int):
        # Parse the spin direction and number
        direction = instruction[0]
        number = int(instruction[1:])

        if part == 1:
            # Check if fist char is a L or R
            if direction == "L":
                # Spin left (subtract)
                self.current_point = (self.current_point - number) % self.range_size

            if direction == "R":
                # Spin right (add)
                self.current_point = (self.current_point + number) % self.range_size

            # Tally it if it landed on 0
            if self.current_point == 0:
                self.total_zeroes += 1
        
        if part == 2:
            if direction == "R":
                # count passes during rotation
                self.total_zeroes += (self.current_point + number) // self.range_size
                # update pos
                self.current_point = (self.current_point + number) % self.range_size

            elif direction == "L":
                self.total_zeroes += (number - self.current_point - 1) // 100 + 1
                self.current_point = (self.current_point - number) % self.range_size

            # count if it *lands* on zero
            if self.current_point == 0:
                self.total_zeroes += 1

    
    def load_instructions(self):
        try:
            with open(self.inputs_file_path, 'r') as f:
                self.instructions = [line.rstrip('\n') for line in f]
        except FileNotFoundError:
            print(f"Error: The file '{self.inputs_file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def solve(self, part: int):
        for instruction in self.instructions:
            self.spin(instruction=instruction, part=part)
        
        print(f"Total Zeroes: {self.total_zeroes}")


if __name__ == '__main__':
    puzzle1 = DoorLock()
    puzzle1.solve(part=1)

    puzzle2 = DoorLock()
    puzzle2.solve(part=2)
