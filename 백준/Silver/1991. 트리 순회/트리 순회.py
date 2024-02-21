import sys

input = sys.stdin.readline

def preorder(T):
    if T != '.':
        print(T, end='')
        preorder(tree[T][0])
        preorder(tree[T][1])

def inorder(T):
    if T != '.':
        inorder(tree[T][0])
        print(T, end='')
        inorder(tree[T][1])
def postorder(T):
    if T != '.':
        postorder(tree[T][0])
        postorder(tree[T][1])
        print(T, end='')

tree = {}
n = int(input())
for i in range(n):
    par, chi1, chi2 = input().split()
    tree[par] = [chi1, chi2]
preorder('A')
print()
inorder('A')
print()
postorder('A')
