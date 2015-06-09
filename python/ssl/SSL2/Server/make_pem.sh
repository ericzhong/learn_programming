#!/bin
CertName="./ClientCA/"$1"_cert.pem"
KeyName="./ClientCA/"$1"_key.pem"
Sub="/C=CN/ST=ShangHai/L=ShangHai/O=WaHaHa.CO/CN="$1"/OU="$1".CA"

echo $CertName
echo $KeyName
echo $Sub

openssl req -new -x509 -days 365 -nodes -out $CertName -keyout $KeyName -subj $Sub
