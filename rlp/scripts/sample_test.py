from hello import Login_function
import yaml
import pdb
import logging


class Sample(Login_function):
    def test_one(self):
        connection_obj = {}
        logging.basicConfig(level=logging.DEBUG)
        self.log = logging.getLogger(__name__)
        with open ("D:\\fnc\python\\git_practice\\rlp\\testbed.yaml","r") as stream:
            yaml_out = yaml.safe_load(stream)
        #self.log.debug(yaml_out)
        device_list = ["Switch1","Switch2"]
        for device in device_list:

            dev_obj = yaml_out["devices"][device]
            self.config_exec(dev_obj,"default interface gig1/1/1")
            self.config_exec(dev_obj,"default interface gig1/1/2")
            self.config_exec(dev_obj,"interface gig1/1/2 \n no switchport \n ip address 10.6.246.131 255.255.255.0 \n "
                                                "no shutdown \n exit")
            self.config_exec(dev_obj, "interface gig1/1/1 \n no switchport \n ip address 11.6.246.131 255.255.255.0 \n "
                                  "no shutdown \n exit")
            # out = self.privil_exec(dev_obj,"show ip int br")
            # print (out)


s = Sample()
s.test_one()