import uuid


class RequestTracker:

    @staticmethod
    def generate_request_id():

        return str(
            uuid.uuid4()
        )