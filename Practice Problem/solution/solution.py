# Google Hashcode 2021 Practice Problem

# function to process input file and extract values
def file_processing(file):
    # this method is more efficient when working with big data
    with open(file + ".in") as f:
        opened_file = [line.strip().split() for line in f] #a list of list such that each line is a list

    first_line = opened_file[0]
    opened_file = opened_file[1:]
    
    return first_line, opened_file #returns the first line and then the list of list without the first_line

# function to accept input values and solve the problem
def solve(input_data):    

    return answer # answer is a list of list where each list have its first value to be the number of people in the team and subsequent values as indexes of the pizza in the original file that will be given to that team

# contains the functions to run
def main():
    for each_file in ["a_example", "b_little_bit_of_everything", "c_many_ingredients", "d_many_pizzas","e_many_teams"]:
        f = file_processing(each_file) # processes each file

        answer = solve(f) #solves each file and returns the each delivery to a new line
        
        output_file = open("../solution/" + each_file + ".out", "w") # writes each answer to a new file and save it with their dataset name in a out format
        output_file.write(str(len(answer)) + "\n") # frist line in file is the total number of teams delivered to i.e the number of length of our list of list, answer
        output_file.write(answer)
        output_file.close()

if __name__ == '__main__':
    main()


# Done!