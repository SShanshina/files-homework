file_names = ['2.txt', '1.txt', '3.txt']

with open('1.txt', encoding='utf-8') as file:
    text = list()
    text.append(file.readlines())
with open('2.txt', encoding='utf-8') as file:
    text.append(file.readlines())
with open('3.txt', encoding='utf-8') as file:
    text.append(file.readlines())
    my_text = sorted(text, key=len)


def get_text(text):
    my_list_len = []
    for my_list in text:
        my_list_len.append(len(my_list))
    my_list_len = sorted(my_list_len)
    new_tuple = zip(file_names, my_list_len, my_text)
    result = []
    for file, list_len, text in new_tuple:
        my_string = ''.join(text)
        list_len = str(list_len)
        result.append(file)
        result.append(list_len)
        result.append(my_string)
        final_result = '\n'.join(result)
    return final_result


with open('4.txt', 'w', encoding='utf-8') as file:
    file.write(get_text(text))