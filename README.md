# automations

This repo has basic templates automation demo projects.

AppiumPython

This is an appium-python automation which runs against comiXology android app https://play.google.com/store/apps/details?id=com.iconology.comics&hl=es_419

Following the "page model object" pattern, there is a folder /mobil which has an .py file representing each page needed in the test cases. Plus, there is a test in /test/mobil/promos_codes.py which have 2 test cases:
1. The first one test one commic be added to the cart.
2. The second one test an invalid promo code.
Of  course each test has at least one assert.

To run the automation:
1. Adjust the property deviceName in /commons/test_data.json, for an already existing device in your enviroment.
2. Run appium server in port 4723
3. Run the file /tests/mobil/promos_codes.py
