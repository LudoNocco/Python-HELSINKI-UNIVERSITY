class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')

    def most_goals(self):    
        return max(self.goals)
    
    def most_points(self):
        return max(self.passes + self.goals)

    def least_minutes(self):
        return min(self.minutes)