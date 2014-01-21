from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    cachecoin=math.Object(
        PARENT=networks.nets['cachecoin'],
        SHARE_PERIOD=120, # seconds
        CHAIN_LENGTH=12*60*60//120, # shares
        REAL_CHAIN_LENGTH=12*60*60//120, # shares
        TARGET_LOOKBEHIND=30, # shares
        SPREAD=30, # blocks
        IDENTIFIER='Q28kFRCjXjMYBfJy'.decode('hex'),
        PREFIX='wVWQvM438v6L2mZr'.decode('hex'),
        P2P_PORT=2225,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8336,
        BOOTSTRAP_ADDRS='rav3n.dtdns.net 37.59.119.242 95.138.185.176 213.239.207.114 81.17.30.121 46.163.105.201 88.190.223.101'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
