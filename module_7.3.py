class WordsFinder:

    def __init__(self, *file_names):
        self.names = []
        for name in file_names:
            self.names.append(name)

    def get_all_words(self):

        all_words = {}
        for name in self.names:
            list_word = []
            list_ = []

            with open(name, encoding='utf-8') as file:

                for line in file:
                    line_lower = line.lower()

                    line_lower_replace = line_lower.replace(',', '')            #удаление пунктуации
                    line_lower_replace = line_lower_replace.replace('.', '')
                    line_lower_replace = line_lower_replace.replace('.=', '')
                    line_lower_replace = line_lower_replace.replace('!', '')
                    line_lower_replace = line_lower_replace.replace('?', '')
                    line_lower_replace = line_lower_replace.replace(';', '')
                    line_lower_replace = line_lower_replace.replace(':', '')
                    line_lower_replace = line_lower_replace.replace('-', '')

                    line_split = line_lower_replace.split()                                 # разделение строк по  словам
                    list_.append(line_split)

            for i in list_:                                                                 # распаковка вложенных списков
                 for y in i:
                    list_word.append(y)

            all_words[name] = list_word                                                      #добавление пары в словарь

        return all_words

    def find(self, word):
        dict_f = {}
        y = list(self.get_all_words().items())
        for i in y:
            for x in i:
                # print(x)
                if isinstance(x, str):
                    key = x
                if isinstance(x, list):
                    # print(x)
                    l_word = word.lower()
                    if l_word in x:
                        ind = x.index(l_word)
                        dict_f[key]=ind+1
        return dict_f


    def count(self, word):
        dict_c = {}
        y = list(self.get_all_words().items())
        for i in y:
            for x in i:
                # print(x)
                if isinstance(x, str):
                    key = x
                if isinstance(x, list):
                    l_word = word.lower()

                    if l_word in x:
                        count= x.count(l_word)
                        dict_c[key] = count
        return dict_c




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))










