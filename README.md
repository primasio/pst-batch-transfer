# pst_transfer
批量向多个账户进行转账操作

## 查看tx
```
https://ropsten.etherscan.io/
```

## 配置
```
passwd #账户密码，用来解锁账户
token_contract_address #token合约地址
account_address #账户地址
eth_rpc #以太坊rpc
TOKEN_ABI #token abi
csv_file #需要转账的数据文件
```

## 执行
```
配置好配置文件之后
执行python main.py 会显示转账过程以及tx
```

## 具体显示结果
```
isConnected: True
unlockAccount:  True
transfer: 0x04d8692cb9f998d3cff6ebd8fd0ec8531be9e5e0 10 0x234a5c4541f6bd09d15f9c0d64280712715de4d078a97a014f417f2b145dc564
transfer: 0x05e995ec955a3d33bd47ef9b975c7965b52ffce7 10 0x5162e40f627e0224f644420665dcf2ad0cfbf712082de38a13239886724b3a20
transfer: 0x0fc34436261e2d4d3e53765be7ab126f94d5c838 10 0xc1f39f21a3f34472dcc06441e5bcc3e91c0896805153aeedcc6852d6c3db3b95
transfer: 0x10f1de67d86a8dbf9eb381845e630b8c89949f1e 10 0xe0398a23f1fbd2ecf589dc88a5524575730487f5c1b2a34bdf2b256806186544
transfer: 0x13f3c1e0195ed7ca8b953f4494cc3e86d1c4e5a0 10 0x7eeba26dd1f5ca0ff04b18673858ad2fc1db5709cda05f2f43d1bed5682d1946
transfer: 0x1a88503ea0cebfecf06e9f70f0db0c171ee3ddfd 10 0x87a33158884b50b0dc066f21b3c9809b666544b85a8d35cff83fa039fd45217a
transfer: 0x1b8d70fee3df5b0c681c380f08da700c1f3f6b03 10 0x14650bfb667ac16d2abea11ad385398ab0912c4d93fdb9b1a921caa8898a04a6
transfer: 0x200ff3f6a443ae5c730ce6d76ac421d8dabec081 10 0x49215a5c9d7b46ddec596ddc5a983eabb4cd1343682303bec231eb834fd9ce6b


 [
  {
    "account_address": "0x04d8692cb9f998d3cff6ebd8fd0ec8531be9e5e0",
    "tx": "0x234a5c4541f6bd09d15f9c0d64280712715de4d078a97a014f417f2b145dc564"
  },
  {
    "account_address": "0x05e995ec955a3d33bd47ef9b975c7965b52ffce7",
    "tx": "0x5162e40f627e0224f644420665dcf2ad0cfbf712082de38a13239886724b3a20"
  },
  {
    "account_address": "0x0fc34436261e2d4d3e53765be7ab126f94d5c838",
    "tx": "0xc1f39f21a3f34472dcc06441e5bcc3e91c0896805153aeedcc6852d6c3db3b95"
  },
  {
    "account_address": "0x10f1de67d86a8dbf9eb381845e630b8c89949f1e",
    "tx": "0xe0398a23f1fbd2ecf589dc88a5524575730487f5c1b2a34bdf2b256806186544"
  },
  {
    "account_address": "0x13f3c1e0195ed7ca8b953f4494cc3e86d1c4e5a0",
    "tx": "0x7eeba26dd1f5ca0ff04b18673858ad2fc1db5709cda05f2f43d1bed5682d1946"
  },
  {
    "account_address": "0x1a88503ea0cebfecf06e9f70f0db0c171ee3ddfd",
    "tx": "0x87a33158884b50b0dc066f21b3c9809b666544b85a8d35cff83fa039fd45217a"
  },
  {
    "account_address": "0x1b8d70fee3df5b0c681c380f08da700c1f3f6b03",
    "tx": "0x14650bfb667ac16d2abea11ad385398ab0912c4d93fdb9b1a921caa8898a04a6"
  },
  {
    "account_address": "0x200ff3f6a443ae5c730ce6d76ac421d8dabec081",
    "tx": "0x49215a5c9d7b46ddec596ddc5a983eabb4cd1343682303bec231eb834fd9ce6b"
  }
]
```