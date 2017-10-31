from libs.Routes import Routes
from components.customer.Customer_ctrl import Customer_ctrl

class Customer_routr(Routes):
    _routes = [  
                [ ['list', 'customers'], Customer_ctrl.list ],
                [ ['view', 'customer'], Customer_ctrl.view ],
                [ ['new', 'customer'], Customer_ctrl.new ]
    ]
