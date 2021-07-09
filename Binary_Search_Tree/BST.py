import random


class Node:
	def __init__(self, number, left=None, right=None) -> None:
		self.data = number
		self.left = left
		self.right = right

	def __repr__(self):
		return str(self.data)


class Binary_Search_Tree:
	def __init__(self, number=None):
		if number is None:
			self.root = None
		else:
			self.root = Node(number)

	def search(self, number):
		tmp = self.root
		while tmp:
			if tmp.data == number:
				return tmp
			elif tmp.data > number:
				tmp = tmp.left
			elif tmp.data < number:
				tmp = tmp.right
		return tmp

	def insert(self, number):
		if self.root is None:
			self.root = Node(number)
			return
		tmp = self.root
		prev = None
		while tmp:
			prev = tmp
			if tmp.data == number:
				print("The number entered already exists!")
			elif tmp.data > number:
				tmp = tmp.left
			elif tmp.data < number:
				tmp = tmp.right
		if number > prev.data:
			prev.right = Node(number)
		elif number < prev.data:
			prev.left = Node(number)

	def delete(self, number):  # Delete Algorithm isn't working
		tmp = self.root
		prev = None
		isleft = True      #True : prev's left child is tmp.
		while tmp:
			if tmp.data == number:
				break
			prev = tmp
			if tmp.data > number:
				isleft = True
				tmp = tmp.left
			elif tmp.data < number:
				isleft = False
				tmp = tmp.right
		if tmp:
			if tmp.left is None and tmp.right is None:
				if not prev:
					if isleft:
						prev.left = None
					else:
						prev.right = None
				else:
					self.root = None
			elif tmp.left is None or tmp.right is None:
				if not tmp.left:
					if isleft:
						prev.left = tmp.left
					else:
						prev.right = tmp.left
				elif not tmp.right:
					if isleft:
						prev.left = tmp.right
					else:
						prev.right = tmp.right
			else:
				biglittle = tmp.right
				prev_biglittle = tmp
				while biglittle.left:
					prev_biglittle = biglittle
					biglittle = biglittle.left
				if not (biglittle.left or biglittle.right):
					prev_biglittle.left = None
				elif not biglittle.right:
					prev_biglittle.left = biglittle.right
				if isleft:
					prev.left = biglittle
				else:
					prev.right = biglittle
				biglittle.left = tmp.left
				biglittle.right = tmp.right
				del tmp
		else:
			print("The number entered not exists!")

	def __preorder(self, node):
		if node is None:
			return
		print(node, end=' ')
		self.__preorder(node.left)
		self.__preorder(node.right)

	def preorder(self):
		self.__preorder(self.root)
		print()

	def __inorder(self, node):
		if node is None:
			return
		self.__inorder(node.left)
		print(node, end=' ')
		self.__inorder(node.right)

	def inorder(self):
		self.__inorder(self.root)
		print()

	def __postorder(self, node):
		if node is None:
			return
		self.__postorder(node.left)
		self.__postorder(node.right)
		print(node, end=' ')

	def postorder(self):
		self.__postorder(self.root)
		print()

	def max_of_tree(self):
		tmp = self.root
		prev = None
		while tmp:
			prev = tmp
			tmp = tmp.right
		return prev.data

	def min_of_tree(self):
		tmp = self.root
		prev = None
		while tmp:
			prev = tmp
			tmp = tmp.left
		return prev.data

	def __height(self, node):
		if node is None:
			return 0
		else:
			return max(self.__height(node.left), self.__height(node.right)) + 1

	def height(self):
		return self.__height(self.root)


bst = Binary_Search_Tree()
arr = list(range(100))
random.shuffle(arr)
for i in range(12):
	tmp = int(input())
	bst.insert(tmp)
#bst.delete()
bst.preorder()
bst.inorder()
bst.postorder()
print(bst.max_of_tree())
print(bst.min_of_tree())
print(bst.height())