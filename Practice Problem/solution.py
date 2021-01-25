# Google Hashcode 2021 Practice Problem

# function to process input file and extract values
def file_processing(file):
    f = open(file).readlines()
    print("There are {} pizzas".format(f[0][0]))
    # for i in f[1:]:
    #     print(i[0])
    return f


# function to accept input values and solve the problem
def solve(input_data):
    
    return


# function to write output values (solution) to file
def write_file():
    
    pass

# contains the functions to run
def main():
    # input_data = file_processing()
    # answer = solve(input_data)
    # write_file('', 'w')
    f = file_processing("a_example") # f is a list which contains each line of the file as an element
    answer = solve(f)
    
    

if __name__ == '__main__':
    main()


# Done!