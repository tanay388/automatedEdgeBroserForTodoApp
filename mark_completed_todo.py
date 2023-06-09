from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from add_todos import add_todos
import time


def mark_first_todo_completed(edgeDriver):
    # Locate the first todo in the list
    first_todo = edgeDriver.find_element(
        By.CSS_SELECTOR, ".todo-list li:first-child")

    # Click the checkbox button to mark it as completed
    checkbox_button = first_todo.find_element(
        By.CSS_SELECTOR, ".checkbox-button")
    checkbox_button.click()

    # Add time delay for ralistic effect
    time.sleep(2)


# Create the Edge Driver service
edgeService = Service(
    r"D:\\Lambdatest Tools\\edgedriver_win64\\msedgedriver.exe")

# Create the Edge WebDriver
edgeDriver = webdriver.Edge(service=edgeService)

# Open the Todo app
edgeDriver.get("https://tanay-deo.web.app/todo")

# Add todos
add_todos(edgeDriver)

# Mark first todo as completed
mark_first_todo_completed(edgeDriver)

# Close the browser
edgeDriver.quit()
