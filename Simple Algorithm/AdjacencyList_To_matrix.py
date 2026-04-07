def adjacency_list_to_matrix(dictionary):
    listing = []
    node = len(dictionary)
    for i,(row, column) in enumerate(dictionary.items()):
        listing.append([0]*node)
        for j in column:
            listing[i][j] = 1
            
    for row in listing:
        print(row)

    return(listing)







famy = {0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}


adjacency_list_to_matrix(famy)

