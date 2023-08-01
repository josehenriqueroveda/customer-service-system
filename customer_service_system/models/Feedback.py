class Feedback:
    def __init__(
        self,
        feedback_id,
        customer_id,
        feedback_type,
        feedback_grade,
        feedback_content,
        feedback_date,
    ):
        self.feedback_id = feedback_id
        self.customer_id = customer_id
        self.feedback_type = feedback_type
        self.feedback_grade = feedback_grade
        self.feedback_content = feedback_content
        self.feedback_date = feedback_date
