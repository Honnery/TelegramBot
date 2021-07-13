from settings import database_config
from .node import Node
from neo4j import GraphDatabase


class GraphApi:
    def __init__(self, url, user, password):
        self._driver = GraphDatabase.driver(url, auth=(user, password))

    def find_nodes_by_label(self, label):
        command = f"""
                  Match (a:{label})-[SHOW_THEN]->(b)
                  Return b
                  """

        result = self._execute_command(command, return_result=True)
        return [Node(rec[0]) for rec in result]

    def find_nodes_by_id(self, node_ind):
        command = f"""
                  Match (a)-[r:SHOW_THEN]->(b)
                  Where id(a)={node_ind} 
                  Return b
                  """
        result = self._execute_command(command, return_result=True)
        return self._extract_nodes(result)

    def search_post_process(self, node_ind=None):
        command = f"""
                  Match (a)-[r:PROCESS_AS]->(b)
                  Where id(a)={node_ind} 
                  Return b"""

        result = self._execute_command(command, return_result=True)
        return self._extract_nodes(result)

    def match_current_node(self, node_ind=None):
        command = f"""
                  Match (n)
                  Where id(n)={node_ind} 
                  Return n"""

        result = self._execute_command(command, return_result=True)
        return self._extract_nodes(result)

    def _execute_command(self, command, return_result=False):
        with self._driver.session() as session:
            result = session.run(command)

            if return_result:
                return result.values()

    @staticmethod
    def _extract_nodes(result):
        return [Node(rec[0]) for rec in result]


graph_api = GraphApi(
    database_config.get("DATABASE_INFO", "url"),
    database_config.get("DATABASE_INFO", "name"),
    database_config.get("DATABASE_INFO", "password"))
