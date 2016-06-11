
from math import floor

class Heap():

	def __init__(self, l = []):
		self.heapify(l)
		self.heap = l

	def __root(self, node):
		return (node - 1)//2

	def __lchild(self, node):
		return 2 * node + 1

	def __rchild(self, node):
		return 2 * node + 2

	def heapify(self,A):
		'''
		Convert the list A into a valid heap, building from bottom up.
		'''
		def sift_down(A, start, end):
			'''
			Move through the heap from the node indicated by 'start' and swap any nodes out of order. Assumes the heaps rooted at the children of of the start node are valid.
			'''
			# start root node
			root = start
			# while root has a child node
			while self.__lchild(root) <= end:
				# node w/ smallest value
				swap   = root
				lchild = self.__lchild(root)
				rchild = lchild + 1
				# left child smaller
				if A[lchild] < A[swap]:
					swap = lchild
				# if there is right child & it is smaller
				if rchild <= end and A[rchild] < A[swap]:
					swap = rchild
				# root is smallest
				if swap == root:
					# no changes needed
					return
				else:
					# swap root with node w/ smallest val
					A[root], A[swap] = A[swap], A[root]
					# next root
					root = swap
		# last node & its parent
		last_node = len(A) - 1
		start = self.__root(last_node)
		# for each parent node
		while start >= 0:
			# construct valid sub heap
			sift_down(A, start, last_node)
			# prev parent
			start -= 1


# TEST SUITE
# --------------------------------------------
l = [22,1,5,35,14,9,19,43,32]
h = Heap(l)
print(h.heap)
