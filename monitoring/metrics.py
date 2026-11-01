class Metrics:

    total_requests = 0

    total_latency = 0

    routed_agents = {}

    @classmethod
    def record_request(cls):

        cls.total_requests += 1

    @classmethod
    def record_agent(
        cls,
        agent
    ):

        cls.routed_agents[agent] = (
            cls.routed_agents.get(
                agent,
                0
            ) + 1
        )

    @classmethod
    def record_latency(
        cls,
        latency
    ):

        cls.total_latency += latency