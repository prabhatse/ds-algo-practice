
class Node (object):
    def __init__ (self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

class BST(object):

    def __init__ (self):
        self.root = None

    def insert (self, newData):
        leaf = Node(newData)

        if self.root is None:
            self.root = leaf
        else:
            current = self.root
            parent = self.root
            while current is not None:
                parent = current
                if newData < current.data:
                    current = current.left
                else:
                    current = current.right

            if newData < parent.data:
                parent.left = leaf
            else:
                parent.right = leaf

    def insert(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)

    # Recursive insertion
    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self._insert(node.right, data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)


    # returns false if the item to be deleted is not on the tree
    def delete (self, data):
        current = self.root
        parent = self.root
        isLeft = False

        if current is None:
            return False

        while current is not None and current.data is not data:
            parent = current
            if data < current.data:
                current = current.left
                isLeft = True 
            else:
                current = current.right
                isLeft = False

        if current is None:
            return False
        # Node has not any children
        if current.left is None and current.right is None:
            if current is self.root:
                self.root = None
            elif isLeft:
                parent.left = None
            else:
                parent.right = None

        # There is no right child
        elif current.right is None:
            if current is self.root:
                self.root = current.left
            elif isLeft:
                parent.left = current.left
            else:
                parent.right = current.left
        # There is no left child
        elif current.right is None:
            if current is self.root:
                self.root = current.right
            elif isLeft:
                parent.lChild = current.right
            else:
                parent.right = current.right
        
        # Both child present
        else:
            successor = current.right
            successorParent = current

            while successor.left is not None:
                successorParent = successor
                successor = successor.left

            if current is self.root:
                self.root = successor
            elif isLeft:
                parent.left = successor
            else:
                parent.right = successor

            successor.left = current.left

            if successor is not current.right:
                successorParent.left = successor.right
                successor.right = current.right

        return True 


    def minNode (self):
        current = self.root
        while current.left is not None:
            current = current.left

        return current.data

    def maxNode (self):
        current = self.root
        while current.right is not None:
            current = current.right

        return current.data

    def _check_balance(self, node):
        if node is None:
            return 0
        left_height = self._check_balance(node.left)
        if left_height == -1:
            return -1
        right_height = self._check_balance(node.right)
        if right_height == -1:
            return -1

        diff = abs(left_height - right_height)
        if diff > 1:
            return -1
        return 1 + max(left_height, right_height)

    def get_height(self, node):
        if node is None:
            return 0
        else:
            return 

    def check_balance(self):
        if self.root is None:
            raise TypeError("root cannot be None")
        height = self._check_balance(self.root)
        return height != -1

    """
                 Y                           X
               /   \      Right(Y)          /  \
              X     C   ==========>        A    Y
             /  \       <==========            /  \
            A    B       Left(X)              B    C

    There are following four cases to handle:
        a) y is left child of z and x is left child of y (Left Left Case)

        T1, T2, T3 and T4 are subtrees.
                 z                                      y 
                / \                                   /   \
               y   T4      Right Rotate (z)          x      z
              / \          - - - - - - - - ->      /  \    /  \ 
             x   T3                               T1  T2  T3  T4
            / \
          T1   T2

        b) y is left child of z and x is right child of y (Left Right Case)

             z                               z                           x
            / \                            /   \                        /  \ 
           y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
          / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
        T1   x                          y    T3                    T1  T2 T3  T4
            / \                        / \
          T2   T3                    T1   T2


        c) y is right child of z and x is right child of y (Right Right Case)

          z                                y
         /  \                            /   \ 
        T1   y     Left Rotate(z)       z      x
            /  \   - - - - - - - ->    / \    / \
           T2   x                     T1  T2 T3  T4
               / \
             T3  T4

        d) y is right child of z and x is left child of y (Right Left Case)

           z                            z                            x
          / \                          / \                          /  \ 
        T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
            / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
           x   T4                      T2   y                  T1  T2  T3  T4
          / \                              /  \
        T2   T3                           T3   T4


                 Y                           X
               /   \      Right(Y)          /  \
              X     C   ==========>        A    Y
             /  \       <==========            /  \
            A    B       Left(X)              B    C


    """    

    def right_rotate(self, y):
        parent_y = y.parent
        left_y = y.left
        B = left_y.right
        left_y.parent = parent_y
        y.parent = left_y
        left_y.right = y
        B.parent = y
        y.left = B
        return left_y

    def left_rotate(self, x):
        parent_x = x.parent
        right_x = x.right
        B = right_x.left
        right_x.parent = parent_x
        x.parent = right_x
        right_x.left = x
        B.parent = x
        x.right = B
        return right_x

    def  insert_into_avl_tree(self, data):
        node = self.inert(data)
        self._rebalance_tree(node.parent, data)

    def _rebalance_tree(node, data):
        if node is None:
            return

        while node is not None:
            balance = self._check_balance(node)
            if balance == -1:
                if data < node.left.data:
                    self.right_rotate(node)
                elif data > node.right.data:
                    self.left_rotate(node)
                elif data > node.left.data:
                    node.left = self.left_rotate(node.left)
                    self.right_rotate(node)
                else data < node.right.data:
                    node.right = self.right_rotate(node.right)
                    self.left_rotate(node)
                node = node.parent
  
  
    def printPostOrder (self):
        global postOrder
        postOrder = []

        def PostOrder(node):
            if node is not None:
                PostOrder(node.left)
                PostOrder(node.right)
                postOrder.append(node.data)

        PostOrder(self.root)
        return postOrder

    def printInOrder (self):
        global inOrder 
        inOrder = []

        def InOrder (node):
            if node is not None:
                InOrder(node.left)
                inOrder.append(node.data)
                InOrder(node.right)

        InOrder(self.root)
        return inOrder

    def printPreOrder (self):
        global preOrder
        preOrder = []

        def PreOrder (node):
            if node is not None:
                preOrder.append(node.data)
                PreOrder(node.left)
                PreOrder(node.right)

        PreOrder(self.root)
        return preOrder

    def treeIsEmpty (self):
        return self.root is None