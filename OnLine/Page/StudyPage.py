from Tools.ComfortableChange import initialize
class StudyPage(object):
    def __init__(self):
        self.a=initialize().driver
    def SelectClass(self):
        SelectClass=self.a.find_elements_by_id('com.ihimee.bwqs:id/title_view')[1]
        return SelectClass
    def SelectClassHour(self):
        SelectClassHour=self.a.find_elements_by_class_name('android.widget.RelativeLayout')[9]
        return SelectClassHour
