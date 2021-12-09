# try :
#     fd = open("aaa.txt","r")
# except IOError:
#     print "error :file not found"
# else :
#     l = fd.readlines()
#     for i in l :
#         print i
# finally:
#     try :
#
#         if not fd.closed:
#             fd.close()
#     except NameError:
#         print "its not defined"
#     print "Read DoNe"
def makeAnagram(a, b):
    # Write your code here
    count = 0
    new_list = []
    for i in b:
        if i not in a:
            count += 1
    for j in a:
        if j not in b:
            count += 1
    for ele in a:
        if ele in b and ele not in new_list:
            if a.count(ele) > 1 or b.count(ele)>1 :
                count = count + abs(a.count(ele)-b.count(ele))
                new_list.append(ele)
    return count
# res = makeAnagram("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke")
# res = makeAnagram("cdec","cabccc")
# print(res)


def alternate(s):
    count = 0
    for index,value in enumerate(s) : # 3 A
        if s[index-1] == value and index>0:
                count = count + 1
    return count
# output = alternate("AAAA")
# print(output)

def isValid(s):
    # Write your code here
    d = {}
    for element in s:
        if element not in d:
            d.update({element: s.count(element)})
    count = 0
    print(d)

    for value in d.values():

        if max(d.values()) == value:
            pass
        else:
            if max(d.values()) -value == 1:
                count = count + 1
    print(count)
    if count >= 2:
        return "NO"
    else:
        return "YES"
# res = isValid("abcdefghhgfedecba")
# aabbccddeeffgghh
# print(res)


def substring_count(s):
    count = len(s)
    for i in range(len(s)):
        for j in range(1,len(s)+1):
            var = s[i:j]
            if var == var[::-1] and len(var)>1:
                if len(var)%2 == 1:
                    if var[:len(var)//2] ==var[len(var)//2+1:]:
                        count = count+1
                else:
                    count = count +1
    return count

substring_count("asasd")