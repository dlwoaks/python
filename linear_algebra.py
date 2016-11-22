def matrix(m, n):
    # creates an mxn matrix initialized to 0s
    A = [m][n]
    for i in range(m):
        for j in range(n):
            A[i][j] = 0
    def insert_vector(v):
        # inserts an extra vector
        try:
            A.append(v)
            m+=1
        except:
            print("invalid format/ invalid vector length")
        else:
            print("insertion successful")
        finally:
            for i in range(m):
                print("\n")
                for j in range(n):
                    print(A[m][n] + " ")
