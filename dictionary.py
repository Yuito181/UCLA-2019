dictionary = {
    "wanker":"jerk",
    "knackered":"tired",
    "chuffed":"pleased"
}
print(dictionary["wanker"])
print(dictionary["knackered"])
print(dictionary["chuffed"])

sentence = "I am totally chuffed"
wordlist = sentence.split(" ")
print(wordlist)

for word in wordlist:
    if word in dictionary:
        print(dictionary[word])