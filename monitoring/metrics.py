class Metrics:

    total_requests = 0

    total_latency = 0

    routed_agents = {}

    agents = {}

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

    @classmethod
    def record_agent_request(
        cls,
        agent
    ):

        if agent not in cls.agents:

            cls.agents[agent] = {

                 "requests": 0,

                "latency_total": 0,

                "successes": 0,

                "failures": 0
            }

        cls.agents[agent]["requests"] += 1

    @classmethod
    def record_agent_latency(
        cls,
        agent,
        latency
    ):

        if agent not in cls.agents:

            cls.agents[agent] = {

                "requests": 0,

                "latency_total": 0,

                "successes": 0,

                "failures": 0
            }

        cls.agents[agent][
            "latency_total"
        ] += latency

    @classmethod
    def record_agent_success(
        cls,
        agent
    ):

        if agent not in cls.agents:

            cls.agents[agent] = {

                "requests": 0,

                "latency_total": 0,

                "successes": 0,

                "failures": 0
            }

        cls.agents[agent][
            "successes"
        ] += 1

    @classmethod
    def record_agent_failure(
        cls,
        agent
    ):

        if agent not in cls.agents:

            cls.agents[agent] = {

                "requests": 0,

                "latency_total": 0,

                "successes": 0,

                "failures": 0
            }

        cls.agents[agent][
            "failures"
        ] += 1