class KnowledgeBaseHealth:

    missing_topics = []

    @classmethod
    def record_missing_topic(
        cls,
        question
    ):

        cls.missing_topics.append(
            question
        )

    @classmethod
    def print_kb_health(cls):
        print(
            "\n=== Knowledge Base Health ==="
        )
        for topic in (
            KnowledgeBaseHealth
            .missing_topics
        ):
            print(
                f"- {topic}"
            )