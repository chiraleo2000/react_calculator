# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize WebDriver
# driver = webdriver.Chrome()
# driver.get("http://localhost:8501")  # Replace with your Streamlit app's URL

# # Example with XPath (modify as per your actual element)
# xpath = "//input[@placeholder='Enter first number']"  # Adjust the XPath as per the actual element
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
# first_number = driver.find_element(By.XPATH, xpath)

# # Function to test basic calculations
# def test_basic_operation(num1, num2, operation, expected_result):
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.__name__, "Enter first number for basic operations")))
#     # Clear and enter first number
#     first_number = driver.find_element(By.CSS_SELECTOR, "Enter first number for basic operations")
#     first_number.clear()
#     first_number.send_keys(str(num1))

#     # Clear and enter second number
#     second_number = driver.find_element(By.CSS_SELECTOR, "Enter second number for basic operations")
#     second_number.clear()
#     second_number.send_keys(str(num2))

#     # Select operation
#     operation_select = driver.find_element(By.CSS_SELECTOR, "Select Basic Operation")
#     operation_select.send_keys(operation)

#     # Click calculate button
#     calculate_button = driver.find_element(By.CSS_SELECTOR, "//button[text()='Calculate Basic Operation']")
#     calculate_button.click()

#     # Wait for result and check
#     time.sleep(2)
#     result = driver.find_element(By.NAME, "Basic Operation Result")
#     assert str(expected_result) in result.text

# # Function to test parabolic calculations
# def test_parabolic_calculations(vertex, point, expected_result):
#     # Clear and enter vertex
#     vertex_input = driver.find_element(By.CSS_SELECTOR,"vertex_input")  # Adjust the element selector as per your app
#     vertex_input.clear()
#     vertex_input.send_keys(vertex)

#     # Clear and enter point
#     point_input = driver.find_element(By.CSS_SELECTOR,"point_input")  # Adjust the element selector as per your app
#     point_input.clear()
#     point_input.send_keys(point)

#     # Click calculate button
#     calculate_button = driver.find_element(By.CSS_SELECTOR,"calculate_parabola_button")  # Adjust the selector as per your app
#     calculate_button.click()

#     # Wait for result and check
#     time.sleep(2)
#     result = driver.find_element(By.CSS_SELECTOR,"parabola_result")  # Adjust the selector as per your app
#     assert expected_result in result.text

# # Function to test area calculations
# def test_area_calculations(shape, dimensions, expected_result):
#     # Select shape
#     shape_select = driver.find_element(By.CSS_SELECTOR,"shape_select")  # Adjust the element selector as per your app
#     shape_select.send_keys(shape)

#     # Enter dimensions
#     dimensions_input = driver.find_element(By.CSS_SELECTOR,"dimensions_input")  # Adjust the element selector as per your app
#     dimensions_input.clear()
#     dimensions_input.send_keys(dimensions)

#     # Click calculate button
#     calculate_area_button = driver.find_element(By.CSS_SELECTOR,"calculate_area_button")  # Adjust the selector as per your app
#     calculate_area_button.click()

#     # Wait for result and check
#     time.sleep(2)
#     area_result = driver.find_element(By.CSS_SELECTOR,"area_result")  # Adjust the selector as per your app
#     assert expected_result in area_result.text

# # Function to test volume calculations
# def test_volume_calculations(object_type, dimensions, expected_result):
#     # Select object type
#     object_type_select = driver.find_element(By.CSS_SELECTOR,"object_type_select")  # Adjust the element selector as per your app
#     object_type_select.send_keys(object_type)

#     # Enter dimensions
#     dimensions_input = driver.find_element(By.CSS_SELECTOR,"dimensions_input")  # Adjust the element selector as per your app
#     dimensions_input.clear()
#     dimensions_input.send_keys(dimensions)

#     # Click calculate button
#     calculate_volume_button = driver.find_element(By.CSS_SELECTOR,"calculate_volume_button")  # Adjust the selector as per your app
#     calculate_volume_button.click()

#     # Wait for result and check
#     time.sleep(2)
#     volume_result = driver.find_element("volume_result")  # Adjust the selector as per your app
#     assert expected_result in volume_result.text


# # Test cases for basic operations
# test_basic_operation(10, 5, "Add", 15)
# test_basic_operation(10, 5, "Subtract", 5)
# test_basic_operation(10, 5, "Multiply", 50.0)
# test_basic_operation(10, 5, "Divide", 2.0)
# test_basic_operation(10, 0, "Divide", "Cannot divide by zero")

# # Test cases for parabolic calculations
# test_parabolic_calculations("(0,0)", "(2,4)", "y = 1.0(x - 0)^2 + 0")
# test_parabolic_calculations("(1,2)", "(3,10)", "y = 2.0(x - 1)^2 + 2")

# # Test cases for area calculations
# test_area_calculations("Circle", "3", "Area of Circle: 28.27")
# test_area_calculations("Circle", "4", "Area of Circle: 50.27")
# test_area_calculations("Circle", "5", "Area of Circle: 78.54")
# test_area_calculations("Square", "5", "Area of Square: 25.0")
# test_area_calculations("Square", "6", "Area of Square: 36.0")
# test_area_calculations("Rectangle", "5,4", "Area of Rectangle: 20.0")
# test_area_calculations("Rectangle", "8,7", "Area of Rectangle: 56.0")
# # Test cases for volume calculations
# test_volume_calculations("Sphere", "3", "Volume of Sphere: 113.1")
# test_volume_calculations("Sphere", "4", "Volume of Sphere: 268.08")
# test_volume_calculations("Cube", "5", "Volume of Sphere: 125.0")
# test_volume_calculations("Cube", "6", "Volume of Sphere: 216.0")

# # Close WebDriver
# driver.close()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("http://localhost:3000")  # Update this URL to your React app's URL

# Utility function to find element and send keys
def send_keys(driver, selector, keys):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    element.clear()
    element.send_keys(keys)

# Function to test basic calculations
def test_basic_operation(num1, num2, operation, expected_result):
    # Select the Basic Calculator tab
    driver.find_element(By.XPATH, "//button[text()='Basic Calculator']").click()

    send_keys(driver, "[placeholder='First Number']", num1)
    send_keys(driver, "[placeholder='Second Number']", num2)

    # Select operation
    operation_select = driver.find_element(By.CSS_SELECTOR, "select")
    operation_select.send_keys(operation)

    # Click calculate button
    driver.find_element(By.XPATH, "//button[text()='Calculate']").click()

    # Wait for result and check
    time.sleep(2)
    result = driver.find_element(By.CSS_SELECTOR, "p").text
    assert str(expected_result) in result

# Function to test parabolic calculations
def test_parabolic_calculations(vertex, point, expected_result):
    # Select the Parabolic Calculator tab
    driver.find_element(By.XPATH, "//button[text()='Parabolic Calculator']").click()

    send_keys(driver, "[placeholder='Enter vertex (h,k)']", vertex)
    send_keys(driver, "[placeholder='Enter a point (x,y)']", point)

    # Click calculate button
    driver.find_element(By.XPATH, "//button[text()='Calculate']").click()

    # Wait for result and check
    time.sleep(2)
    result = driver.find_element(By.CSS_SELECTOR, "p").text
    assert expected_result in result

# Function to test area calculations
def test_area_calculations(shape, dimensions, expected_result):
    # Select the Area Calculator tab
    driver.find_element(By.XPATH, "//button[text()='Area Calculator']").click()

    # Select shape
    shape_select = driver.find_element(By.CSS_SELECTOR, "select")
    shape_select.send_keys(shape)

    # Enter dimensions
    send_keys(driver, "[placeholder='Enter dimensions']", dimensions)

    # Click calculate button
    driver.find_element(By.XPATH, "//button[text()='Calculate']").click()

    # Wait for result and check
    time.sleep(2)
    result = driver.find_element(By.CSS_SELECTOR, "p").text
    assert expected_result in result

# Function to test volume calculations
def test_volume_calculations(object_type, dimensions, expected_result):
    # Select the Volume Calculator tab
    driver.find_element(By.XPATH, "//button[text()='Volume Calculator']").click()

    # Select object type
    object_type_select = driver.find_element(By.CSS_SELECTOR, "select")
    object_type_select.send_keys(object_type)

    # Enter dimensions
    send_keys(driver, "[placeholder='Enter dimensions']", dimensions)

    # Click calculate button
    driver.find_element(By.XPATH, "//button[text()='Calculate']").click()

    # Wait for result and check
    time.sleep(2)
    result = driver.find_element(By.CSS_SELECTOR, "p").text
    assert expected_result in result

# Test cases for basic operations
test_basic_operation(10, 5, "Add", "Result: 15")
test_basic_operation(10, 5, "Subtract", "Result: 5")
test_basic_operation(10, 5, "Multiply", "Result: 50")
test_basic_operation(10, 5, "Divide", "Result: 2")
test_basic_operation(10, 0, "Divide", "Result: Cannot divide by zero")

# Test cases for parabolic calculations
test_parabolic_calculations("0,0", "2,4", "Parabolic equation: y = 1(x - 0)^2 + 0")
test_parabolic_calculations("1,2", "3,10", "Parabolic equation: y = 2(x - 1)^2 + 2")

# Test cases for area calculations
test_area_calculations("Circle", "3", "Area of Circle: 28.27")
test_area_calculations("Square", "4", "Area of Square: 16.0")
test_area_calculations("Rectangle", "5,3", "Area of Rectangle: 15.0")

# Test cases for volume calculations
test_volume_calculations("Sphere", "3", "Volume of Sphere: 113.1")
test_volume_calculations("Cube", "4", "Volume of Cube: 64.0")

# Close WebDriver
driver.quit()