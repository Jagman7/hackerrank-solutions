

def check():
    return "Yeah its working !!"

def DefaultDict_Tutorial():
    import sys

    stdin_fileno = sys.stdin
    count_in = 0
    total_lines = 0
    for line in stdin_fileno:
        if 'exit' == line.strip():
            # print('Found exit. Terminating the program')
            # exit(0)
            stdout_fileno = sys.stdout
            sample_input = ['Hi', 'Hello from AskPython', 'exit']
            for ip in sample_input:
                # Prints to stdout
                stdout_fileno.write(ip + '\n')
            exit(0)
        else:
            if count_in == 0:
                value = (line.strip()).split(" ")
                total_lines = int(value[0]) + int(value[1])
                print(total_lines)


def Alphabet_Rangoli():
    n = 3 ;
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
                # print("char: ",u," round: ", int(char_add_count/2), "al :", alpha[alpha_strt])
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
##########################################################################

    center =  int(column_count/2)
    count = 1
    char_add_count = 1


    count = 0
    count_al = 1
    for yy in reversed(final_output):
        nlist = list(yy)
        temp_cen = center
        alpha_strt = n-1

        if count <= int(len(final_output)/2):
            nlist[temp_cen]=alpha[alpha_strt]
            for u in range(char_add_count):
                # print("count: ",count,"char: ",u," round: ", int(char_add_count/2), "al :", alpha[alpha_strt])
                nlist[temp_cen]=alpha[alpha_strt]
                temp_cen = temp_cen + 2
                if u < int(char_add_count/2):
                    alpha_strt = alpha_strt - 1
                else:
                    alpha_strt = alpha_strt + 1

        yy = "".join(nlist)
        # print("yy :",yy)
        final_output[len(final_output)-count_al] = yy
        count_al = count_al + 1
        count = count + 1
        char_add_count = char_add_count + 2
        center = center - 2


    print(*final_output, sep = "\n")
    # print(len(final_output))
