from components.app.App_tpl import App_tpl
from app.Model import Model
import os

class App_ctrl(object):

    @staticmethod
    def hello(params):
        App_tpl.hello()

    @staticmethod
    def exit(params):
        print('Bye!')
        quit()

    @staticmethod
    def db(params):
        if len(params) == 0:
            return
        
        if params[0] == 'list':
            dbs = os.listdir("./db/")
            App_tpl.list_dbs(dbs)
        elif params[0] == 'use' and len(params) == 2:
            print("Now using: " + params[1])
            Model.init(params[1])


    @staticmethod
    def help(params):
        App_tpl.help()
