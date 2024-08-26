import os
import dotenv
from py2neo import Graph

def drive():
    # load_status = dotenv.load_dotenv("Neo4j-1ae5a366-Created-2024-08-21.txt")
    # if load_status is False:
    #     raise RuntimeError('Environment variables not loaded.')

    # URI = os.getenv("NEO4J_URI")
    # AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
    
    URI = 'neo4j+s://1ae5a366.databases.neo4j.io'
    Auth = ('neo4j', 'yEIj4BBgp1XUpg4lhct1_Cx2E9o2mXJICkATI0wJ-BE')
    
    graph = Graph(URI, auth=Auth)
    return graph
