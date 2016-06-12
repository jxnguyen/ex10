
from math import floor

class Max_Heap():

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
		Convert list a into a heap.
		'''
		# last node
		last = len(a) - 1
		# build heap from bottom up
		for i in range(self.__parent(last), -1, -1):
			# self.to_big(a,i, last)
			self.sift_down(a, i, last)

	def sift_up(self, a, i):
		'''
		Move up through heap & swap out of order elements.
		'''
		parent = self.__parent(i)
		# if current node smaller than parent
		if a[i] > a[parent]:
			# swap
			a[i], a[parent] = a[parent], a[i]
			# move up a layer
			self.sift_up(a, parent)


	def sift_down(self, a, start, end):
		'''
		Repair the Heap from start index down to the leaves. Assumes the subtrees rooted at start are valid heaps.
		'''
		def max_child(a, i):
			'''
			Return index of child with max value.
			'''
			lchild = self.__lchild(i)
			rchild = lchild + 1
			# if two children
			if rchild <= end:
				return lchild if a[lchild] > a[rchild] else rchild
			elif lchild <= end:
				return lchild
			else:
				return None

		root = start
		# child w/ max value
		mchild = max_child(a, root)
		# if child & > than root
		if mchild and a[mchild] > a[root]:
			# swap
			a[root], a[mchild] = a[mchild], a[root]
			# mchild new root
			self.sift_down(a, mchild, end)


def heapsort(a, n):
	# build heap
	h = Max_Heap(a)
	# last index
	end = len(a) - 1
	while end > 0:
		# swap first & last elem
		a[0], a[end] = a[end], a[0]
		# decrement considered range
		end -= 1
		# repair heap
		h.sift_down(a, 0, end)


# TEST SUITE
# --------------------------------------------
from random import randint
l = [randint(0,100) for _ in range(10)]
print("unsorted:\t", l)
heapsort(l, len(l))
print('sorted:\t\t', l)
