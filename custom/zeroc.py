from six.moves import input  
from zeroconf import ServiceBrowser, Zeroconf

class MyListener(object):  
    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print name, info
        # print name, info.get_name(), info.server,

zeroconf = Zeroconf()  
listener = MyListener()  
browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)  
try:  
    input("Press enter to exit...\n\n")
finally:  
    zeroconf.close()