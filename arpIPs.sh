IF='enp0s3'

mapfile -t IPs < <(sudo arp-scan -I $IF --localnet)

IPs=("${IPs[@]::${#IPs[@]}-3}");

for ip in "${IPs[@]:2}"
do
  echo $ip | cut -d " " -f1
done
