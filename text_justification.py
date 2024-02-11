class Solution:
    def fullJustify(self, words, maxWidth):

        line = 0
        ans = []
        out = []


        def left_justified(out):
            sout = " ".join(out)
            sout += " " * (maxWidth - len(sout))
            ans.append(sout)

        def flush(out):
            if not out:
                return
            if len(out) == 1:
                return left_justified(out)

            len_words = [len(word) for word in out]
            total_space = maxWidth - sum(len_words)
            num_spaces = len(out) - 1
            avg_space = total_space // num_spaces
            leftover_space = total_space % num_spaces
            space = [" " * avg_space] * num_spaces
            for i in range(leftover_space):
                space[i] += " "
            
            sout = []
            for i in range(len(space)):
                sout.extend([out[i], space[i]])
            sout.append(out[-1])
            ans.append("".join(sout))



        for i in range(len(words)):
            if line + len(words[i]) <= maxWidth:
                out.append(words[i])
                line += len(words[i]) + 1
            else:
                flush(out)
                out = [words[i]]
                line = len(words[i]) + 1
        
        # add last line so that it is left-justified
        left_justified(out)

        return ans


test = [["This", "is", "an", "example", "of", "text", "justification."], 16]
harness = Solution()
out = harness.fullJustify(test[0], test[1])
for o in out:
    print(o)
soln = ["This    is    an","example  of text","justification.  "]

test2 = ["Valinor was encircled by the Pelóri mountains to the east, which were raised by the Valar as a defence against Melkor. To the west was Ekkaia, the encircling sea which surrounded both Valinor and Middle-earth. Everything in the realm, from the stones to the waters, were hallowed and stainless and there was no sickness, corruption or withering. In Valinor the Valar brought what beauty and light they salvaged from the Spring of Arda before the marring, and they created new things, making Valinor even fairer than Almaren. Its major city was Valimar of many bells, built in the midst of the plain,[1] where the Vanyar and the Valar reside. To the west of Valimar was a green mound called Ezellohar and from this mound grew the Two Trees that lit the land. Two other cities are Alqualondë and Tirion, the respective homes of the Teleri and the Noldor. It also had an island, Tol Eressëa, just off its east coast.  Each of the Valar had their own region of the land where they resided and altered things to their desire:  Yavanna, the Vala of nature, growth, and harvest, resided in the Pastures of Yavanna in the south of the island. Oromë, the Vala of the hunt, lived in the Woods of Oromë to the north-east of the pastures. The forest was home to many creatures which Oromë could track and hunt. Nienna, the lonely Vala of sorrow and endurance, lived cut off in the far west of the island in the Halls of Nienna where she spent her days crying, looking out to sea. Just south of the Halls of Nienna and to the north of the pastures there were the Halls of Mandos. Mandos, the brother of Nienna, was the Vala of the afterlife. All inhabitants of Arda went to the Halls of Mandos should they happen to die, mortals and immortals alike although it was said that in death as in life, they were separated. Also living in the Halls of Mandos was his spouse Vairë the weaver, who wove the threads of time. To the south were situated the Gardens of Lórien, where dwelt Irmo, the Vala of dreams. And on an isle situated in the middle of the lake of Lórellin in Lórien, dwelt Irmo's wife Estë. To the north of this were the Mansions of Aulë the smith Vala who was spouse to Yavanna. In the north-east lay the Mansions of Manwë and Varda, the two most powerful Valar. To the west of them stood the Ring of Doom, and nearby the mound Ezellohar with the Two Trees of Valinor, Telperion and Laurelin.[1]  After the destruction of Númenor, the Undying Lands were removed from Arda so that Men could not reach them and only the Elves could go there by the Straight Road and in ships capable of passing out of the Spheres of the earth.  HISTORY In Year of the Valar 3450, the Spring of Arda ended when Melkor cast down the Two Lamps and destroyed the original dwelling of the Valar upon the isle of Almaren. The Valar departed from Middle-earth and settled in Aman. There they established the realm of Valinor.   The Two Trees of Valinor by Šárka Škorpíková After the destruction of the Lamps came the Years of the Trees and in Y.T. 1050 the Elves awoke.[3] At first the Elves were unwilling to heed the summons of the Valar to come to Valinor. The Vala Oromë selected three ambassadors, Ingwë, Finwë, and Elwë in 1102 who were swiftly brought to Aman and beheld the light of the Trees. These three Elven-kings persuaded many of the elves to journey to Aman. In 1132[6] the Vanyar and Noldor departed from Middle-earth upon an island that was drawn across the Sea to Aman. The third group of the Elves, the Teleri remained in Middle-earth until 1149, when many of them were brought to Aman.  The Elves who arrived to Aman in the Years of the Trees were called Amanyar or Calaquendi because they saw the light of the Two Trees. The Valar opened a cleft between the Pelóri, the Calacirya, so that the Light reached the Elves in their lands and cities, Eldamar, Tirion, Alqualondë and Tol Eressëa.  After the Exile of Feanor, the Noldor were not allowed to return to Valinor, and it was hidden from Mortal lands. The Valar heightened the Pelóri even more, fortified Calacirya and raised the Enchanted Isles in the Shadowy Seas. There were many attempts to reach the Undying Lands from Beleriand by ship, of which only Voronwë Aranwion survived it is told that maybe Tuor was, alone of the mortals, allowed to find Aman before his son Eärendil.  Eärendil was the first known navigator to succeed in passing the Isles of Enchantment, guided by the light of the Silmaril, who came to Valinor to seek the aid of the Valar against Melkor, now called Morgoth. His quest was successful and the Valar went to war again.  After the War of Wrath and the destruction of Beleriand, Aman was no more connected to Middle-earth by the Helcaraxë but could be reached by the ships of the Elves.  Soon after this, the great island of Númenor was raised out of Belegaer, far from the shores of Aman, and the Three Houses of the Edain were brought to live there. Henceforth, they were called the Dúnedain, and were blessed with many gifts by the Valar and the Elves of Tol Eressëa. The Valar feared—rightly—that the Númenóreans would seek to enter Aman to gain immortality (even though a mortal in Aman remains mortal), so they forbade them from sailing west from Númenor.  In time, and not without some corrupting help from Sauron, the Númenóreans violated the Ban of the Valar, and sailed to Aman with a great army under the command of Ar-Pharazôn the Golden. A part of the Pelóri collapsed upon this army, trapping it but not killing it. It is said that the army still lives underneath the pile of rock in the Caves of the Forgotten.  In light of this development, the land of Aman was decisively and forever isolated from the other lands. The flat Arda was cloven in two, and the rest was made round, so that a mariner sailing west along Eärendil's route would simply emerge in the far east. For the Elves, however, a Straight Road remains that peels away from the curvature of the earth and passes to Aman. A very few non-Elves are known to have passed along this road, including Frodo Baggins, Bilbo Baggins, and possibly Samwise Gamgee and Gimli.", 50]
test2[0] = test2[0].split(" ")
out2 = harness.fullJustify(test2[0], test2[1])
for o in out2:
    print(o)