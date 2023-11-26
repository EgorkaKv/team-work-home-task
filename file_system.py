class File:
    
    def __init__(self, name, extension, size, place='Desktop/'):
        self.name = name
        self.extension = extension
        self.size = size
        self.place = place

    def replace(self, new):
        self.place = new


class Folder:
    
    def __init__(self, name, fold_list=[], file_list=[], place='Desktop/'):
        self.name = name
        self.folders = fold_list
        self.files = file_list
        self.place = place
        self.replace()

    def replace(self, new='Desktop/'):
        self.place = new
        for i in self.folders:
            i.replace(self.place + self.name + '/')
        for i in self.files:
            i.replace(self.place + self.name)


def path(top='', tab=0):
    s = '    '
    tab = len(top.place.split('/'))-2
    print(s*tab + top.name + ':')
    for i in top.folders:
        path(top=i)
    for i in top.files:
        print(s*(tab+1) + i.name)


'''def test_pop():
    assert (1, 2, 3) == (2, 1, 3)'''


if __name__ == '__main__':
    test = File('test', 'py', 100)
    exam = File('exam', 'exe', 2354)
    pak = File('pak', 'txt', 10)

    tet = Folder('tet', [], [pak])
    pit = Folder('pit', [tet], [test])
    laba = Folder('laba', [pit], [exam])

    path(top=laba)
