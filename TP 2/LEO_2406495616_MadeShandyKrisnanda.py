from collections import defaultdict

def open_file(): #Opening the file and reading it
    genome_file = input("Genome file name: ")
    validation_file = False
    while validation_file != True:
        try:
            with open(genome_file, "r") as file:
                genome_file = file.read().strip()
                validation_file = True
                return genome_file
        except FileNotFoundError:
            print("File not found")
            genome_file = input("Genome file name: ")

def main_menu(): #Give the user the option to choose what they want to do
    print("Choose an option:")
    print("[1] Compute a reverse complement of a k-mer pattern")
    print("[2] Count a k-mer pattern")
    print("[3] Find most frequent k-mer patterns")
    user_option = input("Select an operation [1/2/3]: ") 
    while user_option not in ["1", "2", "3"]: #Validating input
        print("Invalid input")
        user_option = input("Select an operation [1/2/3]: ")
    return user_option

def reverse_patern(): #Reverse the pattern according to user input
    ask_k_mer = input("Input your pattern: ").upper()
    while ask_k_mer: #Validating input
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
    print(reversed_k_mer)

def count_k_mer(genome): #Count the pattern according to user input
    search_pattern = input("input your pattern: ").upper
    while search_pattern not in genome: #Validating input
        print("Pattern not found")
        search_patter = input("Input your pattern: ")
    count_pattern = 0
    k_mer_reversed = reverse_patern(search_pattern)
    for i in range(len(genome)-len(search_pattern)+1):
        if genome[i:i+len(search_pattern)] == search_pattern:
                count_pattern += 1
        if genome[i:i+len(search_pattern)] == k_mer_reversed:
                count_pattern += 1
    print(count_pattern)
        
def frequent_k_mer(genome): #Find the most frequent k-mer
    len_k_mer = (input("Input your value of k: "))
    validation_len_k_mer = False
    while validation_len_k_mer == False: #Validating input
        try:
            len_k_mer < 0 == True
            len_k_mer = int(len_k_mer)
            validation_len_k_mer = True
        except:
            print("Invalid input")
            len_k_mer = (input("Input your value of k: "))
    while len_k_mer > len(genome): #Validating input
        print("k is too large")
        len_k_mer = int(input("Input your value of k: "))
    genome_ls = defaultdict(int)
    for i in range(len(genome)-len_k_mer+1): #Count the k-mer
            genome_pattern = genome[i:i+len_k_mer]
            genome_ls[genome_pattern] += 1
    sorted_genome_ls = sorted(genome_ls.items(), key=lambda x: x[1], reverse=True) #Sort the k-mer
    frequent_k_mer_ls = []
    for genome, i in sorted_genome_ls: #Find the most frequent k-mer and put it in a list
        if i == sorted_genome_ls[0][1]:
            frequent_k_mer_ls.append(genome)
    for k_mer in frequent_k_mer_ls:
        print(k_mer)

def main(): #Main function
    genome_file = open_file()
    user_option = main_menu()
    if user_option == "1":
        reverse_patern()   
    elif user_option == "2":
        count_k_mer(genome_file)
    elif user_option == "3":
        frequent_k_mer(genome_file)

if __name__=="__main__": #Run the main function
   main()