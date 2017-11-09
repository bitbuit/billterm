from components.app.App_tpl import App_tpl

class App_ctrl(object):

    @staticmethod
    def exit(params):
        print('Bye!')
        quit()
        

    def help(params):
        App_tpl.help()
