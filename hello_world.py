from dwave.cloud import Client

client = Client.from_config(token='XXXXXXXXXXXXXXXXXXXXXX')
print(client.get_solvers())
