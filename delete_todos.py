from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from add_todos import add_todos
from mark_completed_todo import mark_first_todo_completed
import time


def delete_completed_todos(edgeDriver):
    # Find all completed todos
    completed_todos = edgeDriver.find_elements(
        By.CSS_SELECTOR, ".todo-list li.completed")

    # Iterate over completed todos and delete them
    for todo in completed_todos:
        delete_button = todo.find_element(
            By.CSS_SELECTOR, ".delete-button")
        delete_button.click()
        time.sleep(1)


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

# Delete completed todos
delete_completed_todos(edgeDriver)

# Close the browser
edgeDriver.quit()
