class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sletters= list(s)
        tletters= list(t)
        hashtables = {}
        hashtablet = {}

        for n in sletters:
            hashtables[n] = hashtables.get(n, 0) + 1 
        
        for t in tletters:
            hashtablet[t] = hashtablet.get(t, 0) + 1

        if hashtables == hashtablet:
            return True
        return False