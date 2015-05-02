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
        IDENTIFIER='5305F45FAFF3FF77'.decode('hex'),
        PREFIX='32A2273E3F35F31E'.decode('hex'),
        P2P_PORT=2226,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8336,
        BOOTSTRAP_ADDRS='mehrangarh.cach.co windsor.cach.co malbork.cach.co p2cache.syware.de cach.happymining.de 207.30.158.106 46.101.173.108'.split(' '),
        ANNOUNCE_CHANNEL='#cachecoin-bots',
        VERSION_CHECK=lambda v: True,
    ),
    cachecoin_testnet=math.Object(
        PARENT=networks.nets['cachecoin_testnet'],
        SHARE_PERIOD=120, # seconds
        CHAIN_LENGTH=12*60*60//120, # shares
        REAL_CHAIN_LENGTH=12*60*60//120, # shares
        TARGET_LOOKBEHIND=30, # shares
        SPREAD=30, # blocks
        IDENTIFIER='3E20367C2B6B2D7A'.decode('hex'),
        PREFIX='2E6D623E57384E26'.decode('hex'),
        P2P_PORT=12226,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=18336,
        BOOTSTRAP_ADDRS='mehrangarh.cach.co windsor.cach.co malbork.cach.co p2cache.syware.de cach.happymining.de 207.30.158.106 46.101.173.108'.split(' '),
        ANNOUNCE_CHANNEL='#cachecoin-bots',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
