from __future__ import unicode_literals

from web3 import Web3, HTTPProvider

import config

web3 = Web3(HTTPProvider(config.eth_rpc))
web3.eth.defaultAccount = config.account_address

from web3 import personal as wp

p = wp.Personal(web3)
print("isConnected:", web3.isConnected())
print("unlockAccount: ", p.unlockAccount(web3.eth.defaultAccount, config.passwd))  # ropsten

token_Contract = web3.eth.contract(
    abi=config.TOKEN_ABI
)

t_contract = token_Contract(address=config.token_contract_address)


def transfer_pst(rows):
    for row in rows:
        p.unlockAccount(web3.eth.defaultAccount, config.passwd, duration=hex(100))
        t = t_contract.transact().transfer(row["address"], int(row["value"]) * 10 ** 18)
        print("transfer:", row["address"], row["value"], t)
        yield {
            "account_address": row["address"],
            "tx": t
        }
