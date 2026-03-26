class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print("Up to:", self.current)
    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print("Down to:", self.current)
    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()
e = Elevator(1, 10)
e.go_to_floor(5)
e.go_to_floor(1)

class Building:
    def __init__(self, bottom, top, num):
        self.elevators = []
        for i in range(num):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, number, target):
        self.elevators[number].go_to_floor(target)

# chạy 
b = Building(1, 10, 3)

b.run_elevator(0, 6)
b.run_elevator(1, 4)
b.run_elevator(2, 8)