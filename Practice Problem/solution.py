# Google Hashcode 2021 Practice Problem

# function to process input file and extract values
def file_processing(file):
    # this method is more efficient when working with big data
    with open(file + ".in") as f:
        opened_file = [line.strip().split() for line in f] #a list of list such that each line is a list
        
    first_line = opened_file[0] #assigns first line in the list of list to first_line variable
    
    print("There are {} pizzas for {}".format(first_line[0], file))
    print("{} team of two".format(first_line[1]))
    print("{} team of three".format(first_line[2]))
    print("{} team of four\n".format(first_line[3]))
    
    return opened_file #returns the list of list

# function to accept input values and solve the problem
def solve(input_data):    

    pass

# contains the functions to run
def main():
    for each_file in ["a_example", "b_little_bit_of_everything", "c_many_ingredients", "d_many_pizzas","e_many_teams"]:
        f = file_processing(each_file) # processes each file

        answer = solve(f) #solves each file

        # writes each answer to a new file and save it with their dataset name in a text format
        f = open("../solution/" + each_file + ".out", "w") 
        f.write(str(answer))
        f.close()

if __name__ == '__main__':
    main()


# Done!