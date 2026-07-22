# 🌳 Binary Tree Inorder Traversal (LeetCode #94)

A simple Python solution for Binary Tree Inorder Traversal using recursion.

---

## 📌 Traversal Order
1. **Left** Subtree
2. **Root** (Node Value)
3. **Right** Subtree

---

## 💡 Key Concept
* **Object Switching:** The inner function `inorder(node)` switches node objects continuously to move deeper into the tree branches.
* **Backtracking:** When there is no right node, execution finishes and automatically backtracks to the parent node.

---

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(N)$