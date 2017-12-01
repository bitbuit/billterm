from libs.Screen import *

class App_tpl(object):

    @staticmethod
    def hello():
        print("   _    _ _ _ _                             ")
        print("  | |__(_) | | |_ ___ _ _ _ __              ")
        print("  | '_ \ | | |  _/ -_) '_| '  \             ")
        print("__|_.__/_|_|_|\__\___|_| |_|_|_|_H_e_l_l_o_!")
        print("  ~ Write " + Text_style.BOLD + "help" + Text_style.END_STYLE + " if you are lost :$")        

    @staticmethod
    def help():
        print('helping people!')
