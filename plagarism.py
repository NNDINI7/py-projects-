from difflib import SequenceMatcher
with open('demo1.txt') as file1, open('demo2.txt') as file2:
    text1 = file1.read()
    text2 = file2.read()
similarity = SequenceMatcher(None, text1, text2).ratio() # Calculate similarity ratio
print(f"The plagarized content is {similarity*100}%") # Print similarity ratio as percentage

