from ic.interfaces import Interfaces
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent

iden = Identity()
client = Client()
agent = Agent(iden, client)

interfaces = Interfaces(agent)

result = interfaces.cycles_minting.get_icp_xdr_conversion_rate()
print(result)