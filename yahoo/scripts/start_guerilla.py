#!/usr/bin/env python

from plumbum import cli, local, FG, BG
import socket



class StartGuerillaCLI(cli.Application):



    start_master = cli.Flag("-m", default = False, help = "If present, starts the guerilla master")
    start_worker = cli.Flag("-w", default = False, help = "If present, starts a guerilla worker")
    start_redis = cli.Flag("-r", default = False, help = "If present, starts a redis server for guerilla")
    hostname = socket.gethostname()



    def main(self):
        #hostName = cli.SwitchAttr("-hostName", str, default = local.env["HOSTNAME"] )
        print self.start_master, self.start_worker, self.start_redis
        print self.hostname   #hostname is not available in local due to portability issue with hostname
        sgi = StartGuerillaInternal(self.start_master, self.start_worker, self.start_redis, self.hostname)
        sgi.start()


#class StartGuerillaFromENV(cli.Application):



class StartGuerillaInternal():

        def __init__(self, start_master, start_worker, start_redis, hostname):
            self.start_master = start_master
            self.start_worker = start_worker
            self.start_redis  = start_redis
            self.hostname = hostname

        def start(self):
            #TODO:bruceg refresh guerilla and do npm install. Out of scope for now
            if self.start_master:
                #ideally we could run as a background process, but per https://github.com/tomerfiliba/plumbum/issues/48
                #  there are complications re the std io buffers.
                with local.cwd(local.cwd): #assumes we are running in scripts, mabye have install dir env variable?
                    startRedisServerCommand = local.["start-redis-server.command"]
                    startRedisServerCommand()


          

if __name__ == "__main__":
    StartGuerillaCLI.run()