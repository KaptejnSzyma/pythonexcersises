with open("sample.txt", 'a') as sample_file:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{0:2} times {1} is {2:<2}".format(j, i, j*i), file=sample_file)
        print("=" * 40, file=sample_file)
