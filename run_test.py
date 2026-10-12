# run_test.py (placed directly in the root crdt_engine/ folder)
from crdt_engine.engine import insert_node, render_text

def test_basic_insertion():
    nodes = [{"element_id": "ROOT", "parent_id": None, "character": None}]
    nodes = insert_node(nodes, {"element_id": "c1:1", "parent_id": "ROOT", "character": "h"})
    nodes = insert_node(nodes, {"element_id": "c1:2", "parent_id": "c1:1", "character": "e"})
    nodes = insert_node(nodes, {"element_id": "c1:3", "parent_id": "c1:2", "character": "l"})

    assert render_text(nodes) == "hel"
    print("Basic insertion test passed! ✅")

if __name__ == "__main__":
    test_basic_insertion()
    print("All tests passed successfully!")
    