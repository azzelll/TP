from collections import defaultdict

def open_file(): #Opening the file and reading it
    validated_file = False
    while not validated_file:
        try:
            genome_file = input("Genome file name: ")
            with open(f"C:\\Users\\user\\Documents\\Kuliah\\DDP\\DDP 1\\TP\\TP 2\\{genome_file}.txt", "r") as file:
                genome_file = file.read().strip()
                validated_file = True
                return genome_file
        except FileNotFoundError:
            print("File not found")
    return genome_file

def main_menu(): #Give the user the option to choose what they want to do
    print("Choose an option:")
    print("[1] Compute a reverse complement of a k-mer pattern")
    print("[2] Count a k-mer pattern")
    print("[3] Find most frequent k-mer patterns")
    print("[4] Change the genome file")
    print("[5] Exit\n")
    user_option = input("Select an operation [1/2/3]: ") 
    while user_option not in ["1", "2", "3", "4", "5"]: 
        print("Invalid input")
        user_option = input("Select an operation [1/2/3]: ")
    return user_option

def reverse_pattern(ask_k_mer): #Reverse the pattern according to user input
    while ask_k_mer:
        for char in ask_k_mer:
            if char not in ["A", "C", "G", "T"]:
                print("Invalid input")
                ask_k_mer = input("Input your pattern: ").upper()
        break
    reversed_k_mer=""
    for char in ask_k_mer[::-1]:
        if char == "A":
            reversed_k_mer += "T"
        elif char == "C":
            reversed_k_mer += "G"
        elif char == "G":
            reversed_k_mer += "C"
        elif char == "T":
            reversed_k_mer += "A"
    return reversed_k_mer

def count_k_mer(genome): #Count the pattern according to user input
    search_pattern = input("input your pattern: ").upper()
    while search_pattern not in genome: 
        print("Pattern not found")
        search_pattern = input("Input your pattern: ")
    count_pattern = 0
    k_mer_reversed = reverse_pattern(search_pattern)
    for i in range(len(genome)-len(search_pattern)+1):
        len_pattern = i+len(search_pattern)
        if genome[i:len_pattern] == search_pattern:
                count_pattern += 1
        if genome[i:len_pattern] == k_mer_reversed:
                count_pattern += 1
    print(count_pattern)
        
def frequent_k_mer_dictionary(genome): #Find the most frequent k-mer
    k_mer_valid_len = False
    while k_mer_valid_len == False: 
        try:
            len_k_mer = int((input("Input your value of k: ")))
            k_mer_valid_len = True
        except:
            print("Invalid input")
    while len_k_mer > len(genome):
        print("k is too large")
        len_k_mer = int(input("Input your value of k: "))
    genome_ls = defaultdict(int) #Set the default value of genome_ls to int
    for i in range(len(genome)-len_k_mer+1): #Count the k-mer
            genome_pattern = genome[i:i+len_k_mer]
            genome_ls[genome_pattern] += 1
            genome_ls[reverse_pattern(genome_pattern)] += 1
    max_freq = max(genome_ls.values())
    for genome in genome_ls: #Find the most frequent k-mer and put it in a list
        if genome_ls[genome] == max_freq:
            print(genome)

def frequent_k_mer_list(genome): #Find the most frequent k-mer
    k_mer_valid_len = False
    while k_mer_valid_len == False: 
        try:
            len_k_mer = int((input("Input your value of k: ")))
            k_mer_valid_len = True
        except:
            print("Invalid input")
    while len_k_mer > len(genome):
        print("k is too large")
        len_k_mer = int(input("Input your value of k: "))
    genome_ls = [] 
    genome_used = []
    count_f = 0
    for i in range(len(genome)-len_k_mer+1): #Take pattern to count it
        genome_pattern = genome[i:i+len_k_mer]
        if genome_pattern not in genome_used:
            genome_used.append(genome_pattern)
            count = 0
            for j in range(len(genome)-len_k_mer+1) : #Count the k-mer
                genome_check = genome[j:j+len_k_mer]
                if genome_pattern == genome_check:
                    count += 1
                if genome_pattern == reverse_pattern(genome_check):
                    count += 1
            if count > count_f :
                count_f = count
                genome_ls.clear()
                genome_ls.append(genome_pattern)
            elif count == count_f:
                genome_ls.append(genome_pattern)
            elif count < count_f:
                continue
    for genome in genome_ls:
        print(genome)
            

def main(): #Main function
    genome_file = open_file()
    while True:
        user_option = main_menu()
        if user_option == "1":
            k_mer_input = input("Input your pattern: ").upper()   
            print(reverse_pattern(k_mer_input))
            continue
        elif user_option == "2":
            count_k_mer(genome_file)
            continue
        elif user_option == "3":
            frequent_k_mer_dictionary(genome_file)
            continue
        elif user_option == "4":
            genome_file = open_file()
            continue
        elif user_option == "5":
            break
def delete_k_mer(genome,x,k_mer):
    len_genome_delete = len(k_mer)
    i=0
    delete = 0
    while i<len(genome)-len_genome_delete+1 and delete<x:
        if genome[i:i+len_genome_delete] == k_mer:
            genome = genome[:i] + genome[i+len_genome_delete:]
            i-=1
            delete+=1
        if genome[i:i+len_genome_delete] == reverse_pattern(k_mer):
            genome = genome[:i] + genome[i+len_genome_delete:]
            i-=1
            delete+=1
        i+=1
    print(genome)
        
delete_k_mer("CCCACTAGTCACT",2,"AGT")
# if __name__=="__main__": #Run the main function
#    main()
# function parameter genome,x,k-mer
