from collections import defaultdict


def read_file(filename: str) -> list:
    with open(filename) as file:
        coords = []
        max_x = 0 
        max_y = 0
        for line in file:
            line = line.rstrip().replace('->',' ').replace(',', ' ').split(' ')
            if line:
                x_1 = int(line[0])
                y_1 = int(line[1])
                x_2 = int(line[4])
                y_2 = int(line[5])

                if x_1 > max_x:
                    max_x = x_1
                if x_2 > max_x:
                    max_x = x_2
                
                if y_1 > max_y:
                    max_y = y_1
                
                if y_2 > max_y:
                    max_y = y_2

                coords.append(((x_1,y_1),(x_2,y_2)))

    return coords, max_x, max_y

            



if __name__ == '__main__':
    coordinates, x, y = read_file('input.txt')
    points_dict = defaultdict(lambda: 0)
    

    for line_coordnates in coordinates:
        starting_point = line_coordnates[0]
        ending_point = line_coordnates[1]

        x_1 = starting_point[0]
        y_1 = starting_point[1]

        x_2 = ending_point[0]
        y_2 = ending_point[1]
        
        if x_1 == x_2 or y_1 == y_2:
            
            if y_1 == y_2:
                start = x_1 if x_1 < x_2 else x_2
                end = x_2 if x_2 > x_1 else x_1
                for i in range(start, end+1):
                    points_dict[(i,y_2)] += 1

            if x_1 == x_2:
                start = y_1 if y_1 < y_2 else y_2
                end = y_2 if y_2 > y_1 else y_1
                for i in range(start, end+1):
                    points_dict[(x_1, i)] += 1
    
    score = 0
    for key, value in points_dict.items():
        if value > 1:
            score += 1
            
    print(score)
    