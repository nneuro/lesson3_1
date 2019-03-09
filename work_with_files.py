with open('referat.txt', 'r', encoding='utf-8') as referat:
    content = referat.read()
    print(len(content))
    word_list = content.split()
    print(len(word_list))
    content_with_marks = content.replace('.', '!')
    
with open('referat2.txt', 'w', encoding='utf-8') as referat2:
    referat2.write(content_with_marks)