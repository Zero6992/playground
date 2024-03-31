package main
type TreeNode struct {
		Val int
		Left *TreeNode
		Right *TreeNode
 }


 func kthSmallest(root *TreeNode, k int) int {
		stack := [] *TreeNode{}
		node := root
		count := 0
		for node != nil || len(stack) > 0 {
			for node != nil {
				stack = append(stack, node)
				node = node.Left
			}
			node = stack[len(stack) - 1]
			stack = stack[:len(stack) - 1]

			count++

			if k == count {
				return node.Val
			}

			node = node.Right
		}
		return 0
 }