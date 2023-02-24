# Class for charcter

class Character:
    '''Represents a playable character'''
    # A class variable, counting the number of robots
    
    def __init__(self,name) -> None:
        self.name = name
        self.stats = {'strength':0, 'dexterity':0, 'constitution':0, 'intelligence':0,'widsom':0,'charisma':0}
    
    
    def getStats(self):
        return self.stats
    
    def getStat(self,stat_name):
        return self.stats[stat_name]
    
    def getModifiers(self):
        return self
    
    
    
    
    
#     population = 0
#     def __init__(self, name):
#         '''Initializes the data.'''
#         self.name = name
#         print('(Initializing {})'.format(self.name))
#         # When this person is created, the robot
#         # adds to the population
#         Robot.population += 1
#     def die(self):
#         '''I am dying.'''
#         print('{} is being destroyed!'.format(self.name))
#         Robot.population -= 1
#         if Robot.population == 0:
#             print('{} was the last one.'.format(self.name))
#         else:
#             print('There are still {:d} robots working.'.format(
#                 Robot.population))
#     def say_hi(self):
#         '''Greeting by the robot.
#         Yeah, they can do that.'''
#         print('Greetings, my masters call me {}.'.format(self.name))
#     @classmethod
#     def how_many(cls):
#         '''Prints the current population.'''
#         print('We have {:d} robots.'.format(cls.population))
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# Robot.how_many()
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# Robot.how_many()
# print('Robots can do some work here.')
# print('Robots have finished their work. So lets destroy them.')
# droid1.die()
# droid2.die()
# Robot.how_many()