from blmarkdown.Utill import Utill
from blmarkdown.App import App

__author__ = 'Haryo Bagas Assyafah'
__copyright__ = 'Bear Au Jus - ジュースとくま @2021'
__credits__ = ['Haryo Bagas Assyafah']
__license__ = "MIT"
__version__ = "2.2"
__maintainer__ = "Haryo Bagas Assyafah"
__email__ = "haryobagasasyafah6@gmail.com"
__status__ = "Production"


class LearningData:

    def __init__(self, title, link=''):
        self.title = title
        self.link = link
        self.learning_data = dict()

    def __generate(self):
        # Header Data
        output = f'# Learning : {self.title}\n'
        output += f'> Achieved Skills :\n\n'

        # Body Data
        for child_key in self.learning_data:
            output += f'+ {child_key}\n'
            if self.learning_data[child_key]:
                for subject_data in self.learning_data[child_key]:
                    output += f'    - {subject_data}\n'

        # Footer Data
        output += f"\n---\n> Generated by [{App.APP_INFO['APP_NAME']}]({App.APP_INFO['APP_URL']}) {App.APP_INFO['APP_VERSION']}"
        return output

    def add(self, subject, subject_data=list()):
        if not isinstance(subject, str):
            raise Exception(
                "'subject' must an instance of class 'string'. Example : Loop")
        elif not isinstance(subject_data, list):
            raise Exception(
                "'subject_data' must an instance of class 'list'. Example : ['For', 'While', 'For Each']")
        else:
            self.learning_data[subject] = subject_data

    def preview(self, keep_file_on_complete=False, file_name=''):
        Utill.compile_viewer(self.__generate(),
                             keep_file_on_complete, file_name)

    def save_markdown(self, file_name=''):
        return Utill.save_markdown(self.__generate(), file_name)

    def markdown(self):
        print(self.__generate())

    def get_markdown(self):
        return self.__generate()

    def __str__(self) -> str:
        return self.__generate()

    def __repr__(self) -> str:
        return self.__generate()
