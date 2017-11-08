# 求有根树的任意两个节点的最近公共祖先。

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def build_tree(tree, root, idx, length):
    if idx == 0:
        result = root
    else:
        result = TreeNode(tree[idx])
    left = idx * 2 + 1
    right = idx * 2 + 2
    if left < length and tree[left] is not None:
        result.left = build_tree(tree, root, left, length)
    if right < length and tree[right] is not None:
        result.right = build_tree(tree, root, right, length)
    return result

def binary_search(t, u, v):
	left = u
	right = v

	if left > right:
		temp = left
		left = right
		right = temp

	while True:
		if t.val < left:
			t = t.right
		elif t.val > right:
			t = t.left
		else:
			return t.val

def getLCA(t, u, v):
	if not t:
		return None
	if t.val == u or t.val == v:
		return t

	left = getLCA(t.left, u, v)
	right = getLCA(t.right, u, v)

	if left and right:
		return t
	elif left:
		return left
	elif right:
		return right
	else:
		return None

if __name__ == '__main__':
	s = [6,4,8,2,5,7,9,1,3]
	root = TreeNode(s[0])
	build_tree(s, root, 0, len(s))
	ans = binary_search(root, 1, 9)
	# print(ans)
	s1 = [1,2,3,4,5,6,7,8,9]
	root2 = TreeNode(s1[0])
	build_tree(s1, root2, 0, len(s1))
	res = getLCA(root2, 3, 7)
	print(res.val)