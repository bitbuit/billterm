from components.app.App_tpl import App_tpl

class App_ctrl(object):

    @staticmethod
    def hello(params):
        App_tpl.hello()

    @staticmethod
    def exit(params):
        print('Bye!')
        quit()
        
    @staticmethod
    def help(params):
        App_tpl.help()
