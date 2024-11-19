"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 
    'a', 'the', 'time', 'to', 'who', '🐈', '👧', 'and', 'went', 
    'had', 'play', '⚽.', 'they']

story = [words[0], words[2], words[7], words[9], words[7], 
        words[1], words[15], words[10], words[8], words[4], 
        words[10], words[17], words[6], words[8], words[3]] 

# Create a story using the words in the list
##print('[:]', nums[::])
# Display the story to the user
print(' '.join(story))