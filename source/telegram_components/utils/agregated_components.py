def collect_variants_from_nodes(key_name: str, nodes):
    return {node[key_name]: node.id for node in nodes}
