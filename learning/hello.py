# # sample_input = [1,2,[3,4,5, [1,2,3]],[[6]]]
# # output = [1,2,3,4,5,6]
# #
# # empty_list =[]
# # def list_extraction(new_list=[], empty_list=[]):
# #
# #     for i in new_list :
# #         if type(i) == list:
# #             list_extraction(i)
# #         else:
# #             empty_list.append(i)
# #     return empty_list
# #
# #
# # print(list_extraction(sample_input))
# #
# #
# # def sample(a, test_list=[]):
# #     if test_list != []:
# #         test_list =[]
# #     test_list.append(a)
# #     print(test_list)
# #
# # sample(10)
# # sample(20)
# # sample(30)
# #
# #
# # #
# # def sample_function(a, b):
# #     for i in range(len(a)):
# #        for j in range(1,len(a)):
# #            if a[i] + a[j] == b:
# #                print(a[i], a[j])
# #
# # sample_function([1,2,3,4], 5)
# # #
# # #
# # # #
# # # # def sample_decorator(original_function):
# # # #     def test_wrapper(*args, **kwargs):
# # # #         print("i am inside wrapper")
# # # #         original_function(*args, **kwargs)
# # # #
# # # #     return test_wrapper
# # # #
# # # # @sample_decorator
# # # # def display(a):
# # # #     print("i am inside display function {} ".format(a))
# # # #
# # # # display(10)
# # #
# # #
# # # # l1 =  [1,3,4,7,8]
# # # # l2 =  [2,5]
# # # # # [1,2,3,4,5,7,8,9]
# # # #
# # # # new_list = []
# # # #
# # # # for i in range(len(l1)):
# # # #     for j in range(len(l2)):
# # # #         if l1[i] > l2[j] < l1[i+1]:
# # # #             new_list.append()
# # #
# # #
# # #
# # # # def list_sorted_func(a,b):
# # # #     final_list = []
# # # #     i, j = 0, 0
# # # #     while a[i] > :
# # # #
# # # #     return final_list
# # # # print(list_sorted_func([1,3,4,7,8], [2,5]))
# # #
# # # import re
# # #
# # #
# # # def replace_function(file_path, replaced_text):
# # #     fd = open(file_path, 'r+')
# # #     file_content = fd.readlines()
# # #
# # #     new_string = ""
# # #     for line in file_content:
# # #         print(line)
# # #
# # #         pattern = r'[d|D]og'
# # #
# # #         match = re.sub(pattern, replaced_text, line, re.I)
# # #         if match:
# # #             new_string = new_string + match +"\n"
# # #     fd.seek(0)
# # #     fd.write(new_string)
# # #     fd.truncate()
# # #     fd.close()
# # #
# # # # replace_function("/home/test/Desktop/sample.txt", 'elephant')
# # #
# # #
# # # def replace_function(file_path, replaced_text):
# # #     fd = open(file_path, 'r')
# # #     file_content = fd.readlines()
# # #     fd1 = open(file_path, 'w')
# # #
# # #     for line in file_content:
# # #         print(line)
# # #
# # #         pattern = r'[d|D]og'
# # #
# # #         match = re.sub(pattern, replaced_text, line, re.I)
# # #         if match:
# # #             print(match)
# # #             fd1.write(match)
# # #
# # #
# # # # replace_function("/home/test/Desktop/sample.txt", 'elephant')
# # #
# # #
# # # # using naive method
# # # # to combine two sorted lists
# # #
# # # def merge_sorted_list(list1, list2):
# # #     final_list = []
# # #     i, j = 0, 0
# # #     while i < len(list1) and j < len(list2):
# # #         if list1[i] < list2[j]:
# # #             final_list.append(list1[i])
# # #             i += 1
# # #         else:
# # #             final_list.append(list2[j])
# # #             j += 1
# # #     final_list = final_list + list1[i:] + list2[j:]
# # #     return final_list
# # #
# # # # print(merge_sorted_list([1,3, 6,7,8], [2,5]))
# # #
# # #
# # # # Python | Inserting item in sorted list maintaining orderPython | Inserting item in sorted list maintaining order
# # #
# # test_list = [1, 2, 3, 6,7,9]
# # k = 8
# # for i in range(len(test_list)):
# #     print(test_list[i], k)
# #     if test_list[i] > k:
# #         position = i
# #         break
# # else:
# #     position = len(test_list)
# # print(position)
# # test_list.insert(position, k)
# # print(test_list)
# # #
# # # test_list1 = [1,3,5,6,7,10]
# # # test_list2 = [2,4,8,9]
# # #
# # # i, j = 0, 0
# # # res = []
# # # while i < len(test_list1) and j < len(test_list2):
# # #     if test_list1[i] < test_list2[j]:
# # #         res.append(test_list1[i])
# # #         i += 1
# # #     else:
# # #         res.append(test_list2[j])
# # #         j = j + 1
# # # print(res + test_list1[i:] + test_list2[j:])
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# #
# #
# # # import subprocess
# # #
# # # p1 = subprocess.run(["cat", "sample.txt"], capture_output=True, text=True)
# # # # print(p1.stdout)
# # #
# # # p2 = subprocess.run(["grep", "-inr", "elephant"], stdout=subprocess.PIPE, text=True, input=p1.stdout)
# # # print(p2.stdout)
# #
# #
# # new_str = """
# # RP/0/RP0/CPU0:Arches_PE42#show ipv4 interface brief
# # Wed Aug 18 08:59:25.634 IST
# #
# # Interface                      IP-Address      Status          Protocol Vrf-Name
# # srte_c_100_ep_100.46.1.1       100.42.1.1      Down            Down     default
# # srte_c_101_ep_100.46.1.1       100.42.1.1      Down            Down     default
# # srte_c_3001_ep_100.3.1.1       100.42.1.1      Down            Down     default
# # srte_c_3002_ep_100.3.1.1       100.42.1.1      Down            Down     default
# # srte_c_3003_ep_100.3.1.1       100.42.1.1      Down            Down     default
# # BVI2341                        10.44.1.2       Up              Down     irb2341
# # BVI2342                        10.44.2.2       Up              Down     irb2342
# # BVI2343                        10.44.3.2       Up              Down     irb2343
# # BVI2344                        10.44.4.2       Up              Down     irb2344
# # BVI2345                        10.44.5.2       Up              Down     irb2345
# # BVI2346                        10.44.6.2       Up              Down     irb2346
# # BVI2347                        10.44.7.2       Up              Down     irb2347
# # BVI2348                        10.44.8.2       Up              Down     irb2348
# # BVI2349                        10.44.9.2       Up              Down     irb2349
# # BVI2350                        10.44.10.2      Up              Down     irb2350
# # BVI3001                        unassigned      Up              Up       CELL_MGMT
# # BVI3002                        42.2.1.1        Up              Up       vrf452
# # BVI3003                        42.3.1.1        Up              Up       vrf453
# # BVI3004                        42.4.1.1        Up              Up       vrf454
# # BVI3005                        42.5.1.1        Up              Up       vrf455
# # BVI3006                        42.6.1.1        Up              Up       vrf456
# # """
# # # lines = new_str.split("\n")
# # # import re
# # # for line in lines:
# # #     pattern = '(\w+)\s*(\d+\.\d+\.\d+\.\d+)\s*(Up)'
# # #     match = re.search(pattern, line)
# # #     if match:
# # #         print(match.group(1), match.group(2), match.group(3))
# #
# #
# #
# #
# # # def sample():
# # #     print("hello good morning")
# # #
# #
# # # sample()
# #
# # #* args tuple as argument... *argname, *marks
# #
# # # ** kwargs keyword args or dictionaryy
# #
# # # * **
# # def testing(name, *marks):
# #     print(type(marks))
# #     print(marks)
# #     print(name)
# #     sum =  0
# #     for mark in marks:
# #
# #         print(mark)
# #
# #
# #
# # # testing("lucky",1090,788, 10,20,30,40, 50, 60, "attt")
# #
# #
# # # keyword as argment **
# #
# # def sample(**details):
# #     print(details)
# #     print(type(details))
# #     for key,value in details.items():
# #         print(key,value)
# #
# # sample(name="kalyan", age=50, location="hyd")
# #
# #
# #
# # # valid ip program
# #
# # ip_add = "ASASS.2wewewe99.3.22"
# #
# # import re
# # p = "(\d+)\.(\d+)\.(\d+)\.(\d+)"
# # match1 = re.search(p, ip_add)
# # if match1:
# #     aa = match1.group(1)
# #     bb = match1.group(2)
# #     cc = match1.group(3)
# #     dd = match1.group(4)
# #     if int(aa) > 0 and int(aa) <= 255 and\
# #             int(bb) > 0 and int(bb) <= 255 and\
# #             int(cc) > 0 and int(cc) <= 255 and \
# #             int(dd) > 0 and int(dd) <= 255:
# #         print("valid")
# #     else:
# #         print("invalid")
# # else:
# #     print("format is wrong")
#
#
#
#
# # constructor
# # __init__ initializer
# # instance variables / class variables
# class Test:
#
#     def __init__(self):
#         print(" i am in init method")
#
#     def details(self,name, age):
#         self.name= name
#         self.age = age
#
#     def display_details(self):
#         print(self.name, self.age)
#
# # t1 = Test()
# # print(t1)
# # t1.details("name1", "20")
# # count is  5
# # count is  0
#
# class Student:
#     count = 0
#     def __init__(self, name, age, standard):
#         self.name = name
#         self.age = age
#         self.standard = standard
#     def display_details(self):
#         print("count is ", Student.count)
#
# # creating object
# # s1 = Student("name1", "age1", 34)
# #
# # s1.display_details()
# #
# # s2 = Student("name2", "age2",35)
# # s2.display_details()
#
#
# # defining class
# # creating object
# # defining init
# # defining methods
# # defining init with parameters
# # instance variables
# # class variables
# # calling the methods
# # accessing the class variables
# # difference between instance and class variables
# # single level inheritance
# # multi level inheritance
# # multiple inheritance
# # method overridding
# # super keyword
# # public and private variables
# # instance method
# # class method
# # static method
#
#
# # inheritance
#
# # single level
#
# class Testing:
#
#     def sum_of_numbers(self,a,b):
#         print("sum is {}".format(a+b))
# class Child(Testing):
#
#     def sample(self):
#         print("i am in child class")
#
# # c = Child()
# # c.sample()
# # c.sum_of_numbers(10,20)
#
# # multiple level
#
# class A:
#     def methoda(self):
#         print("i am in class A")
#
# class B(A):
#     def methodb(self):
#         print("i am in class b")
#
#
# class C(B):
#     def methodc(self):
#         print("i am in class c")
#
# # c = C()
# # c.methoda()
#
#
# #multiple choice
# # we have four choices
#
# class test1:
#     def method1(self):
#         print("method1")
#
#     def method3(self):
#         print("khan")
#
#
# class test2:
#
#     def method2(self):
#         print("method2")
#
# class test3(test1, test2):
#     def method3(self):
#         print("sal")
#
# t3 = test3()
# t3.method3()
#
#
# # overriding
#
#
#
#
#
#
#
#
#
# # instance methods
# # class methods
# # static methods
#
# # d = {
# # 	"BOSS_Services": 12,
# # 	"CloudLink Service Delivery": 12,
# # 	"MCSS": 12,
# # 	"DB_Migration": 17,
# # 	"BOSS_Address_API": 17,
# # 	"Emergency Re-Route Service": 17,
# # 	"BOSS_EmergencyRegistration": 17,
# # 	"LIS": 17
# # }
#
# # import json
# # fd = open("config.txt", "w")
# # json.dump(d, fd)
# # fd.close()
# #
# # fd1 = open("config.txt", "r")
# # data = json.load(fd1)
# # print(data)
#
#
#
# class Parent:
#
#     def method1(self):
#         print("i am in method1")
#
# class Child(Parent):
#     def method1(self):
#         print("i am in child")
#         super().method1()
#
# c = Child()
# c.method1()

# __varaible __name
# class test1:
#     def method1(self, name):
#         self.__name = name
#
#     def display(self):
#         print(self.name)
#
# #_classname__variablename
# #_classname -- _test1__name
# t = test1()
# t.method1("junk")
# # t.display()
# print(t._test1__name)
# #mangling  _classname


# # objectname._classname__variablename
# print(t._test1__name)

#
# class Student:
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.count += 1 # Student.count = Student.count + 1
#
#     def display(self):
#         print(self.name, self.age)
#
#     @classmethod
#     def test_class(cls):
#         print(Student.count)
#
#     @staticmethod
#     def other_method(age):
#         print(age)
#
# Student.test_class()
# s1 = Student("sam",30)
# s1.display()
# Student.test_class()
#
# # s2 = Student("nag",60)
# # s2.display()
#
import json
# file_name = "sample.json"
# fd1 = open("sample.json", "r")
# content = json.load(fd1)
# print(content)
# print(type(content))
# print(content["data"])

s = """
{
    "data": [
        {
            "feature_name": "DB_Migration",
            "severity": "Low",
            "percentage": 0.57,
            "line_changes": 14,
            "jira_changes": 0,
            "sales_change": 0
        },
        {
            "feature_name": "UX",
            "severity": "Low",
            "percentage": 0.25,
            "line_changes": 0,
            "jira_changes": 2,
            "sales_change": 0
        }
    ]
}
"""
# content = json.loads(s)
# for element in content["data"]:
#     for key,val in element.items():
#         if key == "feature_name":
#             print(key,":",val)




# os -operating system

# import os
# print(os.getcwd())
# os.chdir("c:\\Users\\pathapaa")
# output = os.listdir(".")
# print(output)
# for var in output:
#     if os.path.isdir(var):
#         print(var)
# #     if os.path.exists("c:\\Users\pathapaa\\folder1\\folder2\\folder3\\sample.txt"):
#
#
#
# data = {
#     "name":"test1",
#     "loc":"bng"
#
# }
#
# """
# {
#     "name":"test1",
#     "loc":"bng"
#
# }
# """
#
#
# fd = open("test.json", "w")
#
# json.dump(data,fd, indent=4)
# fd.close()











def sample(a,b):
    return a,b

c,d = sample(10,20)
print(c,d)

import sys
from scipy.signal import butter, filtfilt
from scipy.signal import blackmanharris, fftconvolve
from scipy.signal import butter, filtfilt
from scipy import signal
from numpy.fft import rfft
import soundfile as sf
from numpy import argmax, mean, diff, log
import parabolic
import numpy
class Testing:
    def butter_highpass(self, cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='high', analog=False)
        return b, a

    # Shankara Narayanan. M 21-06-2019
    def butter_lowpass(self, cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='lowpass', analog=False)
        return b, a

    def butter_lowpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.butter_lowpass(cutoff, fs, order=order)
        y = filtfilt(b, a, data)
        return y

    def butter_highpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.butter_highpass(cutoff, fs, order=order)
        y = filtfilt(b, a, data)
        return y

    def estimate_energy(self, raw_audio_file):
        try:
            cutoff = 0
            order = 2
            fs = 16000
            cutoff = 250

            print('Reading file "%s"\n' % raw_audio_file)
            raw_audio, fs = sf.read(raw_audio_file, format='RAW', samplerate=fs, channels=1, subtype='PCM_16')
            raw_audio_filt = self.butter_highpass_filter(raw_audio, cutoff, fs, order)

            f, p = signal.periodogram(raw_audio_filt, fs)
            signal_energy = numpy.mean(p)
            print("Energy: %s" % signal_energy)
            energy = 0
            for i in range(0, len(raw_audio_filt)):
                sampleVal = (raw_audio_filt[i] - 128) * 256.0
                energy += sampleVal * sampleVal
            print(energy)

            return signal_energy

        except Exception as err:
            fn = sys._getframe().f_code.co_name
            raise Exception("func '%s' - err: '%s'!" % (fn, err))

    def parabolic(self,f, x):
        """Quadratic interpolation for estimating the true position of an
        inter-sample maximum when nearby samples are known.

        f is a vector and x is an index for that vector.

        Returns (vx, vy), the coordinates of the vertex of a parabola that goes
        through point x and its two neighbors.

        Example:
        Defining a vector f with a local maximum at index 3 (= 6), find local
        maximum if points 2, 3, and 4 actually defined a parabola.

        In [3]: f = [2, 3, 1, 6, 4, 2, 3, 1]

        In [4]: parabolic(f, argmax(f))
        Out[4]: (3.2142857142857144, 6.1607142857142856)

        """
        xv = 1 / 2. * (f[x - 1] - f[x + 1]) / (f[x - 1] - 2 * f[x] + f[x + 1]) + x
        yv = f[x] - 1 / 4. * (f[x - 1] - f[x + 1]) * (xv - x)
        return (xv, yv)

    def freq_from_fft(self, sig, fs):
        """
        Estimate frequency from peak of FFT
        """
        # Compute Fourier transform of windowed signal
        try:
            windowed = sig * blackmanharris(len(sig))
            import pdb
            # pdb.set_trace()
            f = rfft(windowed)

            # Find the peak and interpolate to get a more accurate peak
            i = argmax(abs(f))  # Just use this for less-accurate, naive version
            if i ==0:
                return 0
            true_i = self.parabolic(log(abs(f)), i)[0]

            # Convert to equivalent frequency
            return fs * true_i / len(windowed)
        except:
            print('freq_from_fft :' + str(sys.exc_info()[0]))
            return 0
        
    def estimate_frequency_moh(self, file, audiopath):
        import time
        try:
            cutoff = 0
            order = 2
            fs = 16000
            audiopath = audiopath.lower()
            raw_audio, fs = sf.read(file, format='RAW', samplerate=fs, channels=1, subtype='PCM_16')
            print('Calculating frequency from FFT:')
            start_time = time.time()
            freq3 = self.freq_from_fft(raw_audio, fs)
            print('%f Hz' % freq3)
            print('Time elapsed: %.3f s\n' % (time.time() - start_time))
            print(freq3)
            return freq3
        except Exception as err:
            fn = sys._getframe().f_code.co_name
            raise Exception("func '%s' - err: '%s'!" % (fn, err))


t = Testing()
print(t.estimate_frequency_moh("Tone6.wav", "jj"))

# from scipy.io import wavfile
#
# def freq(file, start_time, end_time):
#     sample_rate, data = wavfile.read(file)
#     start_point = int(sample_rate * start_time / 1000)
#     end_point = int(sample_rate * end_time / 1000)
#     length = (end_time - start_time) / 1000
#     counter = 0
#     for i in range(start_point, end_point):
#         if data[i] < 0 and data[i+1] > 0:
#             counter += 1
#     return counter/length
#
# print(freq("MOH_200Hz_HF.wav", 1000 ,2100))
# 1231.8181818181818
# #
# import sys
# from aubio import source, pitch
#
# import numpy as np
# win_s = 4096
# hop_s = 512
#
# s = source("Tone6.wav", 8800, hop_s)
# samplerate = s.samplerate
#
# tolerance = 0.8
#
# pitch_o = pitch("yin", win_s, hop_s, samplerate)
# pitch_o.set_unit("midi")
# pitch_o.set_tolerance(tolerance)
#
# pitches = []
# confidences = []
#
# total_frames = 0
# while True:
#     samples, read = s()
#     pitch = pitch_o(samples)[0]
#     pitches += [pitch]
#     confidence = pitch_o.get_confidence()
#     confidences += [confidence]
#     total_frames += read
#     if read < hop_s: break
#
# print("Average frequency = " + str(np.array(pitches).mean()) + " hz")
#
# import os
# import requests
# import sys
#
# def test_create_dir():
#     if not os.path.exists("some"):
#         os.mkdir("some")
