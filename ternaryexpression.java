// # Let's assume the input ternary expression is valid, we can build the tree in preorder manner.

// # Each time we scan two characters, the first character is either ? or :,
// # the second character holds the value of the tree node. When we see ?, 
// #we add the new node to left. 
// #When we see :, we need to find out the ancestor node that doesn't have a right node, and make the new node as its right child.

// # Time complexity is O(n).
// public TreeNode convertToBT (char[] values) {  
//     TreeNode root = new TreeNode(values[0]);  
//     TreeNode n = root;  
//     Stack<TreeNode> a =  new Stack<TreeNode>();  
//     for (int i = 1; i < values.length; i += 2) {  
//         if (values[i] == '?') {  
//             n.left = new TreeNode (values[i + 1]);  
//             a.add(n);  
//             n = n.left;  
  
//         }  
//         else if (values[i] == ':') {  
//             n = a.pop();  
//             while (n.right != null) {  
//                 n = a.pop();  
//             }               
//             n.right = new TreeNode (values[i + 1]);  
//             a.add(n);  
//             n = n.right;  
//         }  
//     }  
//     return root;  
// } 

