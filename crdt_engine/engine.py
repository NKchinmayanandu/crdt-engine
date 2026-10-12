from typing import List, Dict, Any

def insert_node(nodes: List[Dict[str, Any]], new_node: Dict[str, Any]) -> List[Dict[str, Any]]:

    left_origin_id = new_node.get("left_origin_id")
    new_id = new_node.get("element_id")
    
    parent_index = 0
    if left_origin_id and left_origin_id != "ROOT":
        for i, node in enumerate(nodes):
            if node.get("element_id") == left_origin_id:
                parent_index = i
                break

    insert_index = parent_index + 1
    
    while insert_index < len(nodes):
        current_node = nodes[insert_index]
        current_left_origin = current_node.get("left_origin_id")
        
        if current_left_origin == left_origin_id:
            if new_id < current_node.get("element_id"):
                break  
            else:
                insert_index = _skip_subtree(nodes, insert_index)
        
        elif _is_descendant_of(nodes, current_left_origin, left_origin_id):
            insert_index += 1
        else:
            break

    nodes.insert(insert_index, new_node)
    return nodes

def _skip_subtree(nodes: List[Dict[str, Any]], start_index: int) -> int:
   
    target_id = nodes[start_index].get("element_id")
    idx = start_index + 1
    while idx < len(nodes):
        if not _is_descendant_of(nodes, nodes[idx].get("left_origin_id"), target_id) and nodes[idx].get("left_origin_id") != target_id:
            break
        idx += 1
    return idx

def _is_descendant_of(nodes: List[Dict[str, Any]], node_id: str, ancestor_id: str) -> bool:
    current_id = node_id
    visited = set()
    
    while current_id and current_id != "ROOT" and current_id not in visited:
        if current_id == ancestor_id:
            return True
        visited.add(current_id)
        
        parent_id = None
        for n in nodes:
            if n.get("element_id") == current_id:
                parent_id = n.get("left_origin_id")
                break
        current_id = parent_id
        
    return False


def render_text(nodes: List[Dict[str, Any]]) -> str:
    return "".join([node.get("character", "") for node in nodes if node.get("character") is not None])