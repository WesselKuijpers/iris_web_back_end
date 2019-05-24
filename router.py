from controllers.insight_controller import insight_controller
from controllers.predict_controller import predict_controller

# class containing methods for registering th router
class Router:
    # method for registering the blueprints of the controllers
    def register(self):
        # import the app context, is done locally so that an importerror is not raised
        from main import app

        # register all the required functional blueprints pointing to the controllers
        # TODO: find some way to do this dynamically
        app.register_blueprint(predict_controller, url_prefix="/predict")
        app.register_blueprint(insight_controller, url_prefix='/insight')
