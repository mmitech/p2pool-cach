import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack
from operator import *

def get_subsidy(nCap, nMaxSubsidy, bnTarget):
    bnLowerBound = 0.01
    bnUpperBound = bnSubsidyLimit = nMaxSubsidy
    bnTargetLimit = 0x00000fffff000000000000000000000000000000000000000000000000000000

    while bnLowerBound + 0.01 <= bnUpperBound:
        bnMidValue = (bnLowerBound + bnUpperBound) / 2
        if pow(bnMidValue, nCap) * bnTargetLimit > pow(bnSubsidyLimit, nCap) * bnTarget:
            bnUpperBound = bnMidValue
        else:
            bnLowerBound = bnMidValue

    nSubsidy = round(bnMidValue, 2)

    if nSubsidy > bnMidValue:
        nSubsidy = nSubsidy - 0.01

    return int(nSubsidy * 1000000)

def debug_block_info(dat1):
	print 'block header',  data.block_header_type.unpack(dat1)['timestamp']
	return 0

nets = dict(
    cachecoin=math.Object(
        P2P_PREFIX='d9e6e7e5'.decode('hex'),
        P2P_PORT=2225,
        ADDRESS_VERSION=28,
        RPC_PORT=2224,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'cachecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda target: get_subsidy(6, 100, target),
        BLOCKHASH_FUNC=lambda header: pack.IntType(256).unpack(__import__('yac_scrypt').getPoWHash(header, data.block_header_type.unpack(header)['timestamp'])),
        POW_FUNC=lambda header: pack.IntType(256).unpack(__import__('yac_scrypt').getPoWHash(header, data.block_header_type.unpack(header)['timestamp'])),
        BLOCK_PERIOD=900, # s
        SYMBOL='CACH',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'cachecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/cachecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.cachecoin'), 'cachecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://www.chainbrowser.com/cachecoin/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://www.chainbrowser.com/cachecoin/address/',
        SANE_TARGET_RANGE=(2**256//2**20//1000 - 1, 2**256//2**20 - 1),
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
