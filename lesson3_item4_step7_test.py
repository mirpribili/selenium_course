import os
import pytest

@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":) \t very_important_fixture", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р \t print_smiling_faces", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        print("test_first_smiling_faces")

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        print("test_second_smiling_faces")


if __name__ == "__main__":
	os.system ("pytest " + os.path.basename(__file__) + " -s")
#  cd $HOME/selenium_course;python  ~/selenium_course/lesson3_item4_step7_test.py
'''
====================================== test session starts ======================================
platform linux -- Python 3.7.9, pytest-5.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /home/kde/selenium_course
collected 2 items                                                                               

lesson3_item4_step7_test.py ^_^ 

:-Р 

:) 

.:-Р 

.:3 



======================================= 2 passed in 0.02s =======================================
'''
