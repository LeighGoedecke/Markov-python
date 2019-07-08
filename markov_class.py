import sys
import random

class Markov:
    def __init__(self, txtfile):
        self.txtfile = txtfile
        self.word_list = self.__get_word_list()
        self.markov_dict = self.__create_dict()
    
    def __clean_word(self, word):
        if not self.__check_valid_word(word):
            return False
        acceptable_punctuation = [',', '.', '!', '?']
        # removing bad punctuation and special characters
        while not word[0].isalpha():
            word = word[1:]
        while  not (word[-1].isalpha() or word[-1] in acceptable_punctuation):
            word = word[:-1]
        # returning lowercase word
        return word.lower()
    
    def __check_valid_word(self, word):
        for i in word:
            if i.isalpha():
                return True
        return False

    def __get_word_list(self):
        word_list = []
        for line in self.txtfile:
            word_dump = line.split(' ')
            for word in word_dump:
                if self.__clean_word(word):
                    word_list.append(self.__clean_word(word))
        return word_list
    
    def __create_dict(self):
        markov_dict = {}
        for index, word in enumerate(self.word_list[:-1]):
            word = self.__clean_word(word)
            if not word:
                continue
            if word not in markov_dict:
                markov_dict[word] = []
            markov_dict[word].append(self.word_list[index+1])
        return markov_dict
    
    def make_sentence(self):
        final_punctuation = ['!', '?', '.']
        sentence = []
        sentence.append(random.choice(list(self.markov_dict.keys())))
        # capitalising first letter
        sentence[0] = sentence[0][:1].upper() + sentence[0][1:]
        
        while sentence[-1][-1] not in final_punctuation:
            sentence.append(random.choice(self.markov_dict[self.__clean_word(sentence[-1])]))
        return ' '.join(sentence)



def main():
    sentence_list = []
    num_sentences = int(sys.argv[2])
    my_markov = Markov(open(sys.argv[1]))
    for i in range(num_sentences):
        sentence_list.append(my_markov.make_sentence())
    print(' '.join(sentence_list))

if __name__ == '__main__':
    main()
