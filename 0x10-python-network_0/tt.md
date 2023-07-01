### Usage: curl \[options\] url
### Let assume <url> to be www.malloshub.com:

```
     --abstract-unix-socket <path> Connect via abstract Unix domain socket
     --alt-svc <file name> Enable alt-svc with this cache file
     --anyauth       Pick any authentication method
```


### --abstract-unix-socket <path>: Connect via an abstract Unix domain socket.
```
curl --abstract-unix-socket /path/to/socket http://www.malloshub.com
```
* This command connects to http://www.malloshub.com using an abstract Unix domain socket located at /path/to/socket.

###  --alt-svc <file name>: Enable Alternative Services (alt-svc) with the specified cache file.
```
curl --alt-svc cache.txt http://www.malloshub.com
```
* This command enables Alternative Services (alt-svc) using the cache file cache.txt when making a request to http://www.malloshub.com.

### --anyauth: Pick any authentication method.
```
curl --anyauth -u username:password http://www.malloshub.com
```
* This command sends a request to http://www.malloshub.com using any available authentication method with the provided username and password.


```
-a, --append        Append to target file when uploading
     --basic         Use HTTP Basic Authentication
     --cacert <file> CA certificate to verify peer against
     --capath <dir>  CA directory to verify peer against
```
## Breakdown with examples
### -a or --append:
* This option is used to append the output to an existing file instead of overwriting it.

```
curl -a -o output.txt www.malloshub.com
```
* This command retrieves the content from www.malloshub.com and appends it to the file "output.txt" without overwriting any existing content.


### --basic:
* The --basic option is used to specify HTTP Basic authentication credentials.

```
curl --basic -u username:password www.malloshub.com
```
* This command sends an HTTP request to www.malloshub.com with the provided username and password for basic authentication.


### --cacert:
* The --cacert option is used to specify a CA certificate file for SSL/TLS verification.

```
curl --cacert /path/to/cert.pem https://www.malloshub.com
```
* This command connects to www.malloshub.com using HTTPS and verifies the server's SSL/TLS certificate against the provided CA certificate file.


### --capath:
* The --capath option is used to specify a directory containing multiple CA certificates for SSL/TLS verification.

```
curl --capath /path/to/certs https://www.malloshub.com
```
* This command connects to www.malloshub.com using HTTPS and verifies the server's SSL/TLS certificate against the CA certificates found in the specified directory.


```
 -E, --cert <certificate[:password]> Client certificate file and password
     --cert-status   Verify the status of the server certificate
     --cert-type <type> Certificate file type (DER/PEM/ENG)
     --ciphers <list of ciphers> SSL ciphers to use
     --compressed    Request compressed response
     --compressed-ssh Enable SSH compression
```
## Breakdown with examples
### -E, --cert: Specify a client certificate for SSL/TLS authentication.
```
curl -E /path/to/cert.pem https://www.malloshub.com
```
* This command uses the client certificate located at /path/to/cert.pem for SSL/TLS authentication when connecting to https://www.malloshub.com.

### --cert-status: Enable certificate status verification.
```
curl --cert-status https://www.malloshub.com
```
* This command enables certificate status verification when connecting to https://www.malloshub.com.

### --cert-type: Specify the certificate type.
```
curl --cert-type P12 --cert /path/to/cert.p12 https://www.malloshub.com
```
* This command specifies that the client certificate type is P12 (PKCS#12) and uses the certificate located at /path/to/cert.p12 when connecting to https://www.malloshub.com.

### --ciphers: Specify the SSL/TLS ciphers to use.
```
curl --ciphers AES256-SHA https://www.malloshub.com
```
* This command specifies that the SSL/TLS ciphers to be used are AES256-SHA when connecting to https://www.malloshub.com.

### --compressed: Enable compression for HTTP requests.
```
curl --compressed https://www.malloshub.com
```
* This command enables compression for HTTP requests when connecting to https://www.malloshub.com.

### --compressed-ssh: Enable compression for SSH connections.
```
curl --compressed-ssh scp://www.malloshub.com/file.txt
```
* This command enables compression for SSH connections when transferring the file file.txt from www.malloshub.com using SCP.


```
 -K, --config <file> Read config from a file
     --connect-timeout <seconds> Maximum time allowed for connection
     --connect-to <HOST1:PORT1:HOST2:PORT2> Connect to host
```
## Breakdown with examples
### -K, --config: Specify the path to the config file.
```
curl -K /path/to/config.txt https://www.malloshub.com
```
* This command uses the options specified in the config file located at /path/to/config.txt when connecting to https://www.malloshub.com.

### --connect-timeout: Specify the maximum time allowed for the connection to be established.
```
curl --connect-timeout 10 https://www.malloshub.com
```
* This command sets the maximum time allowed for the connection to be established to 10 seconds when connecting to https://www.malloshub.com.

### --connect-to: Specify a network address and port to connect to.
```
curl --connect-to www.malloshub.com:443:proxy.example.com:8080 https://www.malloshub.com
```
* This command connects to www.malloshub.com via the proxy server proxy.example.com on port 8080 when making requests to https://www.malloshub.com.

```
 -C, --continue-at <offset> Resumed transfer offset
```
## Breakdown with examples
### -C, --continue-at: Resume a previous file transfer.
```
curl -C - -O https://www.malloshub.com/file.txt
```
* This command resumes a previous file transfer of file.txt from https://www.malloshub.com, starting from where it left off.


```
 -b, --cookie <data|filename> Send cookies from string/file

```
## Breakdown with examples
### -b, --cookie: Send cookies with the request.
```
curl -b "cookie1=value1; cookie2=value2" https://www.malloshub.com
```
* This command sends the specified cookies with




```
 -c, --cookie-jar <filename> Write cookies to <filename> after operation
     --create-dirs   Create necessary local directory hierarchy
     --crlf          Convert LF to CRLF in upload
     --crlfile <file> Get a CRL list in PEM format from the given file
```
## Breakdown with examples

### -c, --cookie-jar <filename>: Write cookies to <filename> after operation.
```
curl -c cookies.txt https://www.malloshub.com
```
* This command saves the cookies received from the server to a file named cookies.txt after the operation is completed.

### --create-dirs: Create necessary local directory hierarchy.
```
curl --create-dirs -o /path/to/save/file.txt https://www.malloshub.com/file.txt
```
* This command creates the necessary local directory hierarchy (if not already present) and saves the downloaded file from https://www.malloshub.com/file.txt to /path/to/save/file.txt.

### --crlf: Convert LF to CRLF in upload.
```
curl --crlf -T upload.txt https://www.malloshub.com/upload
```
* This command converts LF (line feed) to CRLF (carriage return + line feed) in the file upload.txt before uploading it to https://www.malloshub.com/upload.

### --crlfile: Specify a file with certificate revocation lists.
```
curl --crlfile crl.pem https://www.malloshub.com
```
* This command specifies the file crl.pem containing certificate revocation lists when connecting to https://www.malloshub.com.


```
 -d, --data <data>   HTTP POST data
     --data-ascii <data> HTTP POST ASCII data
     --data-binary <data> HTTP POST binary data
     --data-raw <data> HTTP POST data, '@' allowed
     --data-urlencode <data> HTTP POST data url encoded
     --delegation <LEVEL> GSS-API delegation permission
     --digest        Use HTTP Digest Authentication
```
## Breakdown with examples
### -d, --data <data>: Send data in a POST request.
```
curl -d "param1=value1&param2=value2" http://www.malloshub.com/endpoint
```
* This command sends a POST request to http://www.malloshub.com/endpoint with the data param1=value1&param2=value2.

### --data-ascii: Send data in ASCII format.
```
curl --data-ascii "Hello, World!" http://www.malloshub.com/endpoint
```
* This command sends the ASCII-encoded data "Hello, World!" in a POST request to http://www.malloshub.com/endpoint.

### --data-binary: Send data as binary.
```
curl --data-binary "@file.bin" http://www.malloshub.com/upload
```
* This command sends the contents of the file.bin file as binary data in a POST request to http://www.malloshub.com/upload.

### --data-raw: Send data as-is without any processing.
```
curl --data-raw '{"key": "value"}' -H "Content-Type: application/json" http://www.malloshub.com/endpoint
```
* This command sends the raw JSON data {"key": "value"} in a POST request to http://www.malloshub.com/endpoint with the appropriate Content-Type header.

### --data-urlencode <data>: URL-encode the data before sending.
```
curl --data-urlencode "param1=value 1" http://www.malloshub.com/endpoint
```
* This command URL-encodes the data param1=value 1 and sends it in a POST request to http://www.malloshub.com/endpoint.

### --delegation <LEVEL>: Set the delegation level.
```
curl --delegation always https://www.malloshub.com
```
* This command sets the delegation level to "always" when making a request to https://www.malloshub.com.

### --digest: Use HTTP Digest authentication.
```
curl --digest -u username:password http://www.malloshub.com/protected
```
* This command sends an HTTP request with Digest authentication using the provided username and password to access http://www.malloshub.com/protected.



```
 -q, --disable       Disable .curlrc
     --disable-eprt  Inhibit using EPRT or LPRT
     --disable-epsv  Inhibit using EPSV
     --disallow-username-in-url Disallow username in url
     --dns-interface <interface> Interface to use for DNS requests
     --dns-ipv4-addr <address> IPv4 address to use for DNS requests
     --dns-ipv6-addr <address> IPv6 address to use for DNS requests
     --dns-servers <addresses> DNS server addrs to use
     --doh-url <URL> Resolve host names over DOH
```
## Breakdown with examples
### -q, --disable: Disable the progress meter and error messages.
```
curl -q http://www.malloshub.com
```
* This command disables the progress meter and error messages, making the output more concise when making a request to http://www.malloshub.com.

### --disable-eprt: Disable EPRT command for FTP.
```
curl --disable-eprt ftp://www.malloshub.com/file.txt
```
* This command disables the use of the EPRT command when connecting via FTP to ftp://www.malloshub.com/file.txt.

### --disable-epsv: Disable EPSV command for FTP.
```
curl --disable-epsv ftp://www.malloshub.com/file.txt
```
* This command disables the use of the EPSV command when connecting via FTP to ftp://www.malloshub.com/file.txt.

### --disallow-username-in-url: Disable the use of a username in the URL.
```
curl --disallow-username-in
```
### --dns-interface <interface>: Specify the network interface to use for DNS resolution.
```
curl --dns-interface eth0 http://www.malloshub.com
```
* This command specifies the network interface eth0 for DNS resolution when making a request to http://www.malloshub.com.

### --dns-ipv4-addr <address>: Specify the IPv4 address to use for DNS resolution.
```
curl --dns-ipv4-addr 8.8.8.8 http://www.malloshub.com
```
* This command specifies the IPv4 address 8.8.8.8 for DNS resolution when making a request to http://www.malloshub.com.

### --dns-ipv6-addr <address>: Specify the IPv6 address to use for DNS resolution.
```
curl --dns-ipv6-addr 2001:4860:4860::8888 http://www.malloshub.com
```
* This command specifies the IPv6 address 2001:4860:4860::8888 for DNS resolution when making a request to http://www.malloshub.com.

### --dns-servers <addresses>: Specify a comma-separated list of DNS server addresses to use for resolution.
```
curl --dns-servers 8.8.8.8,8.8.4.4 http://www.malloshub.com
```
* This command specifies the DNS server addresses 8.8.8.8 and 8.8.4.4 for resolution when making a request to http://www.malloshub.com.

### --doh-url <URL>: Use DNS over HTTPS (DoH) with the specified DoH server URL.
```
curl --doh-url https://dns.example.com https://www.malloshub.com
```
* This command makes a request to https://www.malloshub.com using DNS over HTTPS (DoH) with the specified DoH server URL https://dns.example.com.

### -D, --dump-header <filename>: Write the response headers to a file.
```
curl -D headers.txt http://www.malloshub.com
```
* This command sends a request to http://www.malloshub.com and writes the response headers to the file headers.txt.

### --egd-file <file>: Specify the path to the EGD (Entropy Gathering Daemon) socket file.
```
curl --egd-file /dev/random http://www.malloshub.com
```
* This command specifies the EGD socket file /dev/random for generating entropy when making a request to http://www.malloshub.com.

### --engine <name>: Specify the SSL crypto engine to use.
```
curl --engine pkcs11 https://www.malloshub.com
```
* This command specifies the SSL crypto engine pkcs11 when making a request to https://www.malloshub.com.

### --etag-save <file>: Save the ETag value to a file.
```
curl --etag-save etag.txt http://www.malloshub.com/file.txt
```
* This command retrieves the ETag value from the server when accessing http://www.malloshub.com/file.txt and saves it to the file etag.txt.






```
 -D, --dump-header <filename> Write the received headers to <filename>
     --egd-file <file> EGD socket path for random data
     --engine <name> Crypto engine to use
     --etag-save <file> Get an ETag from response header and save it to a FILE
     --etag-compare <file> Get an ETag from a file and send a conditional request
     --expect100-timeout <seconds> How long to wait for 100-continue
```
## Breakdown with examples





```
 -f, --fail          Fail silently (no output at all) on HTTP errors
     --fail-early    Fail on first transfer error, do not continue
     --false-start   Enable TLS False Start
```
## Breakdown with examples



```
 -F, --form <name=content> Specify multipart MIME data
     --form-string <name=string> Specify multipart MIME data
     --ftp-account <data> Account data string
     --ftp-alternative-to-user <command> String to replace USER [name]
     --ftp-create-dirs Create the remote dirs if not present
     --ftp-method <method> Control CWD usage
     --ftp-pasv      Use PASV/EPSV instead of PORT
```
## Breakdown with examples






```
 -P, --ftp-port <address> Use PORT instead of PASV
     --ftp-pret      Send PRET before PASV
     --ftp-skip-pasv-ip Skip the IP address for PASV
     --ftp-ssl-ccc   Send CCC after authenticating
     --ftp-ssl-ccc-mode <active/passive> Set CCC mode
     --ftp-ssl-control Require SSL/TLS for FTP login, clear for transfer
```
## Breakdown with examples







```
 -G, --get           Put the post data in the URL and use GET
```
## Breakdown with examples







```
 -g, --globoff       Disable URL sequences and ranges using {} and []
     --happy-eyeballs-timeout-ms <milliseconds> How long to wait in milliseconds for IPv6 before trying IPv4
     --haproxy-protocol Send HAProxy PROXY protocol v1 header
```
## Breakdown with examples






```
 -I, --head          Show document info only
```
## Breakdown with examples




```
 -H, --header <header/@file> Pass custom header(s) to server
```
## Breakdown with examples





```
 -h, --help          This help text
     --hostpubmd5 <md5> Acceptable MD5 hash of the host public key
     --http0.9       Allow HTTP 0.9 responses
```
## Breakdown with examples



```
 -0, --http1.0       Use HTTP 1.0
     --http1.1       Use HTTP 1.1
     --http2         Use HTTP 2
     --http2-prior-knowledge Use HTTP 2 without HTTP/1.1 Upgrade
     --http3         Use HTTP v3
     --ignore-content-length Ignore the size of the remote resource
```
## Breakdown with examples




```
 -i, --include       Include protocol response headers in the output
```
## Breakdown with examples



```
 -k, --insecure      Allow insecure server connections when using SSL
     --interface <name> Use network INTERFACE (or address)
```
## Breakdown with examples

```
 -4, --ipv4          Resolve names to IPv4 addresses
 -6, --ipv6          Resolve names to IPv6 addresses
```
## Breakdown with examples



```
 -j, --junk-session-cookies Ignore session cookies read from file
     --keepalive-time <seconds> Interval time for keepalive probes
     --key <key>     Private key file name
     --key-type <type> Private key file type (DER/PEM/ENG)
     --krb <level>   Enable Kerberos with security <level>
     --libcurl <file> Dump libcurl equivalent code of this command line
     --limit-rate <speed> Limit transfer speed to RATE
```
## Breakdown with examples




```
 -l, --list-only     List only mode
     --local-port <num/range> Force use of RANGE for local port numbers
```
## Breakdown with examples




```
 -L, --location      Follow redirects
     --location-trusted Like --location, and send auth to other hosts
     --login-options <options> Server login options
     --mail-auth <address> Originator address of the original email
     --mail-from <address> Mail from this address
     --mail-rcpt <address> Mail to this address
```
## Breakdown with examples




```
 -M, --manual        Display the full manual
     --max-filesize <bytes> Maximum file size to download
     --max-redirs <num> Maximum number of redirects allowed
```
## Breakdown with examples




```
 -m, --max-time <seconds> Maximum time allowed for the transfer
     --metalink      Process given URLs as metalink XML file
     --negotiate     Use HTTP Negotiate (SPNEGO) authentication
```
## Breakdown with examples




```
 -n, --netrc         Must read .netrc for user name and password
     --netrc-file <filename> Specify FILE for netrc
     --netrc-optional Use either .netrc or URL
```
## Breakdown with examples




```
 -:, --next          Make next URL use its separate set of options
     --no-alpn       Disable the ALPN TLS extension
```
## Breakdown with examples




```
 -N, --no-buffer     Disable buffering of the output stream
     --no-keepalive  Disable TCP keepalive on the connection
     --no-npn        Disable the NPN TLS extension
     --no-progress-meter Do not show the progress meter
     --no-sessionid  Disable SSL session-ID reusing
     --noproxy <no-proxy-list> List of hosts which do not use proxy
     --ntlm          Use HTTP NTLM authentication
     --ntlm-wb       Use HTTP NTLM authentication with winbind
     --oauth2-bearer <token> OAuth 2 Bearer Token
```
## Breakdown with examples




```
 -o, --output <file> Write to file instead of stdout
```
## Breakdown with examples




```
 -Z, --parallel      Perform transfers in parallel
     --parallel-immediate Do not wait for multiplexing (with --parallel)
     --parallel-max  Maximum concurrency for parallel transfers
     --pass <phrase> Pass phrase for the private key
     --path-as-is    Do not squash .. sequences in URL path
     --pinnedpubkey <hashes> FILE/HASHES Public key to verify peer against
     --post301       Do not switch to GET after following a 301
     --post302       Do not switch to GET after following a 302
     --post303       Do not switch to GET after following a 303
     --preproxy [protocol://]host[:port] Use this proxy first
```
## Breakdown with examples




```
 -#, --progress-bar  Display transfer progress as a bar
     --proto <protocols> Enable/disable PROTOCOLS
     --proto-default <protocol> Use PROTOCOL for any URL missing a scheme
     --proto-redir <protocols> Enable/disable PROTOCOLS on redirect
```
## Breakdown with examples




```
 -x, --proxy [protocol://]host[:port] Use this proxy
     --proxy-anyauth Pick any proxy authentication method
     --proxy-basic   Use Basic authentication on the proxy
     --proxy-cacert <file> CA certificate to verify peer against for proxy
     --proxy-capath <dir> CA directory to verify peer against for proxy
     --proxy-cert <cert[:passwd]> Set client certificate for proxy
     --proxy-cert-type <type> Client certificate type for HTTPS proxy
     --proxy-ciphers <list> SSL ciphers to use for proxy
     --proxy-crlfile <file> Set a CRL list for proxy
     --proxy-digest  Use Digest authentication on the proxy
     --proxy-header <header/@file> Pass custom header(s) to proxy
     --proxy-insecure Do HTTPS proxy connections without verifying the proxy
     --proxy-key <key> Private key for HTTPS proxy
     --proxy-key-type <type> Private key file type for proxy
     --proxy-negotiate Use HTTP Negotiate (SPNEGO) authentication on the proxy
     --proxy-ntlm    Use NTLM authentication on the proxy
     --proxy-pass <phrase> Pass phrase for the private key for HTTPS proxy
     --proxy-pinnedpubkey <hashes> FILE/HASHES public key to verify proxy with
     --proxy-service-name <name> SPNEGO proxy service name
     --proxy-ssl-allow-beast Allow security flaw for interop for HTTPS proxy
     --proxy-tls13-ciphers <list> TLS 1.3 ciphersuites for proxy (OpenSSL)
     --proxy-tlsauthtype <type> TLS authentication type for HTTPS proxy
     --proxy-tlspassword <string> TLS password for HTTPS proxy
     --proxy-tlsuser <name> TLS username for HTTPS proxy
     --proxy-tlsv1   Use TLSv1 for HTTPS proxy
```
## Breakdown with examples




```
 -U, --proxy-user <user:password> Proxy user and password
     --proxy1.0 <host[:port]> Use HTTP/1.0 proxy on given port
```
## Breakdown with examples




```
 -p, --proxytunnel   Operate through an HTTP proxy tunnel (using CONNECT)
     --pubkey <key>  SSH Public key file name
```
## Breakdown with examples




```
 -Q, --quote         Send command(s) to server before transfer
     --random-file <file> File for reading random data from
```
## Breakdown with examples




```
 -r, --range <range> Retrieve only the bytes within RANGE
     --raw           Do HTTP "raw"; no transfer decoding
```
## Breakdown with examples




```
 -e, --referer <URL> Referrer URL
 -J, --remote-header-name Use the header-provided filename
 -O, --remote-name   Write output to a file named as the remote file
     --remote-name-all Use the remote file name for all URLs
 -R, --remote-time   Set the remote file's time on the local output
```
## Breakdown with examples




```
 -X, --request <command> Specify request command to use
     --request-target Specify the target for this request
     --resolve <host:port:address[,address]...> Resolve the host+port to this address
     --retry <num>   Retry request if transient problems occur
     --retry-connrefused Retry on connection refused (use with --retry)
     --retry-delay <seconds> Wait time between retries
     --retry-max-time <seconds> Retry only within this period
     --sasl-authzid <identity>  Use this identity to act as during SASL PLAIN authentication
     --sasl-ir       Enable initial response in SASL authentication
     --service-name <name> SPNEGO service name
```
## Breakdown with examples




```
 -S, --show-error    Show error even when -s is used
```
## Breakdown with examples




```
 -s, --silent        Silent mode
     --socks4 <host[:port]> SOCKS4 proxy on given host + port
     --socks4a <host[:port]> SOCKS4a proxy on given host + port
     --socks5 <host[:port]> SOCKS5 proxy on given host + port
     --socks5-basic  Enable username/password auth for SOCKS5 proxies
     --socks5-gssapi Enable GSS-API auth for SOCKS5 proxies
     --socks5-gssapi-nec Compatibility with NEC SOCKS5 server
     --socks5-gssapi-service <name> SOCKS5 proxy service name for GSS-API
     --socks5-hostname <host[:port]> SOCKS5 proxy, pass host name to proxy
```
## Breakdown with examples




```
 -Y, --speed-limit <speed> Stop transfers slower than this
```
## Breakdown with examples




```
 -y, --speed-time <seconds> Trigger 'speed-limit' abort after this time
     --ssl           Try SSL/TLS
     --ssl-allow-beast Allow security flaw to improve interop
     --ssl-no-revoke Disable cert revocation checks (Schannel)
     --ssl-reqd      Require SSL/TLS
```
## Breakdown with examples




```
 -2, --sslv2         Use SSLv2
```
## Breakdown with examples




```
 -3, --sslv3         Use SSLv3
     --stderr        Where to redirect stderr
     --styled-output Enable styled output for HTTP headers
     --suppress-connect-headers Suppress proxy CONNECT response headers
     --tcp-fastopen  Use TCP Fast Open
     --tcp-nodelay   Use the TCP_NODELAY option
```
## Breakdown with examples




```
 -t, --telnet-option <opt=val> Set telnet option
     --tftp-blksize <value> Set TFTP BLKSIZE option
     --tftp-no-options Do not send any TFTP options
```
## Breakdown with examples




```
 -z, --time-cond <time> Transfer based on a time condition
     --tls-max <VERSION> Set maximum allowed TLS version
     --tls13-ciphers <list> TLS 1.3 ciphersuites (OpenSSL)
     --tlsauthtype <type> TLS authentication type
     --tlspassword   TLS password
     --tlsuser <name> TLS user name
```
## Breakdown with examples




```
 -1, --tlsv1         Use TLSv1.0 or greater
     --tlsv1.0       Use TLSv1.0 or greater
     --tlsv1.1       Use TLSv1.1 or greater
     --tlsv1.2       Use TLSv1.2 or greater
     --tlsv1.3       Use TLSv1.3 or greater
     --tr-encoding   Request compressed transfer encoding
     --trace <file>  Write a debug trace to FILE
     --trace-ascii <file> Like --trace, but without hex output
     --trace-time    Add time stamps to trace/verbose output
     --unix-socket <path> Connect through this Unix domain socket
```
## Breakdown with examples




```
 -T, --upload-file <file> Transfer local FILE to destination
     --url <url>     URL to work with
```
## Breakdown with examples




```
 -B, --use-ascii     Use ASCII/text transfer
 -u, --user <user:password> Server user and password
 -A, --user-agent <name> Send User-Agent <name> to server
 -v, --verbose       Make the operation more talkative
 -V, --version       Show version number and quit
 -w, --write-out <format> Use output FORMAT after completion
     --xattr         Store metadata in extended file attributes
 ```
## Breakdown with examples





