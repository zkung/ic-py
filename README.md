## Python Agent Library for the Internet Computer

`ic-py` provides basic modules to interact with canisters on the DFINITY Internet Computer. Its still under active development.

### Install

```
pip3 install ic-py
```

### Status

1. candid: candid encode & decode  [Done]
2. principal: principal class [Done]
3. identity: secp256k1 & ed25519 identity [Done]
4. client: http client [Done]
5. agent: ic agent to communicate with canisters on ic [Done]
6. canister: canister class, initialized with canister id and did file [Done]
7. common canister interfaces: ledger, management, nns, cycles wallet [WIP]
8. automated testing [WIP]

### Modules & Usage

#### 1. Principal

Create an instance:

```python
from ic.principal import Principal
p = Principal() # default is management canister id `aaaaa-aa`
p1 = Principal(bytes=b'') # create an instance from bytes
p2 = Principal.anonymous() # create anonymous principal
p3 = Principal.self_authenticating(pubkey) # create a principal from public key
p4 = Principal.from_str('aaaaa-aa') # create an instance from string
p5 = Principal.from_hex('xxx') # create an instance from hex
```

Class methods:

```python
p.bytes # principal bytes
p.len # byte array length
p.to_str() # convert to string
```

#### 2. Identity

Create an instance:

```python
from ic.identity import Identity
i = Identity() # create an identity instance, key is randomly generated
i1 = Identity(privkey = "833fe62409237b9d62ec77587520911e9a759cec1d19755b7da901b96dca3d42") # create an instance from private key
```

Sign a message:

```python
msg = b”ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f“
sig = i.sign(msg) # sig = (der_encoded_pubkey, signature)
```

#### 3. Client

Create an instance:

```python
from ic.client import Client
client = Client(url = "https://ic0.app")
```

#### 4. Candid

Encode parameters:

```python
from ic.candid import encode, decode, Types
# params is an array, return value is encoded bytes
params = [{'type': Types.Nat, 'value': 10}]
data = encode(params)
```

Decode parameters:

```python
# data is bytes, return value is an parameter array
params = decode(data)
```

#### 5. Agent

Create an instance:

```python
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
# Identity and Client are dependencies of Agent
iden = Identity()
client = Client()
agent = Agent(iden, client)
```

Query call:

```python
# query the name of token canister `gvbup-jyaaa-aaaah-qcdwa-cai`
name = agent.query_raw("gvbup-jyaaa-aaaah-qcdwa-cai", "name", encode([]))
```

Update call:

```python
# transfer 100 token to blackhole address `aaaaa-aa`
params = [
	{'type': Types.Principal, 'value': 'aaaaa-aa'},
	{'type': Types.Nat, 'value': 10000000000}
]
result = agent.update_raw("gvbup-jyaaa-aaaah-qcdwa-cai", "transfer", encode(params))
```

#### 6. Canister

Create an instance:

```python
from ic.canister import Canister
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
# Identity and Client are dependencies of Agent
iden = Identity(privkey="833fe62409237b9d62ec77587520911e9a759cec1d19755b7da901b96dca3d42")
client = Client()
agent = Agent(iden, client)
```

Query call:

```python
# query the name of token canister `gvbup-jyaaa-aaaah-qcdwa-cai`
canister = Canister(agent, "gvbup-jyaaa-aaaah-qcdwa-cai")
# canister = Canister(agent, "gvbup-jyaaa-aaaah-qcdwa-cai", candid=candidContext)
name = canister.name()
```

Update call:

```python
# transfer 100 token to blackhole address `aaaaa-aa`
canister = Canister(agent, "gvbup-jyaaa-aaaah-qcdwa-cai")
result = canister.transfer('aaaaa-aa', int(100*1E8))
```


#### 7. Interfaces

Create an instance:

```python
from ic.interfaces import Interfaces
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.principal import Principal
import time
# Identity and Client are dependencies of Agent
iden = Identity.from_pem(You_pem)
client = Client()
agent = Agent(iden, client)
interfaces = Interfaces(agent)
```

Query call:

```python
# Query account balance from 449ce7ad1298e2ed2781ed379aba25efc2748d14c60ede190ad7621724b9e8b2
data = {'account': '449ce7ad1298e2ed2781ed379aba25efc2748d14c60ede190ad7621724b9e8b2'}
interfaces = Interfaces(agent)
result = interfaces.ledger.account_balance_dfx(data)
```

Update call:

```python
# send 0.0001 ICP to account `449ce7ad1298e2ed2781ed379aba25efc2748d14c60ede190ad7621724b9e8b2`
toAddress ='449ce7ad1298e2ed2781ed379aba25efc2748d14c60ede190ad7621724b9e8b2'
data = {
        'to': toAddress,
        'fee': {'e8s':int(0.0001E8)},
        'memo': 0,
        'from_subaccount':[],
        'created_at_time':[{'timestamp_nanos':time.time_ns()}],
        'amount': {'e8s':int(0.0001E8)},
}
interfaces = Interfaces(agent)
result = interfaces.ledger.send_dfx(data)
```
