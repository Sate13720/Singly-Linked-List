class Node:
	def __init__(self, data):
		self.data = data
		self.ref = None

class LinkedList:
	def __init__(self):
		self.head = None

	def print_LL(self):
		if self.head == None:  #Checking whether LL is empty or not.
			print("Linked List is empty!.")
		else:
			n = self.head   # means we are on first Node
			while n is not None:
				print( n.data,"-->",end=" ")
				n = n.ref  #go to next node

	def add_begin(self,data):
		new_node = Node(data)
		new_node.ref = self.head #changing new node reference to none
		self.head = new_node     # and head reference to new node

	def add_end(self, data):
		new_node = Node(data)
		if self.head is None: #means we are adding first node
			self.head = new_node
		else:
			n = self.head
			while n.ref is not None:
				n = n.ref
			n.ref = new_node

	def add_after(self, data, x):
		new_node = Node(data)
		n = self.head  #because the node which we entering can't be first node b/c we are entering after the node
		while n is not None:
			if n.data == x: #means we found the node after which we are entering new node
				break
			n = n.ref
		if n is None: #if we are here means given not is  not found
			print("Given Node is not present in the Linked List.")
		else:         #means we find the given node
			new_node.ref = n.ref
			n.ref = new_node

	def add_before(self, data, x):
		if self.head == None:
			print("Linked List is empty.")
			return
		#first we check that given node is first node or not
		if self.head.data == x: #means we adding the first node and the entering node going to be first node
			new_node = Node(data)
			new_node.ref = self.head
			self.head = new_node
			return
		#here we are finding X
		n = self.head
		while n.ref is not None:
			if n.ref.data == x:
				break
			n = n.ref
		if n.ref is None: #means we not found the X
			print("Given Node is not found in the Linked List.")
		else:		#means we find the x given node before which we want to enter new node
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

	def add_empty(self,data):
		if self.head is None: #means LL is empty
			new_node = Node(data)
			self.head = new_node
		else:
			print("Linked List is not Empty.")

	def delete_begin(self):
		if self.head is None:
			print("Linked List is Empty.")
		else:
			self.head = self.head.ref

	def delete_end(self):
		if self.head is None:
			print("Linked List is Empty.")
		elif self.head.ref is None:
			self.head = None
		else:
			n = self.head
			while n.ref.ref is not None:
				n = n.ref
			n.ref = None

	def delete_by_value(self, x):
		if self.head is None:
			print("Linked List is Empty.")
			return
		if self.head.data == x: #means we deleting first Node
			self.head = self.head.ref
			return
		# we are finding X
		n = self.head
		while n.ref is not None: # we came out to while loop in 2 conditions 1. we find x. 2. we not find x means node is not present.
			if x==n.ref.data:
				break
			n = n.ref
		if n.ref is None:
			print("Given Node is not present in the Linked List.")
		else:
			n.ref = n.ref.ref


ll1 = LinkedList()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_end(30)
ll1.add_after(40,10)
ll1.add_before(25,40)
# ll1.add_end(10)
# ll1.add_after(20,20)
# ll1.add_before(5,10)
# ll1.delete_begin()
# ll1.delete_end()
ll1.delete_by_value(25)
ll1.print_LL()



