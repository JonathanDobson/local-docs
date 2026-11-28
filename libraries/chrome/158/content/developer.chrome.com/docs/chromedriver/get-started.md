# Get started with ChromeDriver

This page documents how to start using ChromeDriver for testing your website on
desktop (Windows/Mac/Linux). You can also read
[Getting Started with Android](https://developer.chrome.com/docs/chromedriver/get-started/android) or
[Getting Started with ChromeOS](https://developer.chrome.com/docs/chromedriver/get-started/chromeos).

## Setup

ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome. It is maintained by the Chromium team with help from WebDriver contributors. If you are unfamiliar with Selenium WebDriver, you should check out the [Selenium site](https://www.selenium.dev/).

Follow these steps to setup your tests for running with ChromeDriver:

- Ensure Chromium and Google Chrome are installed in a recognized location.
  - ChromeDriver expects you to have Chrome installed in the default location for your platform. You can [force ChromeDriver to use a custom location](https://developer.chrome.com/docs/chromedriver/capabilities) by setting a special capability.
- [Download the ChromeDriver binary](https://googlechromelabs.github.io/chrome-for-testing/) for your platform.
- Help WebDriver find the downloaded ChromeDriver executable.

Any of these steps should work:

1. Include the ChromeDriver location in your PATH environment variable
2. (*Java only* ) Specify its location using the `webdriver.chrome.driver` system property (see sample below)
3. (*Python only* ) Include the path to ChromeDriver when instantiating `webdriver.Chrome`. See the following samples.

### Sample Java test

    import org.openqa.selenium.*;
    import org.openqa.selenium.chrome.*;
    import org.junit.Test;
    public class GettingStarted {   
    @Test   
    public void testGoogleSearch() throws InterruptedException {
      // Optional. If not specified, WebDriver searches the PATH for chromedriver.
      // System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
      // WebDriver driver = new ChromeDriver();
      driver.get("http://www.google.com/"); 
      Thread.sleep(5000);  // Let the user actually see something!
      WebElement searchBox = driver.findElement(By.name("q"));
      searchBox.sendKeys("ChromeDriver");
      searchBox.submit(); 
      Thread.sleep(5000);  // Let the user actually see something!
      driver.quit();  
     }
    }

### Sample Python test

    import time
    from selenium import webdriver

    driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/')
    time.sleep(5) # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5) # Let the user actually see something!
    driver.quit()

### Control ChromeDriver's lifetime

The ChromeDriver class starts the ChromeDriver server process at creation and
terminates it when quit is called. This can waste a significant amount of time
for large test suites where a ChromeDriver instance is created per test. There
are two options to remedy this, ChromeDriverService and starting ChromeDriver
separately.

#### ChromeDriverService

Use the ChromeDriverService. This is available for most languages and lets you start or stop the ChromeDriver server yourself. Here's a Java example, with JUnit 4:  

    import java.io.*;
    import org.junit.*;
    import org.openqa.selenium.*;
    import org.openqa.selenium.chrome.*;
    import org.openqa.selenium.remote.*;
    public class GettingStartedWithService {
      private static ChromeDriverService service;
      private WebDriver driver;
      @BeforeClass
      public static void createAndStartService() throws IOException {
          service = new ChromeDriverService.Builder()
                  .usingDriverExecutable(new File("/path/to/chromedriver"))
                  .usingAnyFreePort()
                  .build();
          service.start();
      }
      
      @AfterClass   
      public static void stopService() {
        service.stop();
      }

      @Before   
      public void createDriver() {
        driver = new RemoteWebDriver(service.getUrl(), new ChromeOptions());
      }

      @After   public void quitDriver() {
        driver.quit();
      }

      @Test   
      public void testGoogleSearch() {
        driver.get("http://www.google.com");
        // rest of the test...
      }
    }

Python:  

    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    service = Service('/path/to/chromedriver')
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get('http://www.google.com/');
    time.sleep(5) # Let the user actually see something!
    driver.quit()

#### Start ChromeDriver separately

Start the ChromeDriver server separately before running your tests, and connect
to it using the Remote WebDriver.

Terminal:  

    $ ./chromedriver
    Starting ChromeDriver
    76.0.3809.68 (...) on port 9515
    ...

Java:  

    import java.net.*;
    import org.openqa.selenium.*;
    import org.openqa.selenium.chrome.*;
    import org.openqa.selenium.remote.*;  

    public class GettingStartedRemote {

      public static void main(String[] args) throws MalformedURLException {
        WebDriver driver = new RemoteWebDriver(
            new URL("http://127.0.0.1:9515"),
            new ChromeOptions());
        driver.get("http://www.google.com");
        driver.quit();
      }
    }