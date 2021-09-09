from datetime import date
from blmarkdown.Utill import Utill
from blmarkdown.App import App
from blmarkdown.LearningData import LearningData

__author__ = 'Haryo Bagas Assyafah'
__copyright__ = 'Bear Au Jus - ジュースとくま @2021'
__credits__ = ['Haryo Bagas Assyafah']
__license__ = "MIT"
__version__ = "2.2"
__maintainer__ = "Haryo Bagas Assyafah"
__email__ = "haryobagasasyafah6@gmail.com"
__status__ = "Production"


class Learning:

    def __init__(self, learning_subject_title, credit_name, footer_data=dict()):
        self.learning_subject_title = learning_subject_title
        self.credit_name = credit_name
        self.footer_data = footer_data
        self.data = list()

    def __generate(self):
        # Header Data
        output = f'# Learning : {self.learning_subject_title}\n\n'

        # Body Data
        for idx, learning_data in enumerate(self.data):
            idx += 1
            output += f"### Learning {('0' + str(idx)) if idx < 10 else str(idx)} - {learning_data.title}\n"
            if not learning_data.link == '':
                output += f'> Shortcut : [Link]({learning_data.link})\n\n'

            model = learning_data.learning_data
            for child_key in model:
                output += f'+ {child_key}\n'
                if model[child_key]:
                    for subject_data in model[child_key]:
                        output += f'    - {subject_data}\n'
            output += '\n---\n'

        # Footer Data
        if not self.footer_data:
            output += f"**{self.credit_name}** @{date.today().year} | Generated by [{App.APP_INFO['APP_NAME']}]({App.APP_INFO['APP_URL']}) {App.APP_INFO['APP_VERSION']}"
        else:
            output += '# Credit\n'
            for i in self.footer_data:
                output += f'+ {i} : {self.footer_data[i]}\n'
            output += f"\n**{self.credit_name}** @{date.today().year} | Generated by [{App.APP_INFO['APP_NAME']}]({App.APP_INFO['APP_URL']}) {App.APP_INFO['APP_VERSION']}"

        return output

    def add(self, child):
        if isinstance(child, str):
            self.data.append(LearningData(child))
        elif isinstance(child, list):
            tmp = list()
            for data in child:
                if isinstance(data, LearningData):
                    tmp.append(data)
                elif isinstance(data, str):
                    tmp.append(LearningData(data))
                else:
                    raise Exception(
                        "data inside a list must an instance of 'LearningData' or 'str'")
            self.data = self.data + tmp
        elif isinstance(child, LearningData):
            self.data.append(child)
        else:
            raise Exception(
                "'child' must an instance of 'LearningData' or 'str' or 'list'")

    def preview(self, keep_file_on_complete=False, file_name=''):
        Utill.compile_viewer(self.__generate(),
                             keep_file_on_complete, file_name)

    def save_markdown(self, file_name=''):
        return Utill.save_markdown(self.__generate(), file_name)

    def get_markdown(self):
        return self.__generate()

    def markdown(self):
        print(self.__generate())

    def get_child(self, index):
        return self.data[index]

    def index(self):
        if not self.data:
            return {}
        else:
            return {idx: learning_data.title for idx, learning_data in enumerate(self.data)}

    def __str__(self) -> str:
        return self.__generate()

    def __repr__(self) -> str:
        return self.__generate()
