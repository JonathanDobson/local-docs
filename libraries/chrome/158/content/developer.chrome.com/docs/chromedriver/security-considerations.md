# Security considerations

ChromeDriver is a powerful tool, and it can cause harm when in the wrong hands.
While using ChromeDriver, follow these suggestions:

- By default, ChromeDriver only allows local connections. If you need to connect to it from a remote host, use `--allowed-ips` switch on the command line to specify a list of IP addresses that are allowed to connect to ChromeDriver.
- Run ChromeDriver with a test account that has no access to sensitive local or network data. ChromeDriver should never be run with a privileged account.
- Run ChromeDriver in a protected environment, such as Docker or virtual machine.
- Use firewall to prevent unauthorized remote connection to ChromeDriver.
- If you are using ChromeDriver through third-party tools, such as Selenium Server, protect the network ports of those tools, too.
- Use the latest versions of ChromeDriver and Chrome.