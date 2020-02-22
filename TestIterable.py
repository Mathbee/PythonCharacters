# coding=utf-8
#可迭代对象Eg1
class Eg1(object):
    def __init__(self, text):
        self.text = text
        self.sub_text = text.split(' ')

    def __getitem__(self, index):
        return self.sub_text[index]

#可迭代对象Eg2
class Eg2(object):
    def __init__(self, text):
        self.text = text
        self.sub_text = text.split(' ')

    def __iter__(self):
        return Eg2Iterator(self.sub_text)

class Eg2Iterator(object):
    def __init__(self, sub_text):
        self.sub_text = sub_text
        self.index = 0
    def __next__(self):
        try:
            sub_text = self.sub_text[self.index]
        except:
            raise StopIteration()
        self.index += 1
        return sub_text
    def __iter__(self):
        return self

class Eg3(object):
    def __init__(self, text):
        self.text = text
        self.sub_text = text.split(' ')

    def __iter__(self):
        for item in self.sub_text:
            yield item

class Eg4(object):
    def __init__(self, text):
        self.text = text
        self.sub_text = text.split(' ')
    def __iter__(self):
        yield from self.sub_text


if __name__ == '__main__':
    '''
    #Eg1
    o1 = Eg1('Hello, the wonderful new world!')
    for i in o1:
        print(i)
    '''

    '''
    #Eg2
    o2 = Eg2('Hello, the wonderful new world!')
    for i in o2:
        print(i)
    '''
    '''
    o3 = Eg3('Hello, the wonderful new world!')
    for i in o3:
        print(i)
    '''

    
    o4 = Eg4('Hello, the wonderful new world!')
    for i in o4:
        print(i)
