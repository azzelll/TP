genome_file_ls = ["vibrio_cholerae.txt", "e_coli.txt", "ori_vibrio_cholerae.txt"]

def open_file():
    genome_file = input("Genome file name: ")
    while genome_file not in genome_file_ls:
        print("File not found")
        genome_file = input("Genome file name: ")
    with open(genome_file, "r") as file:
        genome_file = file.read()
    return genome_file

def main_menu():
    print("Choose an option:")
    print("[1] Compute a reverse complement of a k-mer pattern")
    print("[2] Count a k-mer pattern")
    print("[3] Find most frequent k-mer patterns")
    option = input("Select an operation [1/2/3]: ") 
    while option not in ["1", "2", "3"]:
        print("Invalid input")
        option = input("Select an operation [1/2/3]: ")
    return option

def func1(variable):
    result=""
    for char in variable[::-1]:
        if char == "A":
            result += "T"
        elif char == "C":
            result += "G"
        elif char == "G":
            result += "C"
        elif char == "T":
            result += "A"
    return result
def func2(variable):
    pattern = input("Input your pattern: ")
    while pattern not in variable:
        print("Pattern not found")
        pattern = input("Input your pattern: ")
    count=0
    k_mer_reversed = func1(pattern)
    for i in range(len(variable)):
        if variable[i:i+len(pattern)] == pattern:
            count += 1
        if variable[i:i+len(pattern)] == k_mer_reversed:
            count += 1
    print(count)

def func3(variable):
    k = (input("Input your value of k: "))
    validation = False
    while validation == False:
        try:
            k = int(k)
            validation = True
        except:
            print("Invalid input")
            k = (input("Input your value of k: "))
    try:
        k = int(k)
    except:
        print("Invalid input")
        k = (input("Input your value of k: "))
    while k > len(variable):
        print("k is too large")
        k = int(input("Input your value of k: "))
    result = []
    count_f = 0
    for i in range(len(variable)):
        variable_n = variable[i:i+k]
        count_1 = 0
        if len(variable_n) == k and variable_n not in result:
            for i in range(len(variable)):
                if variable[i:i+k] == variable_n:
                    count_1 += 1
        if count_1 > count_f:
                result.clear()
                result.append(variable_n)
                count_f = count_1
        elif count_1 == count_f:
            result.append(variable_n)
    for i in result:
        print(i)

if __name__=="__main__":
    genome_file = open_file()
    option = main_menu()
    if option == "1":
        Input_variable = input("Input your variable: ")
        result = func1(Input_variable)
        print(result)
    elif option == "2":
        func2(genome_file)
    elif option == "3":
        func3(genome_file)