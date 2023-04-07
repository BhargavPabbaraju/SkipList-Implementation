

from random import randint as rand

class Node:
  def __init__(self,key):
    self.bottom = None
    self.right = None
    self.key = key

class SkipList:
  def __init__(self,n):
    self.maxLevels = n
    self.leftInfinities = []
    self.rightInfinities = []
    self.currentMaxLevel = self.maxLevels-1
    for i in range(self.maxLevels):
      left = Node(-float('inf'))
      right = Node(float('inf'))
      left.right = right
      if i>0:
        self.leftInfinities[i-1].bottom = left
        self.rightInfinities[i-1].bottom = right
      self.leftInfinities.append(left)
      self.rightInfinities.append(right)
  


  def getNearestNode(self,key):
    node = self.leftInfinities[self.currentMaxLevel]
    prevNode = self.leftInfinities[self.currentMaxLevel]
    
    
    while node:
      if node.right.key<key:
        prevNode = node
        node = node.right
        
      else:
        prevNode = node
        node = node.bottom
    
    return prevNode
  

  def lookup(self,key):
    node = self.leftInfinities[self.currentMaxLevel]
    
    
    while node:
      if node.right.key==key:
        print(key,"found.")
        return
        #return True
      if node.right.key<key:
        print('right value',node.right.key,'<',key,'moving right')
        node = node.right
        
      else:
        print('right value',node.right.key,'>',key,'moving down')
        node = node.bottom

    
    print(key,"not found.")
    #return False
    
  

  def insert(self,key,rands=[]):
    print("Inserted",key)
    prevNode = self.getNearestNode(key)
    newNode = Node(key)
    newNode.right = prevNode.right
    prevNode.right = newNode
   
    
    self.increaseLevels(newNode,rands)

  def delete(self,key):
    print("Deleted",key)
    node = self.getNearestNode(key)
    if not (node.right and node.right.key==key):
      print(str(key)+" not found.")
      return

    leftNode = self.leftInfinities[self.currentMaxLevel]
    rightNode = leftNode
    level = self.currentMaxLevel

    while level<self.maxLevels:
      while rightNode.right!=None:
        if rightNode.right.key == key:
          rightNode.right = rightNode.right.right
          break
        rightNode = rightNode.right
      

      if leftNode.bottom:
        leftNode = leftNode.bottom
        rightNode = leftNode
      level+=1
    
    self.update_current_max_level()
    
  
  def update_current_max_level(self):
    leftNode = self.leftInfinities[self.currentMaxLevel]
    while leftNode.right.key == float('inf'):
      self.currentMaxLevel+=1
      leftNode = leftNode.bottom
  

  def flip(self):
    r = rand(1,100)
    #print(r)
    return r<50

  
  def increaseLevels(self,node,rands=[]):
    level = self.maxLevels - 2
    if len(rands)>0:
      for r in rands:
        if r==0 or level<0:
          return
        newNode = Node(node.key)
        newNode.bottom = node
        node = self.leftInfinities[level]
        while  node and node.key < newNode.key:
          prevNode = node
          node = node.right
        
        newNode.right = prevNode.right
        prevNode.right = newNode
        node = newNode


        level-=1
        if level < self.currentMaxLevel:
          self.currentMaxLevel = level+1

        
        
    else:
      while self.flip() and level>=0:
        newNode = Node(node.key)
        newNode.bottom = node
        node = self.leftInfinities[level]
        while  node and node.key < newNode.key:
          prevNode = node
          node = node.right
        
        newNode.right = prevNode.right
        prevNode.right = newNode
        node = newNode


        level-=1
        if level < self.currentMaxLevel:
          self.currentMaxLevel = level
        
        self.currentMaxLevel+=1
    
    #print()


    

  def traverse(self):
    leftNode = self.leftInfinities[self.currentMaxLevel]
    rightNode = leftNode
    level = self.currentMaxLevel

    while level<self.maxLevels:
      while rightNode.right!=None:
        print(rightNode.key,end='->')
        rightNode = rightNode.right
      
      print(rightNode.key)
      if leftNode.bottom:
        leftNode = leftNode.bottom
        rightNode = leftNode
      level+=1

sl = SkipList(50)

