"""
TruBio Statics Elements
"""

class Pen_Profile():
    def __init(self):
        self.idendity = None
        self.en_description = None
        self.en_parameter = None
        self.ch_description = None
        self.ch_parameter = None

    def pen_csv_to_list(self, steam):
        """从CSV中读入Historian形式列表
        return:
        steam:<str> csv readin line
        """
        self.identity, self.en_description, self.en_parameter, self.ch_description, self.ch_parameter = steam.split(',')
