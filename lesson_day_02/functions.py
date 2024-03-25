import math
signal_power=10
noise_power=4

ratio=signal_power / noise_power
decibels=10 * math.log10(ratio)
print(decibels)

radians=0.7
height=math.sin(radians)
print(height)
print(math.sqrt(9))

#FUNCTION DEFINATIONS

def print_lyrics():
    print("I'm a lumberkack, and I'm okay.")
    print("I sleep all night and work all day")

print_lyrics()

def repeat_lyrics():
    