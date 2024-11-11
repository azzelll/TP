import time
def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1
    for j in range(low,high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    return i + 1
def quicksort(lst, low = 0, high = 1):
    if low<high:
        q = partition(lst, low, high)
        quicksort(lst, low, q-1)
        quicksort(lst, q+1, high)
def header():
    print("""
TP 03 DDP1 -- 2024
Implementation of QuickSort
============================
""")
def input_user():
    file_input = (input("Enter the name of the input file: "))
    file_output = (input("Enter the name of the output file: "))
    return file_input, file_output
def read_file(file_input):
    validate = False
    while not validate:
        try:
            with open(file_input, 'r') as f:
                lst = [int(line.strip()) for line in f]
            validate = True
        except FileNotFoundError:
            print("File not found")
            file_input = input("Enter the name of the input file: ")
    return lst
def write_file(file_output, lst):
    with open(file_output, 'w') as f:
        for i in lst:
            f.write(str(i) + '\n')
def main():
    header()
    unsorted_file, sorted_file = input_user()
    #constructing the list of numbers, using list comprehension
    numbers = read_file(unsorted_file)
    t1 = time.time()
    t = time.process_time()
    print(numbers[0:10])
    print("Sorting in progress ...")
    quicksort(numbers,0,len(numbers)-1)

    cpu_time = time.process_time() - t
    duration = time.time() - t1
    #writing the sorted numbers to the output file
    write_file(sorted_file, numbers)
    print("CPU time of the quicksort: ", cpu_time)
    print("Clock time of the quicksort: ", duration)
if __name__ == '__main__':
    main()