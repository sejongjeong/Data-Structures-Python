import random

class Node:
	def __init__(self, number, left = None, right = None) -> None:
		self.data = number
		self.left = left
		self.right = right
	def __repr__(self):
		return str(self.data)

class Binary_Search_Tree:
	def __init__(self, number = None):
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

	def __preorder(self, node):
		if node is None:
			return
		print(node, end = ' ')
		self.__preorder(node.left)
		self.__preorder(node.right)

	def preorder(self):
		self.__preorder(self.root)
		print()
	
	def __inorder(self, node):
		if node is None:
			return
		self.__inorder(node.left)
		print(node, end = ' ')
		self.__inorder(node.right)
	
	def inorder(self):
		self.__inorder(self.root)
		print()
	
	def __postorder(self, node):
		if node is None:
			return
		self.__postorder(node.left)
		self.__postorder(node.right)
		print(node, end = ' ')

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
		

bst = Binary_Search_Tree()
arr = list(range(100))
random.shuffle(arr)
for i in range(12):
	tmp = int(input())
	bst.insert(tmp)
bst.preorder()
bst.inorder()
bst.postorder()
print(bst.max_of_tree())
print(bst.min_of_tree())