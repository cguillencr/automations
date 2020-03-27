# automations
This repo has a basic automation example with Appium and Python for an Android app.

## AppiumPython

### Android

This is an appium-python automation example which runs against comiXology Android app.  See  https://play.google.com/store/apps/details?id=com.iconology.comics&hl=es_419

Following the "page model object" pattern, there is a folder /mobil which has an .py file representing each page needed in the test cases. Plus, there is a test in /test/mobil/promos_codes.py which has 2 test cases:

- The first one tests one comic being added to the cart.
- The second one tests an invalid promo code. 

Of course each test has at least one assert.

To run the automation:

1. Adjust the property deviceName in /commons/test_data.json, for an already existing device in your environment.
2. Run Appium server in port 4723
3. Run the file /tests/mobil/promos_codes.py

Checkout how the automation looks in https://youtu.be/MDTomLnQIvA

### IOs

This is an appium-python automation example which runs against an IOs application.

Following the "page model object" pattern, there is a folder /mobil/ios which has an .py file representing each page needed in the test cases. Plus, there is a test in /test/mobil/ios/test_nav_flow.py.

To run the automation:

1. Adjust the property deviceName in /commons/test_data.json, for an already existing device in your environment.
2. Run Appium server in port 4723
3. Run the file /tests/ios/test_nav_flow.py

Checkout how the automation looks in https://youtu.be/x-7bsxBC6ng

