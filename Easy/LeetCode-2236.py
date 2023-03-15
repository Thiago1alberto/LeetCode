# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def checkTree(self, root):

        
        #Verifica se o nó raiz é null.
        if not root:
            return True

        #Verifica se o nó raiz tem algum filho
        if not root.left and not root.right: 
            return True

        #Atribui o valor dos filhos esquerdo e direito da raiz para val_esquerda e val_direita, respectivamente.
        #Se os filhos não existirem (Nenhum), ele atribuirá 0 a eles.
        left_val = root.left.val if root.left else 0 
        right_val = root.right.val if root.right else 0

   
    #Verifica se o valor da raiz é igual a soma dos valores de seus filhos esquerdo e direito.
    #recursivamente verifica as subárvores esquerda e direita chamando o método checkTree nelas.
    #A função retorna True se todas as condições forem atendidas e False caso contrário.
        return root.val == left_val + right_val and \
            self.checkTree(root.left) and \
            self.checkTree(root.right)
