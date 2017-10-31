from libs.Routes import Routes
from components.me.Me_ctrl import Me_ctrl

class Me_routr(Routes):
    _routes = [  
                [ ['who', 'am', 'i'], Me_ctrl.view ]
    ]
