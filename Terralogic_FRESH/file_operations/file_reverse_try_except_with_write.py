import sys


def do_revers_line(line):
    print "line:",line
    list_line = line.split()
    res_str = ""
    for each_word in list_line:
        st = ""
        l = len(each_word)
        while l>0:
            st = st + each_word[l-1]
            l = l-1
        res_str = res_str + " " +st
    return res_str.strip()


def read_file(filename):
    try:
        fd = open(filename,"r")
    except IOError:
        print "File is not exist , please give proper file"
        sys.exit()
    fd1 = open("reversed11.txt","w")
    line_list = fd.readlines()
    for each_line in line_list:
        revers_line = do_revers_line(each_line)
        fd1.write(revers_line)
        fd1.write("\n")
    fd.close()
    fd1.close()

read_file("abcde.txt")
print "file operation is done"
