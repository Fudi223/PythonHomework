str = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my \hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be \let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be \an answer let it be For though they may be parted there is still a chance that they will see There will be an answer le\t it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it \be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when\ the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of \music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There wil\l be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

word_occurences = {}

for word in str.split(" "):
     if word in word_occurences:
         word_occurences[word] += 1
     else:
         word_occurences[word] = 1

for key, value in word_occurences.items():
     print(key, value)