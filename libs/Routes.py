class Routes(object):
    _routes = []

    @classmethod
    def find(self, inputs):
        action = None
        params = []
        for route in self._routes:
                path = route[0]
                cmds = inputs[:len(path)]
                if cmds == path:
                    action = route[1]
                    params = inputs[len(route[0]):] if len(inputs) > len(route[0]) else []
                    break

        return (action, params)
