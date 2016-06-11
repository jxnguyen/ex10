
from math import floor

class Heap():

	def __init__(self, l = []):
		self.heapify(l)
		self.heap = l

	def __parent(self, node):
		return (node - 1)//2

	def __lchild(self, node):
		return 2 * node + 1

	def __rchild(self, node):
		return 2 * node + 2

	def heapify(self, a):
		'''
		Convert list a into a valid heap.
		'''
		# last node
		last = len(a) - 1
		# build heap from bottom up
		for i in range(self.__parent(last), -1, -1):
			self.to_big(a,i)

	def to_small(self, a, i):
		'''
		Move up through heap & swap out of order elements.
		'''
		parent = self.__parent(i)
		# if current node smaller than parent
		if a[i] < a[parent]:
			# swap
			a[i], a[parent] = a[parent], a[i]
			# move up a layer
			self.to_small(a, parent)

	def to_big(self, a, i):
		'''
		Move down through the heap & swap out of order elements.
		'''
		# last node
		end = len(a) - 1
		# children
		lchild, rchild = self.__lchild(i), self.__rchild(i)
		# if children
		if lchild <= end:
			# find smallest
			swap = i
			# left child smaller than parent
			if a[swap] > a[lchild]:
				swap = lchild
			# if right child is smaller
			elif rchild <= end and a[swap] > a[rchild]:
				swap = rchild
			else:
				# parent is smallest
				return

			# swap
			a[i], a[swap] = a[swap], a[i]
			# move down a layer
			self.to_big(a, swap)



# TEST SUITE
# --------------------------------------------
from random import randint
l = [randint(0,100) for _ in range(10)]
h = Heap(l)
print(h.heap)
