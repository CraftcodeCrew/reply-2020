import numpy as np

def main():

    print('hello, best team!')
    
    some_data = (1, 2, 5, 2, 17)
    some_permutated_data = np.random.permutation(some_data)
    print(some_permutated_data)

if __name__ == "__main__":
    main()