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