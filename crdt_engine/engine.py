from typing import TypedDict,List, Dict, Any, Optional

class NodeDict(TypedDict):
    element_id: str
    parent_id: Optional[str]
    character: Optional[str]
    is_deleted: bool

def insert_node(nodes: List[NodeDict], new_node: NodeDict) -> List[NodeDict]:
    target_parent_id = new_node.get("parent_id")
    new_id = new_node.get("element_id")
    
    parent_index = 0
    if target_parent_id and target_parent_id != "ROOT":
        for i, node in enumerate(nodes):
            if node.get("element_id") == target_parent_id:
                parent_index = i
                break

    insert_index = parent_index + 1
    
    while insert_index < len(nodes):
        current_node = nodes[insert_index]
        current_parent_id = current_node.get("parent_id")  
        
        if current_parent_id == target_parent_id:
            if new_id < current_node.get("element_id"):
                break  
            else:
                insert_index += 1  
        elif _is_descendant_of(nodes, current_parent_id, target_parent_id):
            insert_index += 1
        else:
            break

    nodes.insert(insert_index, new_node)
    return nodes


def _is_descendant_of(nodes: List[NodeDict], current_parent_id: str, target_parent_id: str) -> bool:
    visited = set()
    
    while current_parent_id and current_parent_id != "ROOT" and current_parent_id not in visited:
        if current_parent_id == target_parent_id:
            return True
        visited.add(current_parent_id)
        
        next_parent_id = None
        for n in nodes:
            if n.get("element_id") == current_parent_id:
                next_parent_id = n.get("parent_id")
                break
        current_parent_id = next_parent_id
        
    return False


def render_text(nodes: List[NodeDict]) -> str:
    return "".join([
        node.get("character", "") 
        for node in nodes 
        if not node.get("is_deleted", False) and node.get("character") is not None
    ])


def delete_node(nodes: List[NodeDict], element_id: str) -> List[NodeDict]:
    for node in nodes:
        if node.get("element_id") == element_id:
            node["is_deleted"] = True
            break
    return nodes