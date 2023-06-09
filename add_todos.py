from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time


def add_todos(edgeDriver):
    # Add todos one by one
    todos = ["Buy groceries", "Finish homework", "Go for a run"]
    for todo in todos:
        # Find the input field
        input_field = edgeDriver.find_element(
            By.CSS_SELECTOR, ".add-todo input[type='text']")

        # Enter the todo text
        input_field.send_keys(todo)

        # Introduce a delay for a realistic effect
        time.sleep(1)

        # Find the "Add Todo" button and click it
        add_button = edgeDriver.find_element(
            By.CSS_SELECTOR, ".add-todo button")
        add_button.click()

        # Introduce a delay for a realistic effect
        time.sleep(1)


# Create the Edge Driver service
edgeService = Service(
    r"D:\\Lambdatest Tools\\edgedriver_win64\\msedgedriver.exe")

# Create the Edge WebDriver
edgeDriver = webdriver.Edge(service=edgeService)

# Open the Todo app
url = "https://tanay-deo.web.app/todo"
edgeDriver.get(url)

# Call the add_todos method
add_todos(edgeDriver)

# Close the browser
edgeDriver.quit()
