# get the input
def get_input() -> dict:

    with open('inputs\input2.txt', 'r') as file:
        strinput = file.read().strip()

    games = {}
    for line in strinput.split('\n'):
        val = line.split(':')
        triplets = val[1].split(';')
        ordered_triplets = get_ordered_pairs(triplets) #(r,g,b)
        games[int(val[0][5:])] = ordered_triplets

    return games

# get each game in (red, green, blue) list (done for fun)
def get_ordered_pairs(triplets: list) -> list:

    ordered_list = []
    for triplet in triplets:
        l = [0,0,0]
        number_list = triplet.strip().split(',')

        for cube in number_list:
            num, color = cube.split()

            if color == "red":
                l[0] = int(num)
            if color == "green":
                l[1] = int(num)
            if color == "blue":
                l[2] = int(num)

        ordered_list.append(tuple(l))

    return ordered_list


# solution part 1
def soln1(input_dict: dict) -> int:

    sum1 = 0
    given_pair = (12,13,14)
    for game, value in input_dict.items():
        flag = True
        for round in value:
            if round[0]>given_pair[0] or round[1]>given_pair[1] or round[2]>given_pair[2]:
                flag = False
                break
        if flag:
            sum1 += game
    return sum1

# solution part 2
def soln2(input_dict: dict) -> int:

    sum2 = 0
    for value in input_dict.values():
        min_triplet = [0,0,0]
        for round in value:
            min_triplet[0] = max(min_triplet[0],round[0])
            min_triplet[1] = max(min_triplet[1],round[1])
            min_triplet[2] = max(min_triplet[2],round[2])
        
        sum2 += min_triplet[0]*min_triplet[1]*min_triplet[2]

    return sum2


if __name__ == "__main__":
    
    games_input = get_input()
    print(soln1(games_input))
    print(soln2(games_input))
