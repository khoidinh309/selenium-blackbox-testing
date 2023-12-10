## Introduction
### This is a testing repository based on the Python-Selenium webdriver package that focuses on testing the set timed assignment and the set grade of an assignment on the Moodle demo website.
## Prequisite to run tests
- Install selenium package using cmd:
```bash
pip install selenium
or
pip install -r requirements.txt

```
- Install Chrome with lastest version - chrome driver is no longer needed.

## Run tests
```bash
cd soft-ware-testing-ass3
python test_runner.py
or
python3 test_runner.py
```

## Test case
- Set timed assignment 

|Id |allow_submission_date|due_date  |cutoff_date|remind_me_date|expected_result                                                    |
|---|---------------------|----------|-----------|--------------|-------------------------------------------------------------------|
|1  |20/11/2023           |21/11/2023|22/11/2023 |23/11/2023    |                                                                   |
|2  |20/11/2023           |19/11/2023|22/11/2023 |23/11/2023    |Due date must be after the allow submissions from date             |
|3  |20/11/2023           |21/11/2023|19/11/2023 |23/11/2023    |Cut-off date cannot be earlier than the allow submissions from date|
|4  |20/11/2023           |21/11/2023|22/11/2023 |19/11/2023    |Remind me to grade by date cannot be earlier than the due date     |

    A white space indicates that test-case is valid and none of error is raised.

- Set grade assignment
  
|Id |maximum_grade|grade_pass|expected_result                                                         |max_response_time|
|---|-------------|----------|------------------------------------------------------------------------|-----------------|
|1  |10           |0         |                                                                        |5                |
|2  |10           |11        |The grade to pass can not be greater than the maximum possible grade 10 |4                |
|3  |-1           |0         |Invalid grade value. This must be an integer between 1 and 100          |4                |
|4  |101          |0         |Invalid grade value. This must be an integer between 1 and 100          |4                |
|5  |100          |102       |The grade to pass can not be greater than the maximum possible grade 100|4                |
|6  |100          |-1        |                                                                        |5                |

    A white space indicates that test-case is valid and none of error is raised.

## Test results
- Set timed assignment

  |Id |Passed|
  |---|------|
  |1  |Passed|
  |2  |Passed|
  |3  |Passed|
  |4  |Passed|

- Set grade assignment
  
  |Id |UI_Passed|RT_Passed|
  |---|---------|---------|
  |1  |Passed   |Passed   |
  |2  |Passed   |Passed   |
  |3  |Passed   |Passed   |
  |4  |Passed   |Passed   |
  |5  |Passed   |Passed   |
  |6  |Passed   |Passed   |


      The results of the reponse time are not assured, it bases on the internet status.

## Conclusion
Overall, the test matches its expectations. Selenium Driver is a good tool to deploy these functional tests, but not for sure the response time test.


