class TrieNode:
    """
        Implementa un nodo de un Trie.
    """
    def __init__(self):
        """
            Inicializa un nodo de Trie con un diccionario de hijos y un indicador de fin de palabra.
        """
        self.children = {}
        self.is_end = False

class Trie:
    """
        Implementa una estructura de Trie para almacenar palabras y detectar prefijos.
        Attributes:
            root: TrieNode
                Nodo raíz del Trie.
    """

    def __init__(self):
        """Inicializa un Trie con un nodo raíz vacío."""
        self.root = TrieNode()

    def insert(self, word):
        """
            Inserta una palabra en el Trie y verifica si es un prefijo o tiene prefijos.
            :params: word: str: La palabra a insertar en el Trie.
            :return: bool: True si la palabra es un prefijo de otra o si otra palabra es su prefijo. False en caso
            contrario.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if node.is_end:
                return True
        node.is_end = True

        if node.children:
            return True

        return False

    def search(self, word):
        """
            Verifica si una palabra existe en el Trie.
            :params: word: str: La palabra a buscar en el Trie.
            :return: bool: True si se encuentra la palabra y es una palabra completa en el Trie, False de otra forma.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end


def noPrefix(words):
    """
        Verifica si un conjunto de palabras no tiene prefijos comunes.
        :param words: List[str]: Un conjunto de palabras.
        :return: None
    """
    trie = Trie()
    for i in words:
        if trie.insert(i):
            print('BAD SET')
            print(i)
            return
    print('GOOD SET')


if __name__ == '__main__':
    n = int(input().strip())
    words = []
    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
