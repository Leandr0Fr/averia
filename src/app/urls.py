from .routes.ping import ns_ping
from .routes.models.predict import ns_predict
from .routes.models.feedback import ns_feedback
from .routes.download import ns_download
from .routes.delete import ns_delete
from .routes.retrieve import ns_retrieve

urlpatterns = [
    ns_ping,
    ns_predict,
    ns_feedback,
    ns_download,
    ns_delete,
    ns_retrieve,
]