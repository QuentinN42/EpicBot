#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )"

RES=$(curl -s 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=FR&allowCountries=FR')

echo "$RES" | jq -r '[ .data.Catalog.searchStore.elements[] | {"id": .title, "date": (.promotions.promotionalOffers[0].promotionalOffers[0].endDate), "price": .price.totalPrice.fmtPrice, "link": .customAttributes[3].value} ] | map(select(.price.originalPrice != "0")) | map(select(.price.discountPrice == "0")) | .[] | (.id + ";"  + "https://www.epicgames.com/store/fr/p/" + .link + ";" + (.date | split("T")[0]))' > ./jeuxYolo.txt

python3 convert.py
