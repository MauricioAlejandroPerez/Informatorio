#import random
#import string

#word = "".join([random.choice(string.ascii_lowercase) for i in range(700)])
#print(word)

word = "axyvdjmjpgubyonloeyzzssdxwodjphmhgylptpezkwfzmnygcgydpjznrraoeabvpepewdcxpgwojspuhcnwvqapdtieivaeihgutcedlkqkwjpkuqmmimxnmhbmuqitliwhhyglntpeawhzemoncgeusjsitbuogwvjewxmchqlcpiujrumazojanadytcefmzcwslwxoeeljehkjmkxzxijkpmmutjqbmigmtqrxfmaadfbnnxixlbcdenowiwuhzcyemjitkjniswinxezqrlfjfxahirgkgyyboubzhxdskipsqxshcuaqwpjygdxiaqxkbxunantpkippgeyztrbkcdzndosafxfequfpedfxsbyzgguvgroidxmblxpcpyylvkqmorgfsuvclokyhpahcooijjnsxtpothdenbriuumufbpzrkvaenjwekdojfozsrzpwhkedftbkdbmahyuwheweiudkldylfzlwuntugwxeusfdkrejtfpgvcsedmhgerqhzfeupkwhrnzxumozpgctgypwadixqtbdbtrasuryqcobsdaywabaoiysyxpcuddjldnuvycjgiyefehazeuuvshfqusaddrodwvktypqssumswqrnfmiuqbiosdrwhjrjrcflhvidfbspqszomusgwpniaattnndzrhouxgbtuojvhmd"


# {'a': 100, 'b': 2, }
res = {}
for letter in word:
    letter_key = letter
    res[letter_key] = res.get(letter_key, 0) + 1

print(res)
