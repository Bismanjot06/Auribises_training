white_square= '\u25A0'
black_square= '\u25A1'
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            print(white_square, end=' ')
        else:
            print(black_square, end=' ')
    print()