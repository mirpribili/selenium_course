import pytest
import os

# Пометьте первый тест параметром, который в случае неожиданного прохождения теста,
# помеченного как xfail, отметит в отчете этот тест как упавший.


@pytest.mark.xfail(strict=True)  # strict=True
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False

if __name__ == "__main__":
	os.system ("pytest " + os.path.basename(__file__) + " -s")
#cd $HOME/selenium_course;python  ~/selenium_course/lesson3_item5_step6_test_xfail.py
#conda deactivate; source $HOME/enviroments/selenium_env/bin/activate; cd $HOME/selenium_course;python  ~/selenium_course/lesson3_item5_step6_test_xfail.py
