def draw_figure(n):
    if n == 0:
        return
    else:
        print('*' * n)
        draw_figure(n - 1)
        print('#' * n)

def main():
    num = int(input())
    draw_figure(num)

main()
