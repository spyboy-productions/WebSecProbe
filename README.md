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

<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/1141162711464550430/1151709638581039115/webSecProbe.png" />


<h4 align="center">  Web Security Assessment Tool </h4>

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

### ⭔ PYPI Installation :
---
```
pip install WebSecProbe
```

#### How To Run:
```
WebSecProbe <URL> <Path>

________________________

Example: WebSecProbe https://spyboy.in premium
```

---

#### 💬 If having issue [Chat here](https://discord.gg/ZChEmMwE8d)
[![Discord Server](https://discord.com/api/guilds/726495265330298973/embed.png)](https://discord.gg/ZChEmMwE8d)

### ⭔ Snapshots
---

<img width="100%" align="centre" src="https://cdn.discordapp.com/attachments/1141162711464550430/1151709638262263858/Screenshot_2023-09-14_at_8.11.44_AM.png" />
