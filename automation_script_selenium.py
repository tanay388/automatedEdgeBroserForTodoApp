from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Driver Code
if __name__ == '__main__':
    # create service object
    edgeService = Service(
        r"D:\\Lambdatest Tools\\edgedriver_win64\\msedgedriver.exe")

    # create webdriver object
    edgeDriver = webdriver.Edge(service=edgeService)

    # open browser and navigate to the website
    edgeDriver.get('https://www.lambdatest.com')
