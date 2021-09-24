def gen_group_sets(cols):
    res = [set()]
    for i in range(len(cols)):
        for j in range(i, len(cols)):
            res.append(set(cols[i:j+1]))
    print(res)

gen_group_sets(["colA", "colB", "colC"])