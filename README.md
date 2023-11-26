<p align="center">
    <a href="https://spyboy.in/twitter">
      <img src="https://img.shields.io/badge/-TWITTER-black?logo=twitter&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://spyboy.in/">
      <img src="https://img.shields.io/badge/-spyboy.in-black?logo=google&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://spyboy.blog/">
      <img src="https://img.shields.io/badge/-spyboy.blog-black?logo=wordpress&style=for-the-badge">
    </a>
    &nbsp;
    <a href="https://spyboy.in/Discord">
      <img src="https://img.shields.io/badge/-Discord-black?logo=discord&style=for-the-badge">
    </a>
  
</p>

<br>

<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/1141162711464550430/1152291533563891793/websecp.png" />


<h4 align="center">  Web Security Assessment Tool, Bypass 403</h4>

A cutting-edge utility designed exclusively for web security aficionados, penetration testers, and system administrators. WebSecProbe is your advanced toolkit for conducting intricate web security assessments with precision and depth. This robust tool streamlines the intricate process of scrutinizing web servers and applications, allowing you to delve into the technical nuances of web security and fortify your digital assets effectively.

<h4 align="center"> This tool is a Proof of Concept and is for Educational Purposes Only. </h4> 

---

WebSecProbe is designed to perform a series of HTTP requests to a target URL with various payloads in order to test for potential security vulnerabilities or misconfigurations. Here's a brief overview of what the code does:

- It takes user input for the target URL and the path.
- It defines a list of payloads that represent different HTTP request variations, such as URL-encoded characters, special headers, and different HTTP methods.
- It iterates through each payload and constructs a full URL by appending the payload to the target URL.
- For each constructed URL, it sends an HTTP GET request using the requests library, and it captures the response status code and content length.
- It prints the constructed URL, status code, and content length for each request, effectively showing the results of each variation's response from the target server.
- After testing all payloads, it queries the Wayback Machine (a web archive) to check if there are any archived snapshots of the target URL/path. If available, it prints the closest archived snapshot's information.

> Does This Tool Bypass 403 ?

> It doesn't directly attempt to bypass a 403 Forbidden status code. The code's purpose is more about testing the behavior of the server when different requests are made, including requests with various payloads, headers, and URL variations. While some of the payloads and headers in the code might be used in certain scenarios to test for potential security misconfigurations or weaknesses, it doesn't guarantee that it will bypass a 403 Forbidden status code.

> In summary, this code is a tool for exploring and analyzing a web server's responses to different requests, but whether or not it can bypass a 403 Forbidden status code depends on the specific configuration and security measures implemented by the target server.

<br>

<details>
  <summary>Click to expand: Payload Breakdown</summary>

  Here's a brief breakdown of the payloads:

  - **Empty String:**
    - An empty string as a payload.

  - **URL Encoding (%2e):**
    - URL encoding of a dot (.) concatenated with the path.

  - **Path with Slash (/):**
    - Path followed by a slash (/).

  - **Double Slash (//):**
    - Double slash before and after the path.

  - **Path with Current Directory (./):**
    - Current directory (./) before and after the path.

  - **Request Header (-H X-Original-URL):**
    - X-Original-URL header with the path.

  - **Request Header (-H X-Custom-IP-Authorization):**
    - X-Custom-IP-Authorization header with the IP address 127.0.0.1.

  - **Request Header (-H X-Forwarded-For):**
    - X-Forwarded-For header with the IP address http://127.0.0.1 and 127.0.0.1:80.

  - **Request Header (-H X-rewrite-url):**
    - X-rewrite-url header with the path.

  - **URL Encoding (%20 and %09):**
    - URL encoding with space (%20) and tab (%09).

  - **Query Parameter (?):**
    - Query parameter with a question mark (?).

  - **Path with HTML Extension (.html):**
    - Path with .html extension.

  - **Path with Query String (/?anything):**
    - Path followed by a query string.

  - **Fragment Identifier (#):**
    - Fragment identifier with a hash (#).

  - **POST Request Header (-H Content-Length:0 -X POST):**
    - Content-Length header set to 0 and a POST request.

  - **Wildcard (*):**
    - Wildcard after the path.

  - **Path with PHP Extension (.php):**
    - Path with .php extension.

  - **Path with JSON Extension (.json):**
    - Path with .json extension.

  - **HTTP Method (-X TRACE):**
    - TRACE HTTP method.

  - **Request Header (-H X-Host):**
    - X-Host header with the IP address 127.0.0.1.

  - **Path Traversal (..;/):**
    - Path traversal.

  - **Whitespace at the Beginning (" " + self.path):**
    - Whitespace added at the beginning of the path.

  - **Path with Semicolon (;):**
    - Semicolon added before and after the path.

  - **Path with Extra Slashes:**
    - Test for bypassing by adding extra slashes (e.g., //path).

  - **Path with URL-encoded Slash:**
    - Use URL-encoded slash to bypass (e.g., %2Fpath).

  - **Path with Double URL-encoded Slash:**
    - Use double URL-encoded slash (e.g., %252Fpath).

  - **Path with Path Parameter:**
    - Add a path parameter (e.g., /path;parameter).

  - **Path with Query Parameter in Path:**
    - Add a query parameter within the path (e.g., /path?parameter).

  - **Path with Additional Dots:**
    - Add additional dots in the path (e.g., /path/../path).

  - **Path with Unicode Encoding:**
    - Use Unicode encoding to represent characters (e.g., %u002Fpath).

  - **Path with Double URL-encoded Dot:**
    - Use double URL-encoded dot (e.g., %252E).

  - **Path with URL-encoded Null Byte:**
    - Use URL-encoded null byte (e.g., %00).

  - **Path with Hex Encoding:**
    - Use hex encoding for characters in the path (e.g., /path%2Ehtml).

  This list covers a variety of common techniques used in web security testing. However, the effectiveness of these payloads depends on the specific vulnerabilities or misconfigurations present in the target system.

</details>



---

<h4 align="center">
  OS compatibility :
  <br><br>
  <img src="https://img.shields.io/badge/Windows-05122A?style=for-the-badge&logo=windows">
  <img src="https://img.shields.io/badge/Linux-05122A?style=for-the-badge&logo=linux">
  <img src="https://img.shields.io/badge/Android-05122A?style=for-the-badge&logo=android">
  <img src="https://img.shields.io/badge/macOS-05122A?style=for-the-badge&logo=macos">
</h4>

<h4 align="center"> 
Requirements:
<br><br>
<img src="https://img.shields.io/badge/Python-05122A?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Git-05122A?style=for-the-badge&logo=git">
</h4>

### ⭔ PYPI Installation : https://pypi.org/project/WebSecProbe/
---
```
pip install WebSecProbe
```

#### How To Run On CLI:

`WebSecProbe <URL> <Path>`

Example: 
```
WebSecProbe https://example.com admin-login
```

#### Python Code
```py
from WebSecProbe.main import WebSecProbe

if __name__ == "__main__":
    url = 'https://example.com'  # Replace with your target URL
    path = 'admin-login'  # Replace with your desired path

    probe = WebSecProbe(url, path)
    probe.run()

```

---

#### 💬 If having issue [Chat here](https://discord.gg/ZChEmMwE8d)
[![Discord Server](https://discord.com/api/guilds/726495265330298973/embed.png)](https://discord.gg/ZChEmMwE8d)

### ⭔ Snapshots:
---

<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/1141162711464550430/1151709638262263858/Screenshot_2023-09-14_at_8.11.44_AM.png" />
