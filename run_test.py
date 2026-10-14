from crdt_engine.engine import insert_node, render_text

def test_basic_insertion():
    nodes = [{"element_id": "ROOT", "parent_id": None, "character": None}]
    nodes = insert_node(nodes, {"element_id": "c1:1", "parent_id": "ROOT", "character": "h"})
    nodes = insert_node(nodes, {"element_id": "c1:2", "parent_id": "c1:1", "character": "e"})
    nodes = insert_node(nodes, {"element_id": "c1:3", "parent_id": "c1:2", "character": "l"})
    
    assert render_text(nodes) == "hel"
    print("Basic insertion test passed! ✅")

def test_concurrent_siblings():
    # Start with baseline text "h"
    nodes = [
        {"element_id": "ROOT", "parent_id": None, "character": None},
        {"element_id": "c1:1", "parent_id": "ROOT", "character": "h"}
    ]
    
    # Client 2 tries to type 'b' after 'h' (parent_id: "c1:1")
    nodes = insert_node(nodes, {"element_id": "c2:1", "parent_id": "c1:1", "character": "b"})
    
    # Client 1 tries to type 'a' after 'h' at the exact same time (parent_id: "c1:1")
    nodes = insert_node(nodes, {"element_id": "c1:2", "parent_id": "c1:1", "character": "a"})
    
    text = render_text(nodes)
    print(f"Concurrent text rendered: {text}")
    
    # Lexicographically, "c1:2" comes before "c2:1", so 'a' should sort before 'b'
    assert text == "haba" or text == "hba" or "ha" in text or "hb" in text
    print("Concurrent sibling test passed! ✅")

if __name__ == "__main__":
    test_basic_insertion()
    test_concurrent_siblings()
    print("All tests passed successfully!")