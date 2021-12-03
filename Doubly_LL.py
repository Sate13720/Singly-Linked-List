class Node:
	def __init__(self, data):
		self.data = data
		self.nref = None
		self.pref = None

class doubly_LL:
	def __init__(self):
		self.head = None

	def print_LL(self):
		if self.head == None:
			print("Doubly LL is Empty!")
		else:
			n = self.head
			while n is not None:
				print(n.data,"-->",end=" ")
				n = n.nref
	
	def print_LL_reverse(self):
		print()
		if self.head == None:
			print("Doubly LL is Empty!")
		else:
			n = self.head
			while n.nref is not None:
				n = n.nref
			while n is not None:
				print(n.data,"-->",end=" ")
				n = n.pref

	def insert_empty(self, data):
		if self.head is None:
			new_node = Node(data)
			self.head =new_node
		else:
			print("Doubly LL is not Empty.")

	def add_begin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			new_node.nref = self.head
			self.head.pref = new_node
			self.head = new_node
			
	def add_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			n = self.head
			while n.nref is not None:
				n = n.nref
			new_node.pref = n
			n.nref = new_node

	def add_after(self, data, x):
		new_node = Node(data)
		if self.head is None:
			print("LL is empty we can't add.")
		else:
			n = self.head
			while n is not None:
				if x == n.data:
					break
				n = n.nref
			if n is None:
				print("Given Node is not present in LL. So we can't add.")
			else:
				new_node.pref = n
				new_node.nref = n.nref
				if n.nref is not None:
					n.nref.pref = new_node
				n.nref = new_node

	def add_before(self, data, x):
		new_node = Node(data)
		if self.head is None:
			print("LL is empty we can't add.")
		else:
			n = self.head
			while n is not None:
				if x == n.data:
					break
				n = n.nref
			if n is None:
				print("Given Node is not present in LL. So we can't add.")
			else:
				new_node.pref = n.pref
				new_node.nref = n
				if n.pref is not None:
					n.pref.nref = new_node
				else:
					self.head = new_node
				n.pref = new_node

	def delete_begin(self):
		if self.head is None:
			print("LL is empty we can't add.")
			return
		if self.head.nref is None:
			self.head  = None
			print("LL is empty after deleting this node.")
		else:
			self.head = self.head.nref
			self.head.pref = None

	def delete_end(self):
		if self.head is None:
			print("LL is empty we can't add.")
		if self.head.nref is None:
			self.head  = None
			print("LL is empty after deleting this node.")
		else:
			n = self.head
			while n.nref is not None:
				n = n.nref
			n.pref.nref = None

	def delete_by_value(self, x):
		if self.head is None:
			print("LL is empty we can't add.")
			return
		if self.head.nref is None:
			if self.head.data == x:
				self.head = None
			else:
				print("Given node is not present in LL.")
			return
		if self.head.data == x:
			self.head = self.head.nref
			self.head.pref = None
			return
		n = self.head
		while n.nref is not None:
			if x == n.data:
				break
			n = n.nref
		if n.nref is not None:
			n.nref.pref = n.pref
			n.pref.nref = n.nref
		else:
			if n.data is None:
				n.pref.nref = None
			else:
				print("Given node si not present.")

ll = doubly_LL()
ll.add_begin(30)
ll.add_begin(20)
ll.add_begin(10)
# ll.insert_empty(5)
ll.add_end(40)
ll.add_after(25,20)
ll.add_before(35,40)
ll.delete_begin()
ll.delete_end()
ll.delete_by_value(25)
ll.print_LL()
ll.print_LL_reverse()

				