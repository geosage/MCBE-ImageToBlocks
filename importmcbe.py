def mcbeimage(imagenames, num_cols, num_rows):
    blockrows = []
    col_idx = 0
    row_idx = 0
    for i in range(len(imagenames)):
        print(row_idx)
        if col_idx != num_cols:
            blockrows[row_idx].append(imagenames[i])
            col_idx = col_idx + 1
        else:
            row_idx = row_idx + 1
            col_idx = 0

    print(blockrows)
