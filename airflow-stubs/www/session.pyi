import flask.sessions
import flask_session.sessions

class SessionExemptMixin:
    def save_session(self, *args, **kwargs): ...

class AirflowDatabaseSessionInterface(SessionExemptMixin, flask_session.sessions.SqlAlchemySessionInterface): ...
class AirflowSecureCookieSessionInterface(SessionExemptMixin, flask.sessions.SecureCookieSessionInterface): ...
