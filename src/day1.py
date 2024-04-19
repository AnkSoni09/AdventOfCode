# read the input
def read_input() -> str:

    with open('inputs\input1.txt', 'r') as file:

        strinput = file.read().strip()
    
    return strinput

# solution
def soln(input_txt: str) -> int:

    summ = 0
    for line in input_txt.split():
        digit = '0'
        for char in line:
            if char.isdigit():
                digit+=char
                break

        for char in line[::-1]:
            if char.isdigit():
                digit+=char
                break
        
        summ += int(digit)

    return summ

if __name__ == "__main__":
    
    strinput = read_input()
    strinput2 = strinput
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for num, name in enumerate(digits):
        strinput2 = strinput2.replace(name,f"{name}{num+1}{name}")
    
    print(soln(strinput))
    print(soln(strinput2))