class HtmlPage:

    def __init__(self, title, body):
        self.__title = title
        self.__body = body

    def cook(self):

        html_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title></title>
</head>
<body>
<section>
<h1>{self.title}</h1>
</section>
<section>
{self.body} \n \n
</section>
</body>
</html>'''
        return html_page

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):

        self.__title = title

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):

        self.__body = body


