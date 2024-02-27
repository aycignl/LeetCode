'''
Author: Gönül Aycı
Email: aycignl@gmail.com
License: MIT, 2024 
'''

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedbacks = set(positive_feedback)
        negative_feedbacks = set(negative_feedback)

        # Initialize all student IDs with 0 points to handle if
        # none of the feedback matches the positive or negative feedback lists
        student_points = {id: 0 for id in student_id}

        for r, feedback_str in enumerate(report):
            feedbacks = feedback_str.split()
            for f in feedbacks:
                if f in positive_feedbacks:
                    student_points[student_id[r]] += 3
                elif f in negative_feedbacks:
                    student_points[student_id[r]] -= 1

        # Sort students by points (descending) and then by student ID (ascending) to get the top K students
        top_k_students = sorted(student_points, key=lambda x: (-student_points[x], x))[:k]
        
        return top_k_students
