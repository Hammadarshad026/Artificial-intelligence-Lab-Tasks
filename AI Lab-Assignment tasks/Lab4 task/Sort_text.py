import os
os.system("cls")
class Word_sort:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def main_work(self):
        words = self.input_string.split()
        n = len(words)
        for i in range(1, n):
            key = words[i]
            j = i - 1
            while j >= 0 and words[j].lower() > key.lower():
                words[j+1] = words[j]
                j -= 1
            words[j+1] = key
        return ' '.join(words)

input_string = 'the Quick brown fox jumPs over the lazY Dog'
obj = Word_sort(input_string)
output_string = obj.main_work()
print(output_string)
