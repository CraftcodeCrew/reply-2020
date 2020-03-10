import numpy as np

def main():
    
     print("hello, best team evvaaaa!")
     
     some_data = (10, 11, 12, 13, 14, 15)
     some_permuted_data = np.random.permutation(some_data)
     print(some_permuted_data)
     print("random permutation of length 3: " +  str(np.random.permutation(3)))
     


if __name__ == "__main__":
    # execute only if run as a script
    main()