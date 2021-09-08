import os
import time
import markdown as mdgen
from datetime import datetime
import webbrowser as browser
from blmarkdown.App import App
from blmarkdown.Flavor import Flavor

__author__ = 'Haryo Bagas Assyafah'
__copyright__ = 'Bear Au Jus - ジュースとくま @2021'
__credits__ = ['Haryo Bagas Assyafah']
__license__ = "MIT"
__version__ = "2.1"
__maintainer__ = "Haryo Bagas Assyafah"
__email__ = "haryobagasasyafah6@gmail.com"
__status__ = "Production"


class Utill:

    # Main Save Function =================================================================================================
    @ staticmethod
    def save_html(markdown, file_name=''):
        if file_name == '':
            file_name = f'{Utill.generate_filename()}-generated-html'

        # Check filename extension
        file_name = Utill.check_ext(file_name, 'html')

        # Check if preview file is exist
        if os.path.exists(file_name):
            os.remove(file_name)

        # Converting markdown to HTML
        html = Utill.get_html(markdown)

        # Writing HTML to file
        f = open(file_name, 'w', encoding='utf-8')
        f.write(html)
        f.close()

        # Collecting generated HTML path
        path = os.path.dirname(os.path.abspath('__file__')).replace(
            '\\', '/') + f'/{file_name}'

        return path

    @ staticmethod
    def save_markdown(markdown, file_name=''):
        if file_name == '':
            file_name = f'{Utill.generate_filename()}-generated-md'

        # Check filename extension
        file_name = Utill.check_ext(file_name, 'md')

        # Writing markdown to file
        f = open(file_name, 'w', encoding='utf-8')
        f.write(markdown)
        f.close()

        # Collecting generated HTML path
        path = os.path.dirname(os.path.abspath('__file__')).replace(
            '\\', '/') + f'/{file_name}'

        return path

    # Main Generator Function =================================================================================================
    @ staticmethod
    def markdown_to_html(markdown, processor=mdgen.markdown):
        return processor(markdown)

    @ staticmethod
    def compile_viewer(markdown, keep_file_on_complete=False, file_name=''):
        # Check filename extension
        if file_name == '':
            file_name = file_name = f"{App.APP_INFO['APP_NAME']}-preview.html"
        else:
            file_name = Utill.check_ext(file_name, 'html')

        # Generating and saving HTML file
        path = Utill.save_html(markdown, file_name)

        # Opening generared HTML file in default browser
        browser.open_new(path)

        if not keep_file_on_complete:
            # System sleep for a second (or generated HTML file will be deleted before its open)
            time.sleep(1)

            # Deleting generated HTML
            if os.path.exists(file_name):
                os.remove(file_name)

    @ staticmethod
    def get_html(markdown):
        output = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
{Utill.get_css()}
</style>
<title>{Utill.get_curr_date_formatted()} | {App.APP_INFO['APP_LABEL']}</title>
</head>
<body>
<div class="markdown-body ui-header"><pre>Your Generated Markdown Preview :</pre></div>
<article class="markdown-body ui-header" style="top: -100px;">
{Utill.markdown_to_html(markdown)}
</article>
<div class="markdown-body ui-data">
<pre><b># {App.APP_INFO['APP_LABEL']}</b><br>------------------------<br><a id="title_md"><a id="action_md" href="#" class="ui-link-controller" onclick="func_md()">+</a> GENERATED MARKDOWN </a><button id="copy_md" class="ui-button-contoller" onclick="copy()" style="display: none;">COPY</button><button id="download_md" class="ui-button-contoller" style="margin-right: 10px;" onclick="downloadCurrentDocument()">SAVE</button></pre>
<pre id="container_md" style="height: 10% !important; display: none;">
{markdown}
</pre>
</div>
<script type="text/javascript">
{Utill.get_js()}
</script>
</body>
</html>"""
        return output

    @staticmethod
    def get_css():
        return Flavor.get_css()

    @staticmethod
    def get_js():
        return Flavor.get_js()

    # ETC Function =================================================================================================
    @ staticmethod
    def get_curr_date():
        return datetime.today()

    @ staticmethod
    def get_curr_date_formatted():
        return Utill.get_curr_date().strftime('%d-%m-%Y %H:%M:%S')

    @ staticmethod
    def generate_filename():
        return Utill.get_curr_date().strftime('%H%M%S%d%m%Y')

    @ staticmethod
    def check_ext(param, ext):
        ext = ext.lower()

        # Adding '.' or dot if ext not contain dot. ex : 'html' or 'py' -> '.html' or '.py'
        if not ext[0] == '.':
            ext = '.' + ext

        # Adding / rewriting the extension of file
        var = param.split('.')
        if len(var) > 0:
            if var[-1] == ext[1:]:
                return param
            elif var[-1].lower() == ext[1:]:
                var[-1] = var[-1].lower()
                return '.'.join(i for i in var)
        return param + ext
