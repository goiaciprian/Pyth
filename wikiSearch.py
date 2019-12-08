
import tkinter as tk
from tkinter import ttk
from pprint import pprint
from urllib.request import urlopen
from urllib.error import URLError
from json import loads
from re import split

# debuging purpose
from pdb import set_trace

__version__ = '0.0.2a'


class NotStringError(Exception):
    """ Error raised when the language is set to an integer
    :param message: The message that will be shown
    :type message: string
    """
    _message_ = "The input of the language method should be a string.(argv 2)"

    def __init__(self, message: str = None, *args):
        if message:
            self.message = message
        else:
            self.message = self._message_
        super(NotStringError, self).__init__(self.message)


class NothingToSearchError(Exception):
    '''Error raised when no search word
    :param message: The message that will be shown
    :type message: str
    '''
    _message_ = "You must introduce an word."

    def __init__(self, message: str = None, *args):
        if message:
            self.message = message
        else:
            self.message = self._message_
        super(NothingToSearchError, self).__init__(self.message)


class WikiAnswer(object):
    '''
        Gets all the pages from wikipedia based on a user input

        :param searchWord: The word or words that are searhed in databse
        :param lang: Set the language

        :type searchWord: string
        :type lang: string

        :raise NotStringError: If lang is an integer
        :raise NothingToSearchError: If there's not an search word

        :return: List of tuples with name of the page and it's link
        :rtype: List

        '''

    def __init__(self, searchWord: str = None, lang: str = "ro"):

        self._searchWord = searchWord
        self.classCreation = searchWord
        self._lang = lang
        self._finalSearch = ""
        self.__api__ = ""
        self._data = ""

    @property
    def classword(self):
        ''' :return: The optional input at the creation of the class
            :rtype: str
        '''
        return self.classCreation

    @property
    def pprintData(self):
        ''' Show the row answer from wikipedia
            :return: An array with titles, links and paragraphs about
                the search word
            :rtype: list
        '''
        if self._data:
            return self._data
        else:
            print('No data yet.')

    @property
    def language(self):
        ''' Show the current search language
            :return: The current searching language
            :rtype: str
        '''
        return self._lang

    @ language.setter
    def language(self, newLang: str):
        ''' Set the searching language
            :param newLang: Set the new searching language
            :type newLang: str
        '''
        if type(newLang) == str:
            self._lang = newLang
        else:
            raise NotStringError()

    def searchWiki(self, searchWord2: str = None, debug: bool = False):
        '''Function that iterate through the wikipedia database
           :param searchWord2: Substitute for the class parameter _searchWord
           :type searchWord2: str
           :param debug: If true the function will print the finished list
           :type deubg: bool
           :return: A list of tuples with two elements: Title and link
           :rtype: list
        '''
        # set_trace()
        if searchWord2:
            self._searchWord = searchWord2
        elif not self._searchWord:
            raise NothingToSearchError
        elif searchWord2 == '':
            raise NothingToSearchError
        wordList = []
        self._finalSearch = ''
        wordList = self._searchWord.split()
        for i in wordList:
            self._finalSearch = self._finalSearch + "_" + i
        self.__api__ = f"https://{self._lang}.wikipedia.org/w/api.php?action=opensearch&search={self._finalSearch[1::]}"
        try:
            urldata = urlopen(self.__api__).read().decode('utf-8')
        except URLError as e:
            print(e)
            raise NotStringError
        data = loads(urldata)
        self._data = data
        tupleList = []
        for y, x in enumerate(data[3]):
            tupleList.append((data[1][y], x))

        if debug:
            print('\n')
            pprint(tupleList)
            print('\n')
        return tupleList


class MainApp(tk.Tk):
    '''GUI
    '''

    _bgAPP = WikiAnswer()
    _existentLabels = False
    _labels = []

    def _logic(self, x: str):
        ''' The logic behind the answer frame
            :param x: Asign the user entry to the searchWord param
            :type x: str
        '''
        # set_trace()
        self.finishedAnswer = self._bgAPP.searchWiki(x, True)
        numbers = len(self.finishedAnswer) - 1

        if self._existentLabels:
            # answerFrame.destroy()
            self._existentLabels = False

        for x, i in enumerate(self.finishedAnswer):
            name = 'text' + str(x)
            self._labels.append(name)
            name = tk.Label(canvas, text=i)
            name.pack()
            if x == numbers:
                self._existentLabels = True

    def __init__(self):
        tk.Tk.__init__(self)
        self.finishedAnswer = None
        self.config(background='white')
        self.geometry('{}x{}+{}+{}'.format(680, 450, 320, 150))
        self.resizable(False, False)

        # Top of the window, the search part
        searchFrame = tk.Frame(self, background='white')
        searchFrame.pack(fill=tk.X, side=tk.TOP, ipady=25)

        # Before the canvas
        beforeCanvas = tk.Frame(self, background='white')
        beforeCanvas.pack(fill=tk.BOTH, side=tk.BOTTOM)

        # The canvas
        global canvas
        canvas = tk.Canvas(beforeCanvas, scrollregion=(0, 0, 500, 500))
        vbar = tk.Scrollbar(beforeCanvas, orient=tk.VERTICAL)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        vbar.config(command=canvas.yview)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=tk.LEFT, expand=tk.TRUE, fill=tk.BOTH)

        # Bottom part of the window, the part where the answers are shown
        # global answerFrame
        # answerFrame = tk.Frame(canvas, background='white')
        # answerFrame.pack(fill=tk.X, side=tk.BOTTOM)

        # Widgets for the top
        SPACELABEL = tk.Label(searchFrame, text=' ' * 29, background='white')
        SPACELABEL.pack(side=tk.LEFT, padx=25)

        searchLabel = tk.Label(
            searchFrame,
            text='Search: ',
            font=('Halvatica', 13, 'bold'),
            background='white'
        )
        searchLabel.pack(side=tk.LEFT, padx=10)

        searchEntry = ttk.Entry(searchFrame, width=35)
        searchEntry.bind('<Return>', lambda x: self._logic(searchEntry.get()))
        searchEntry.focus_set()
        searchEntry.pack(side=tk.LEFT)

        searchButton = ttk.Button(
            searchFrame,
            text='Search',
            command=lambda: self._logic(searchEntry.get())
        )
        searchButton.pack(side=tk.LEFT, padx=15)

    def start(self):
        '''Initilize the main loop
        '''
        self.mainloop()


if __name__ == "__main__":
    app = MainApp().start()
