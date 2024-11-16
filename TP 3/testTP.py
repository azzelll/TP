import time

def partition(lst, low, high, reversed = False):
    if not reversed:
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1
    if reversed:
        pivot = lst[low]
        i = high + 1
        for j in range(high, low, -1):
            if lst[j] <= pivot:
                i -= 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i - 1], lst[low] = lst[low], lst[i - 1]
        return i - 1

def quicksort(lst, low=0, high=None, reversed = False):
    if high is None:
        high = len(lst) - 1
    if low < high:
        q = partition(lst, low, high, reversed)
        quicksort(lst, low, q - 1)
        quicksort(lst, q + 1, high)
        
# def quicksort_reversed(lst, low=0, high=None):
#     if high is None:
#         high = len(lst) - 1
#     if low < high:
#         q = partition_reversed(lst, low, high)
#         quicksort_reversed(lst, low, q - 1)
#         quicksort_reversed(lst, q + 1, high)

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
    reversed_input = input("Sort in reversed order (y/n): ")
    if reversed_input.lower() == 'y':
        reversed = True
    else:
        reversed = False
    return file_output, lst, reversed

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
            
def sorting(numbers, reversed):
    start_time = time.time()
    cpu_start_time = time.process_time()
    print("\nSorting in progress ...")
    quicksort(numbers, reversed=reversed)
    duration = time.time() - start_time
    cpu_time = time.process_time() - cpu_start_time
    return cpu_time, duration

def print_result(cpu_time, duration):
    print("CPU time of the quicksort: ", cpu_time)
    print("Clock time of the quicksort: ", duration)
    
def main():
    header()
    sorted_file, numbers, reversed = input_user() #constructing the list of numbers, using list comprehension
    cpu_time, duration = sorting(numbers, reversed) 
    write_file(sorted_file, numbers) #writing the sorted numbers to the output file
    print_result(cpu_time, duration)
    
if __name__ == '__main__':
    main()