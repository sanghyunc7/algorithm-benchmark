from test_harness.harness import *
from typing import *

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        poolStickers = set()
        for s in stickers:
            for c in s:
                poolStickers.add(c)
        for c in target:
            if not c in poolStickers:
                return -1
        
        # work in layers
        # create a layer by trying all stickers on all elements from prev layer
        # prune the layer by removing elements that are dominated
        layer = []

        target_tuple = [0] * 26
        target_set = set()
        for c in target:
            target_tuple[ord(c) - ord('a')] += 1
            target_set.add(c)

        sticker_set = set()
        for s in stickers:
            t = [0] * 26
            for c in s:
                if c in target_set:
                    t[ord(c) - ord('a')] += 1
            sticker_set.add(tuple(t))
        

        # does t1 dominate t2?
        def dominate(t1, t2):
            # does t2 have any letters with a greater count than t1?
            for i in range(26):
                if t2[i] > t1[i]:
                    return False
            return True

        
        def reduced(layer):
            reduced_set = set()
            for t2 in layer:
                # is t2 dominated by any t1 element?
                dominated = False
                for t1 in layer:
                    if t1 == t2:
                        # dont count this case of domination
                        continue
                    if dominate(t1, t2):
                        dominated = True
                        break
                if not dominated:
                    reduced_set.add(t2)
            return reduced_set

        def combine(t1, t2):
            t = []
            for i in range(26):
                t.append(t1[i] + t2[i])
            return t
        
        # does adding t2 help t1 get closer to target?
        def useful(t1, t2):
            good = False
            for i in range(26):
                if target_tuple[i] - t1[i] > 0 and t2[i] > 0:
                    good = True
                    break
            return good

        
        def found_target(t):
            for i in range(26):
                if t[i] < target_tuple[i]:
                    return False
            return True
        # print(len(stickers))
        # print(len(sticker_set))
        sticker_set = reduced(sticker_set)
        # print(len(sticker_set))
        layer = sticker_set.copy()
        n = 1
        while True:
            for t in layer:
                if found_target(t):
                    return n

            # try stickers + reduced_set permutations to create next layer
            next_layer = set()
            for t2 in sticker_set:
                for t1 in layer:
                    # optimization idea:
                    # combine a t2 that will only mark an improvement towards the goal
                    if useful(t1, t2):
                        next_layer.add(tuple(combine(t1, t2)))
            layer = reduced(next_layer)
            n += 1
            print("n", n)
            print(len(layer))
        return -1

        

        

input1 = [["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"], "stoodcrease"]
input2 = [["all","chord","doctor","dance","drive","ready","phrase","skill","dress","select","if","develop","space","broad","lone","was","fight","how","window","place","has","plural","star","complete","though","rub","practice","here","nation","dark","job","observe","key","hole","short","last","neck","oh","science","industry","work","gun","rule","magnet","stead","many","push","tall","soft","road"], "thosecontinent"]
input3 = [["divide","danger","student","share","feet","say","expect","chair","special","blue","differ","thank","doctor","top","there","had","ice","mark","note","equate","basic","so","hope","happy","draw","evening","star","shall","thousand","mother","quite","letter","atom","baby","such","trouble","stand","day","room","third","level","salt","thing","shore","truck","block","time","fresh","dream","talk"], "distantcollect"]
if __name__ == "__main__":
    test_run(Solution(), [input1, input2, input3])
        