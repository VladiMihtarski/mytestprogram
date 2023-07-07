def generate_bit_vectors(n, vector):
    if n == 0:
        print(vector)
    else:
        generate_bit_vectors(n - 1, vector + "0")
        generate_bit_vectors(n - 1, vector + "1")

def main():
    n = int(input())
    generate_bit_vectors(n, "")

main()


