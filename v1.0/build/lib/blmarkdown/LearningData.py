__author__ = 'Haryo Bagas Assyafah'
__copyright__ = 'Bear Au Jus - ジュースとくま @2021'
__credits__ = ['Haryo Bagas Assyafah']
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Haryo Bagas Assyafah"
__email__ = "haryobagasasyafah6@gmail.com"
__status__ = "Production"


class LearningData:

    def __init__(self, title, link=''):
        self.title = title
        self.link = link
        self.learning_data = dict()

    def add(self, subject, subject_data=list()):
        self.learning_data[subject] = subject_data
