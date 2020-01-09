from core.config.globalimport import *
from core.servers.dns.DNSBase import DNSBase
from core.packets.dnsserver import  DNSServerThread

class PyDNSServer(DNSBase):
    ID = "pydns_server"
    Name = "PyDNS Server"
    Author = 'Samuel Colvin @samuelcolvin'
    ExecutableFile = ""

    def __init__(self,parent):
        super(PyDNSServer,self).__init__(parent)
        

    @property
    def commandargs(self):
        pass

    def LogOutput(self, data):
        pass
        #TODO: add system logger controller 
        #print(data)
        #self.logger.info(data)

    def boot(self):
        self.reactor = DNSServerThread(self.conf)
        self.reactor.sendRequests.connect(self.LogOutput)
        self.reactor.setObjectName(self.Name)  # use dns2proxy as DNS server