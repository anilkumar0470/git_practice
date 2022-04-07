# new_list = [[1,2,3],[4,5,6],[7,8,9]]
#
# out_list = []
#
# def extract_list(input_list):
#     for index, element in enumerate(input_list):
#         if index%2 == 0:
#             out_list.extend(element)
#         else:
#             element.reverse()
#             out_list.extend(element)
#     print(out_list)
# # extract_list(new_list)
#
#
# n_list = [1,0,9,7,8,0,6,8,9,0,7,8]
#
# o_list = []
# for ele in n_list:
#     if ele == 0:
#         o_list.insert(0, ele)
#     else:
#         o_list.append(ele)
# print(o_list)








#
# list1 = [10,30, 25, 67, 23, 24,65, 76]
#
# for i in range(len(list1)):
#     for j in range(i, len(list1)):
#         if list1[i] > list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]
#
# print(list1[-2])


# try:
#     fd1 = open("sample.txt", "r")
#     fd2 = open("sample_out.txt", "w")
# except FileNotFoundError:
#     print(" given file is not found ")
# else:
#
#     content = fd1.readlines()
#     try:
#         for line in content:
#             fd2.write(line)
#     except :
#         print("not able write into file ")
#
#     fd1.close()
#     fd2.close()
# finally:
#     print("done")




dict1 = {"name":"x", "loc":"bang", "company":"com", "mob":123, "details":{"name":"j", "loc":"hyd"}}
dict2 = {"name":"x", "loc":"bang", "company":"temp", "mob":123, "details":{"name":"kkk", "loc":"hyd"}}


# def compare_dicts(input_dict1, input_dict2):
#
#     for key, value in input_dict1.items():
#         if type(value) ==dict:
#
#             for k, v in value.items():
#                 if key in input_dict2:
#                     if value ==  input_dict2[key]:
#
#                             print("both values are same ")
#                     else:
#                             print("both values not same ")
#
#
#         if key in input_dict2:
#             if input_dict1[key] == input_dict2[key]:
#                 print("key and value are same  {}".format(key))
#             else:
#                 print("key and value are not same {} {}".format(input_dict1[key], input_dict2[key]))
#
#
# compare_dicts(dict1, dict2)
#
#
# import PyPDF2
#
# # creating a pdf file object
# pdfFileObj = open('sample.pdf', 'rb')
#
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# # printing number of pages in pdf file
# print(pdfReader.numPages)
#
# # creating a page object
# pageObj = pdfReader.getPage(0)
#
# # extracting text from page
# import pdb
# pdb.set_trace()
# print(pageObj.extractText())
#
# # image_list = pdf.getPageImageList(0)
#
# # closing the pdf file object
# pdfFileObj.close()
#
# #
# #import the library
# import fitz
#
# file = 'sample.pdf'
#
# #open the fitz file
# pdf = fitz.open(file)
#
# #select the page number
# image_list = pdf.getPageImageList(0)
# print(image_list)
#
# # #applying the loop
# # for image in image_list:
# #    xref = image[0]
# #    pix = fitz.Pixmap(pdf, xref)
# #    if pix.n < 5:
# #        pix.writePNG(f'{xref}.png')
# #    else:
# #        pix1 = fitz.open(fitz.csRGB, pix)
# #        pix1.writePNG(f'{xref}.png')
# #        pix1 = None
# #    pix = None
# #
# # #print the images
# # print(len(image_list), 'detected')