class LinkedList:

    def __init__(self):
        self.firstElem = None

    # Dodaje element na koniec listy
    def push(self, item):
        if self.firstElem == None:
            self.firstElem = LinkedListElement(item)
        else:
            el = self.firstElem
            while el.nextElem != None:
                el = el.nextElem
            el.nextElem = LinkedListElement(item)

    # Wstawia element na właściwe miejsce, zakładając, że lista jest posortowana
    def push_sorted(self, item):
        if self.firstElem == None:
            self.push(item)
            return

        el = self.firstElem
        while el.nextElem != None:
            if el.nextElem.content >= item:
                break
            el = el.nextElem

        next_elem = el.nextElem
        el.nextElem = LinkedListElement(item)
        el.nextElem.nextElem = next_elem

    # Sprawdza, czy element o podanej wartości istnieje na liście
    def exists(self, item):
        el = self.firstElem
        while el != None:
            if el.content == item:
                return True
            el = el.nextElem

        return False

    # Usuwa pierwszy element
    def remove_first(self):
        if self.firstElem == None:
            return
        self.firstElem = self.firstElem.nextElem

class LinkedListElement:

    def __init__(self, content):
        self.content = content
        self.nextElem = None
