# Task 1 CURL

---

## 1.Curl --version**

**Comand:**
`curl --version`

**Output:**

- curl 8.5.0 (x86_64-pc-linux-gnu)
- libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 (+libidn2/2.3.7) libssh/0.10.6/openssl/zlib nghttp2/1.59.0 librtmp/2.3 OpenLDAP/2.6.7
- Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
- Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd

---

## 2. Get to Fetch Post

**Command:**
`curl http://example.com`

**Output:**

- <!doctype html><html lang="en"><head><title>Example Domain</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style><body><div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.<p><a href="https://iana.org/domains/example">Learn more</a></div></body></html>

---

## 3. Fetch Data from an API

**Command:**
`curl https://jsonplaceholder.typicode.com/posts`

**Output:**

- "userId": 1
- "id": 1
- "title: *"sunt aut facere repellat provident occaecati excepturi optio reprehenderit"*
- body: *"quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"*

---

## 4. View only Headers

**Command:**
`curl -I https://jsonplaceholder.typicode.com/posts`

**Output:**

- HTTP/2 200
- date: Sat, 11 Oct 2025 20:30:48 GMT
- content-type: application/json; charset=utf-8
- access-control-allow-credential: true
- cache-control: max-age=43200
- etag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"
- expires: -1
- nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
- pragma: no-cache
- report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=U%2F3uq4jrCIhuEOZxid5fbtebd0IkPkZMw3LNw4GpzOs%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1758711984"}],"max_age":3600}
- reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=U%2F3uq4jrCIhuEOZxid5fbtebd0IkPkZMw3LNw4GpzOs%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1758711984"
- server: cloudflare
- vary: Origin, Accept-Encoding
- via: 2.0 heroku-router
- x-content-type-options: nosniff
- x-powered-by: Express
- x-ratelimit-limit: 1000
- x-ratelimit-remaining: 999
- x-ratelimit-reset: 1758712004
- x-ratelimit-reset: 1758712004
- cf-cache-status: HIT
- cf-ray: 98d11e106fe2b09f-ATL
- alt-svc: h3=":443"; ma=86400

---

## 5. Make a POST request

**Command:**
`curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`

**Output:**

- "title": "foo"
- "body": "bar"
- "userId": "1"
- "id": 101

---

## Summary

**Task demonstrates how to:**

- curl --version: shows installed version and supported protocols.
- GET request: displays multiple JSON posts.
- Header request: returns status and metadata (e.g., HTTP/1.1 200 OK)
- POST request: returns the created post with an auto-generated ID (simulated).

- -I → Fetch headers only.
- -X → Specify HTTP method (e.g., POST, PUT, DELETE).
- -d → Send data with the request.
- Use | jq to format JSON output neatly.