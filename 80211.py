	#!/usr/bin/python

"""
Setting the position of Nodes (only for Stations and Access Points)
and providing mobility using mobility models with wmediumd enabled."""

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mininet.wifi.node import OVSKernelAP, UserAP
from mininet.wifi.link import wmediumd
from mininet.wifi.cli import CLI_wifi
from mininet.wifi.net import Mininet_wifi
from sys import argv
#from mininet.net import start as ethStart


def topology():

    "Create a network."
    if int(argv[4]):
        net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP, link=wmediumd)#, enable_interference=True, noise_threshold=-91, fading_coefficient=1)
    else:
        net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP)#, enable_interference=True, noise_threshold=-91, fading_coefficient=1)
    info("*** Creating nodes\n")
    print "Config AP"
    ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode=str(argv[1]), channel=str(argv[2]), band=float(argv[3]),
                             position='150,150,0', ip="10.0.1.1/8")#, #[HT40+][HT40-][SHORT-GI-40][DSSS_CCK-40][GF]
                             #ht_capab="[SHORT-GI-20][HT40+][HT40-][SHORT-GI-40][DSSS_CCK-40][GF]") #), #config="preamble=1")#,ieee80211n=1")#, ht_capab="[HT40][SHORT-GI-40]")
    #ap2 = net.addAccessPoint('ap2', ssid='new-ssid-2', mode='ac', channel=str(argv[1]), position='1500,150,0')
    #ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='n', channel='11',
    #                         position='150,150,0')
    print "Config STA1"
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', position='150,149,0', min_x=100, max_x=200, min_y=100, max_y=200, min_v=5, max_v=10)
    #sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', min_x=100, max_x=200, min_y=100, max_y=200, min_v=5, max_v=10)
    print "Config STA2"
    #sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', position='150, 151,0', min_x=100, max_x=200, min_y=100, max_y=200, min_v=5, max_v=10)

    #sta3 = net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8', position='150, 152,0', min_x=100, max_x=200, min_y=100, max_y=200, min_v=5, max_v=10)
    #sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', min_x=100, max_x=200, min_y=100, max_y=200, min_v=5, max_v=10)
    print "Config C1"
    c1 = net.addController('c1', controller=Controller)

    h1 = net.addHost('h1', ip='10.0.0.5/8', position='150,148,0', mac='00:00:00:00:00:05')
    #h2 = net.addHost('h2', ip='10.0.0.6/8', position='150,147,0', mac='00:00:00:00:00:06')

    info("*** Configuring Propagation Model\n")
    net.propagationModel(model="logDistance", exp=3)
    #net.propagationModel(model="young")

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    # Link 100mbps
    net.addLink(ap1, h1)#, link=True, bw=100, delay='5ms', loss=0, max_queue_size=1000, use_htb=True)
    #net.addLink(ap1, h2)#, link=True, bw=100, delay='5ms', loss=0, max_queue_size=1000, use_htb=True)

    #net.plotGraph(max_x=300, max_y=300)

    net.seed(20)

    h1.cmd("python -m SimpleHTTPServer 80 > /tmp/http.log &")
    h1.cmd("iperf --u -s -D")
    #h2.cmd("python -m SimpleHTTPServer 80 > /tmp/http.log &")
    sta1.cmd("python -m SimpleHTTPServer 80 > /tmp/http.log &")

    if True:
        net.startMobility(time=0, repetitions=1)
        net.mobility(sta1, 'start', time=2, position='150,151,0')
        #net.mobility(sta2, 'start', time=2, position='150, 140,0')
        net.mobility(sta1, 'stop', time=120, position='150,152,0')
        #net.mobility(sta2, 'stop', time=22)
        net.stopMobility(time=120)

    #Disabled mobility
    #net.startMobility(time=3, model='RandomDirection', max_x=200, max_y=200)

    info("*** Starting network\n")
    #ethStart()
    net.build()
    c1.start()
    ap1.start([c1])
    #ap2.start([c1])

    #net.startTerms()

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
