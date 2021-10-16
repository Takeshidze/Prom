def main():
    a = list(map(int, input()))
    if a[0] + a[1] + a[2] == a[3] + a[4] + a[5]:
        print("Ты счастливчик")
    else: print("Ты лузер")

if __name__ == '__main__':
    main()