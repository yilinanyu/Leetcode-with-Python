def topk(word_list, k):
	
	word_counter = {}
	for word in word_list:
		if word in word_counter:
			word_counter[word] += 1
		else:
		    word_counter[word] = 1
	popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
	top_k = popular_words[:k]
	return top_k
word_list = ['Jellicle', 'Cats', 'are', 'black', 'and', 'white,', 'Jellicle', 'Cats', 'are', 'rather', 'small;', 'Jellicle', 'Cats', 'are', 'merry', 'and', 'bright,', 'And', 'pleasant', 'to', 'hear', 'when', 'they', 'caterwaul.', 'Jellicle', 'Cats', 'have', 'cheerful', 'faces,', 'Jellicle', 'Cats', 'have', 'bright', 'black', 'eyes;', 'They', 'like', 'to', 'practise', 'their', 'airs', 'and', 'graces', 'And', 'wait', 'for', 'the', 'Jellicle', 'Moon', 'to', 'rise.', '']
print topk(word_list, 3)