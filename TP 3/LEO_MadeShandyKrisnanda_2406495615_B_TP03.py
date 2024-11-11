import time

def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1

def quicksort(lst, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    if low < high:
        q = partition(lst, low, high)
        quicksort(lst, low, q - 1)
        quicksort(lst, q + 1, high)
        
def header():
    print("""
TP 03 DDP1 -- 2024
Implementation of QuickSort
============================
""")
    
def input_user():
    file_input = (input("Input file name: "))
    lst = read_file(file_input)
    file_output = (input("\nOutput file name: "))
    return file_output, lst

def read_file(file_input):
    validate = False
    while not validate:
        try:
            with open(f".\\{file_input}.txt", 'r') as f:
                lst = [int(line.strip()) for line in f]
            validate = True
        except FileNotFoundError:
            print("File not found")
            file_input = input("Enter the name of the input file: ")
    return lst

def write_file(file_output, lst):
    with open(f"{file_output}.txt", 'w') as f:
        f.writelines(f"{str(i)}\n" for i in lst)
            
def sorting(numbers):
    start_time = time.time()
    cpu_start_time = time.process_time()
    print("\nSorting in progress ...")
    quicksort(numbers)
    duration = time.time() - start_time
    cpu_time = time.process_time() - cpu_start_time
    return cpu_time, duration

def print_result(cpu_time, duration):
    print("CPU time of the quicksort: ", cpu_time)
    print("Clock time of the quicksort: ", duration)
    
def main():
    header()
    sorted_file, numbers = input_user() #constructing the list of numbers, using list comprehension
    cpu_time, duration = sorting(numbers)
    write_file(sorted_file, numbers) #writing the sorted numbers to the output file
    print_result(cpu_time, duration)
    
if __name__ == '__main__':
    main()