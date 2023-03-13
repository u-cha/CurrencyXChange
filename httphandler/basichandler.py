from htmlcook.htmlcook import HtmlPage


class BasicHandler:
    __statuses = (200, 400, 404, 405, 406, 409, 500)

    def __init__(self):
        self.__status = None
        self.__data = None
        self.__content_type = None

    @classmethod
    def check_status(cls, status):
        if status in cls.__statuses:
            return True
        return False

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if self.check_status(status):
            self.__status = status
        else:
            self.__status = 404

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, content):
        self.__data = content

    @property
    def content_type(self):
        return self.__content_type

    @content_type.setter
    def content_type(self, content_type):
        self.__content_type = content_type

    def cook_html(self, route):
        html = HtmlPage(route, self.data)
        html_page = html.cook()
        return html_page


