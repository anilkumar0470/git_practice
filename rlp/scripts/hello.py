import pexpect.popen_spawn
import time
import yaml
import os
import sys

class Login_function:
    connect_device_list = []
    connection_device_info = {}
    with open("D:\\fnc\python\\git_practice\\rlp\\testbed.yaml","r") as stream:
        yaml_out = yaml.safe_load(stream)


    def connect(self,device,prompt=None):
        out = pexpect.popen_spawn.PopenSpawn("telnet {} {}".format(device["connections"]["ip"],device["connections"]["port"], timeout=120))
        import pdb
        pdb.set_trace()
        out.sendline("\r")
        out.sendline("\r")

        time.sleep(2)
        count =8
        while count == 8:
            import pdb
            pdb.set_trace()
            i = out.expect(["Username","Password",">","config","#","refused"])
            if i == 0 :
                print ("value is  {}".format(i))
                out.sendline(device["credentials"]["username"])
                continue
            if i == 1 :
                print("value is  {}".format(i))
                out.sendline(device["credentials"]["password"])
                continue
            if i==2 :
                print("value is  {}".format(i))
                #pytest.set_trace()
                out.sendline("enable")

                if not out.expect("word"):
                #     pass
                    print(device["credentials"]["enable_password"])
                    out.sendline(device["credentials"]["enable_password"])
                if prompt:
                    Login_function.connection_device_info.update({device["alias"]: out})
                    print(Login_function.connection_device_info)
                    print("junk")
                    return out
                continue
            if i == 4 :
                # if prompt:
                #     out.sendline("exit")
                #     return out
                print("value is  {}".format(i))
                print("Device is in privil mode")
                #Login_function.connect_device_list.append(device["alias"])
                # import pdb
                # pdb.set_trace()
                Login_function.connection_device_info.update({device["alias"]:out})
                print (Login_function.connection_device_info)
                out.sendline("terminal length 0")
                out.expect("#")
                break
            if i == 3:
                if prompt:
                    out.sendline("exit")
                    return out
                print("value is  {}".format(i))
                Login_function.connection_device_info.update({device["alias"]: out})
                print(Login_function.connection_device_info)
                return out
            if i ==5 :
                child = pexpect.spawn('telnet {}'.format(device["connections"]["ip"]))

                count = 10
                while count > 0:
                    count -= 1
                    index = child.expect(['Username:', 'Password:', '#', '>'])
                    if index == 1:
                        child.sendline(device["connections"]["terminal_server_password"])
                        break
                    elif index == 0:
                        child.sendline(device["connections"]["terminal_server_username"])
                    else:
                        child.sendline("\n")
                        break

                index = child.expect(['#', '>'])
                if index == 1:
                    child.sendline("enable")
                    child.expect('Password:')
                    child.sendline(device["connections"]["terminal_server_enable_password"])
                    child.expect('#')

                line_number = str(device["connections"]['port'])[2:]

                child.sendline("clear line {}".format(line_number))
                child.expect('[confirm]')
                child.sendline('\r')
                child.expect('#')
                child.sendline('exit')

                self.log.debug("device_disconnect - completed")
                self.connect(device,prompt=prompt)


    def config_exec(self,dev_obj,command_to_send):
        #pytest.set_trace()
        if dev_obj["alias"] not in Login_function.connection_device_info:
            self.connect(dev_obj)
            connection_info = Login_function.connection_device_info[dev_obj["alias"]]
        else:
            connection_info = Login_function.connection_device_info[dev_obj["alias"]]

        connection_info.sendline("configure terminal")
        command_list = command_to_send.split("\n")

        for commnad in command_list:
            print(commnad)
            connection_info.sendline(commnad.strip())
        print ("All commands configured sucessfully!!")

    def privil_exec(self, dev_obj, command_to_send,prompt="show"):
        #self.connect(dev_obj,prompt="show")
        if dev_obj["alias"] not in Login_function.connection_device_info:
            self.connect(dev_obj)
            connection_info1 = Login_function.connection_device_info[dev_obj["alias"]]
        else:
            connection_info1 = Login_function.connection_device_info[dev_obj["alias"]]

        #print(connection_info1)
        for i in range(10):
            connection_info1.sendline(command_to_send+"\r")
            kkk = connection_info1.expect([">", "config", "#"])

            if kkk ==1:
                connection_info1.sendline("exit")
            print(kkk)
            time.sleep(2)
            output = connection_info1.before
            print(output)
            flag = False
            if len(output) > 100:
                flag = True
                break
        if flag:
            return output


# print(Login_function.is_connect)
# l = Login_function()
# l.connect("172.19.198.127", "2034")
# print(Login_function.is_connect)


#
#
# import getpass
# import sys
# import telnetlib
#
# HOST = "127.0.0.1 5006"
#
# import pdb
# pdb.set_trace()
# tn = telnetlib.Telnet(host="localhost",port=5006)
#
# import pdb
# pdb.set_trace()
# tn.read_until("#")
# user = "apathapa"
# password = "apathapa"
#
# if password:
#     tn.write("terminal length 0" + "\r\n")
#     tn.write("show version" + "\r\n")
# print(tn.read_all())
