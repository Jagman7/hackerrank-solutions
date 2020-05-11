

def check():
    return "Yeah its working !!"


def Alphabet_Rangoli():
    n = 3  ;
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    column_count = n + (n-1) + (n + (n-2))
    row_count = n + (n-1)

    final_output = []

    for y in range(row_count):
        str = ""
        for x in range(column_count):
            str = str + "-"
        final_output.append(str)

    center =  int(column_count/2)
    count = 0
    char_add_count = 1
    # print(center)
    for xx in final_output:
        nlist = list(xx)
        temp_cen = center
        alpha_strt = n-1
        ############ adding char ###################
        if count <= int(len(final_output)/2):
            nlist[temp_cen]=alpha[alpha_strt]
            for u in range(char_add_count):
                print("char: ",u," round: ", int(char_add_count/2), "al :", alpha[alpha_strt])
                nlist[temp_cen]=alpha[alpha_strt]
                temp_cen = temp_cen + 2
                if u < int(char_add_count/2):
                    alpha_strt = alpha_strt - 1
                else:
                    alpha_strt = alpha_strt + 1

        #############################################

        xx = "".join(nlist)
        final_output[count] = xx
        count = count + 1
        char_add_count = char_add_count + 2
        center = center - 2
        # if count == 3:
        #     print("Break hua")
        #     break



    print(*final_output, sep = "\n")
    # print(len(final_output))
