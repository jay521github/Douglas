from Tools.ComfortableChange import initialize
class Bake(object):
    def __init__(self):
        self.a=initialize().driver
    def Bake(self):
        Bake=self.a.find_element_by_id('com.ihimee.bwqs:id/topbar_left_view_btn')
        return Bake