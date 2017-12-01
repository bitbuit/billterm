from libs.Routes import Routes
from components.app.App_ctrl import App_ctrl

class App_routr(Routes):
    _routes = [  
                [ ['hello!'], App_ctrl.hello ],
                [ ['exit'], App_ctrl.exit ],
                [ ['help'], App_ctrl.help ]
    ]
