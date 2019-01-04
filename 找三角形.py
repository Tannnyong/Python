

for i in range(1,13):
    for j in range(i,13):
        for k in range(j,13):
            if i+j>k and i+k>j and j+k>i:
                if i <= 10 and j <= 10 and k <= 10:
                    if i+j+k == 24:

                        print(i,j,k)
