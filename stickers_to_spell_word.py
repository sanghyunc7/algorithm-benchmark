from test_harness.harness import *

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        elements = 0

        @lru_cache(maxsize=None)
        def dfs(remain):
            nonlocal elements
            elements += 1
            if remain == "": return 0

            remain_counter = Counter(remain)
            min_stickers = float("inf")

            for sticker_counter in self.sticker_counters:
                applied_counter = {c: max(count - sticker_counter[c], 0) for c, count in remain_counter.items()}
                applied_counter_s = "".join(sorted([ch * count for ch, count in applied_counter.items()]))
                
                if applied_counter_s != remain:
                    num_stickers = 1 + dfs(applied_counter_s)
                    min_stickers = min(min_stickers, num_stickers)
            
            return min_stickers
        self.sticker_counters = [Counter(sticker) for sticker in stickers]
        target = "".join(sorted(target))

        ans = dfs(target)
        print(elements)
        return -1 if ans == float("inf") else ans

    def minStickers1(self, stickers: List[str], target: str) -> int:
        poolStickers = set()
        for s in stickers:
            for c in s:
                poolStickers.add(c)
        for c in target:
            if not c in poolStickers:
                return -1
        
        t = [0] * 26
        for c in target:
            t[ord(c) - ord('a')] += 1
        target_tuple = tuple(t)

        sticker_set = set()
        for s in stickers:
            t = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                # saturation point
                t[i] = min(t[i] + 1, target_tuple[i])
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
            # optimization:
            # reduce states by having a saturation point of target_tuple[i]
            t = []
            for i in range(26):
                t.append(min(t1[i] + t2[i], target_tuple[i]))
            return t

        
        # print(len(stickers))
        # print(len(sticker_set))
        sticker_set = reduced(sticker_set)
        # print(len(sticker_set))
        layer = sticker_set.copy()
        n = 1

        visit = set()
        visit.update(layer)
        while True:
            if target_tuple in layer:
                return n

            # try stickers + reduced_set permutations to create next layer
            next_layer = set()
            for t2 in sticker_set:
                for t1 in layer:
                    # optimization idea:
                    # combine a t2 that will only mark an improvement towards the goal
                    t = tuple(combine(t1, t2))
                    if t not in visit:
                        next_layer.add(t)
            layer = reduced(next_layer)
            visit.update(layer)
            n += 1
            print("n", n)
            print(len(layer))
        return -1

        

        

input1 = [["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"], "stoodcrease"]
input2 = [["all","chord","doctor","dance","drive","ready","phrase","skill","dress","select","if","develop","space","broad","lone","was","fight","how","window","place","has","plural","star","complete","though","rub","practice","here","nation","dark","job","observe","key","hole","short","last","neck","oh","science","industry","work","gun","rule","magnet","stead","many","push","tall","soft","road"], "thosecontinent"]
input3 = [["divide","danger","student","share","feet","say","expect","chair","special","blue","differ","thank","doctor","top","there","had","ice","mark","note","equate","basic","so","hope","happy","draw","evening","star","shall","thousand","mother","quite","letter","atom","baby","such","trouble","stand","day","room","third","level","salt","thing","shore","truck","block","time","fresh","dream","talk"], "distantcollect"]
if __name__ == "__main__":
    test_run(Solution(), [input1, input2, input3], 1)
        