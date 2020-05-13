

def check():
    return "Yeah its working !!"

def Word_Order():
    import sys

    stdin_fileno = sys.stdin
    # stdout_fileno = sys.stdout
    total_lines = 0
    count_in = -1
    main_arr = []
    for line in stdin_fileno:
        # print("count_in :",count_in,"total :", total_lines)
        if count_in == total_lines:
            main_arr.append(str(line.strip()))

            # list_set = set(main_arr)
            # unique_list = (list(list_set))

            # print(unique_list)
            # print(main_arr)
            # ['q', 'a', 'q', 'x']
            unq_arr = []
            prod_arr = []
            for x in main_arr:
                check = False
                for y in unq_arr:
                    if x == y:
                        check = True
                if check == False:
                    unq_arr.append(x)
                    char_count = 0
                    for xx in main_arr:
                        if x == xx:
                            char_count = char_count + 1
                    prod_arr.append(char_count)

            # print(unq_arr)
            # print(prod_arr)

            # stdout_fileno.write(str(len(unq_arr)) + '\n')
            print(str(len(unq_arr)))
            # str_m = ""
            c = False
            # for f in prod_arr:
            #     if c == False:
            #         str_m = str_m + str(f)
            #         c=True
            #     else:
            #         str_m = str_m + " " + str(f)
            # print(str_m)
            # stdout_fileno.write(str(str_m) + '\n')
            print(*prod_arr, sep = " ")

            exit(0)
        else:
            if count_in == -1:
                total_lines = int(line)
                count_in = 0
                count_in = count_in + 1
            else:
                main_arr.append(str(line.strip()))
                count_in = count_in + 1

def DefaultDict_Tutorial():
    import sys

    stdin_fileno = sys.stdin
    stdout_fileno = sys.stdout
    count_in = -1
    total_lines = 0
    n = 0
    m = 0
    arr_n = []
    arr_m = []
    n_count = 1
    # print("count_in :",count_in,"total :", total_lines)
    for line in stdin_fileno:
        # print("count_in :",count_in,"total :", total_lines)
        if count_in == total_lines:
            # print('Found exit. Terminating the program')
            # exit(0)
            # stdout_fileno = sys.stdout
            value = str(line.strip())
            arr_m.append(value)
            final_output = []

            for x in arr_m:
                temp_arr=[]
                poss = 1
                check=0
                for y in arr_n:
                    if x == y:
                        temp_arr.append(poss)
                        check = 1
                    # if check == 0:
                    #     temp_arr.append(-1)
                    poss = poss + 1
                final_output.append(temp_arr)

            for c in range(len(final_output)):
                if len(final_output[c]) == 0:
                    final_output[c].append(-1)

            # print("final :", final_output)


            # sample_input = ['Hi', 'Hello from AskPython', 'exit']
            for ip in final_output:
                temp_out = ""
                bb=0
                for v in ip:
                    # print("v: ",v)
                    if bb == 0:
                        temp_out = temp_out + str(v)
                        bb = bb + 1
                    else:
                        temp_out = temp_out + " " + str(v)
                # print("# TEMP: ",temp_out)
                stdout_fileno.write(temp_out + '\n')
            exit(0)
        else:
            if count_in == -1:
                value = (line.strip()).split(" ")
                n = int(value[0])
                m = int(value[1])
                total_lines = n + m
                count_in = 0
                count_in = count_in + 1
            else:
                value = str(line.strip())
                if n_count <= n:
                    arr_n.append(value)
                    n_count = n_count + 1
                else:
                    arr_m.append(value)
                count_in = count_in + 1



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
