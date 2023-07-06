def recursive_sum(arr, index):
    if index == len(arr):
        return 0
    else:
        return arr[index] + recursive_sum(arr, index + 1)

def main():
    input_string = input()
    array = list(map(int, input_string.split()))
    total_sum = recursive_sum(array, 0)
    print(total_sum)

main()
