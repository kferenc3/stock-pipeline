FROM minio/minio:latest

EXPOSE 9000:9000
EXPOSE 9001:9001

VOLUME ~/minio/data:/data

CMD ["server", "/data" "--console-address", ":9001"]