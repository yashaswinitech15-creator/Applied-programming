/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> res;
    public void solve(TreeNode root){
        if(root==null) return;
        solve(root.left);
        res.add(root.val);
        solve(root.right);
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        res = new ArrayList<>();

        // Approach-1 : Recursive
        // solve(root);
        // return res;

        // Approach-2 : Iterative
        if(root==null) return res;
        Stack<TreeNode> st = new Stack<>();
        st.push(root);
        TreeNode curr = root;
        while(!st.isEmpty()){
            if(curr!=null){
                st.push(curr.left);
                curr = curr.left;
            }else{
                curr = st.pop();
                if(curr!=null){
                    res.add(curr.val);
                    st.push(curr.right);
                    curr = curr.right;
                }
            }
        }
        return res;
    }
}