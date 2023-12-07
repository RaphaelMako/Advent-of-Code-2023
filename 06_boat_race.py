import re
import math
import sys

data = '''Time:        40     82     91     66
Distance:   277   1338   1349   1063'''

def part_one(data):
    # Data splitting:
    data = data.split('\n')
    data[0] = data[0].split(':')[1]
    data[1] = data[1].split(':')[1]

    data[0] = re.findall(r'\d+', data[0])
    data[1] = re.findall(r'\d+', data[1])

    def min_time_finder(time, distance):
        count = 0
        min = sys.maxsize
        print('distance: ', distance)
        while (count < time):
            if (count * (time - count) > distance):
                min = count
                break
            else:
                count += 1
                continue
        return min

    def max_time_finder(time, distance):
        count = time
        max = 0
        while count > 0:
            if (count * (time - count) > distance):
                max = count
                break
            else:
                count -= 1
                continue
        return (max + 1)
    
    def main():

        total = 1
        for i, race in enumerate(data[0]):
            number = (max_time_finder(int(race), int(data[1][i])) - min_time_finder(int(race), int(data[1][i])))
            total *= number
            print(number)
        
        print(total)
            
    main()


# part_one(data)

#part two I'm going to be super lazy and just change the data instead of rewriting anything

two_data = '''Time:        40829166
Distance:   277133813491063'''

part_one(two_data)