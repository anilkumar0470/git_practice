# import fileutil
#
#
# print("ggg")
# import pdb
# pdb.set_trace()
# print("fff")
# def get_file_info(full_fname):
#     file_path = fileutil.get_path(full_fname)
#     return file_path
#
#
# filename = __file__
# filename_path = get_file_info(filename)
# print(f'path = {filename_path}')












class sample_hello():
    def __init__(self,name):
        print(" i am in hello",name)
class sample_hai():
    def __init__(self):
        print("i am in hai")
a = "hello"
b = "hela"
c = eval("sample_{}(b)".format(a))



class s :
    def __init__(self,name):
        pass
ss = s('apathapa')