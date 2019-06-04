from Tools.ComfortableChange import initialize
class HomePage(object):
    def __init__(self):
        self.a=initialize().driver
    def Study(self):
        Study=self.a.find_element_by_id('com.ihimee.bwqs:id/main_tab_study')
        return Study
    def Sure(self):
        Sure=self.a.find_element_by_id('com.ihimee.bwqs:id/sure_btn')
        return Sure
