def do_revers_line(each_line):
    print "line:",each_line
    list_line = each_line.split()
    res_str = ""
    for each_word in list_line:
        st = ""
        l = len(each_word)
        while l>0:
            st = st + each_word[l-1]
            l = l-1
        res_str =res_str +""+st
    return res_str



def read_file(filename):
    fd = open(filename,"r")
    #fd1= open("reversed.txt","w")
    line_list = fd.readlines()
    for each_line in line_list:
        revers_line = do_revers_line(each_line)
        #fd1.write(revers_line)
        #fd1.write("\n")
        print revers_line
    fd.close()
    #fd1.close()

read_file("abcde.txt")
