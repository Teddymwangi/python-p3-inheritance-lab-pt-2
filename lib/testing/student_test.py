import unittest
from student import Student, ChattyStudent
from io import StringIO
import sys

class TestStudent(unittest.TestCase):
    def test_student_hello(self):
        student = Student()
        captured_output = StringIO()
        sys.stdout = captured_output
        student.hello()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hey there! I'm so excited to learn stuff.")

    def test_student_raise_hand(self):
        student = Student()
        captured_output = StringIO()
        sys.stdout = captured_output
        student.raise_hand()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Pick me!")

    def test_chatty_student_hello(self):
        chatty_student = ChattyStudent()
        captured_output = StringIO()
        sys.stdout = captured_output
        chatty_student.hello()
        sys.stdout = sys.__stdout__
        expected_output = "Hey there! I'm so excited to learn stuff.\nHow are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_chatty_student_raise_hand(self):
        chatty_student = ChattyStudent()
        captured_output = StringIO()
        sys.stdout = captured_output
        chatty_student.raise_hand()
        sys.stdout = sys.__stdout__
        expected_output = "\n".join(["Pick me!"] * 10)
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
