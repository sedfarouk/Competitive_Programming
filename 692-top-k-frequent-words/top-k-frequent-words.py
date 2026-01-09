class Element:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word 
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = []

        for word, freq in cnt.items():
            if len(heap) < k:
                heappush(heap, Element(word, freq))

            elif freq > heap[0].freq or (freq == heap[0].freq and word < heap[0].word):
                heapreplace(heap, Element(word, freq))

        heap.sort(reverse=True)
        return [element.word for element in heap]