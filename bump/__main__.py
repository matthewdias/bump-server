from bump import (APP, SERVER_BIND)
from bump.routes import VIEW_FUNCTIONS


if __name__ == "__main__":
    print("in __main__")
    for route, func, opts in VIEW_FUNCTIONS:
        APP.add_url_rule(
            rule=route, endpoint=func.__name__,
            view_func=func, **opts)
    APP.run(host=SERVER_BIND[0],
            port=SERVER_BIND[1])
