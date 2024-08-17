# https://leetcode.com/problems/convert-bst-to-greater-tree/
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {TreeNode}
def convert_bst(root)
    greater(root, [0])
    root
end

def greater(node, total)
    return if node.nil?

    greater(node.right, total)
    node.val = node.val + total[0]
    total[0] = node.val
    greater(node.left, total)
end
