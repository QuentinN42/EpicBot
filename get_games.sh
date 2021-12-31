#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )"

RES=$(curl -s 'https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=FR&allowCountries=FR')

echo "$RES" | jq -r '[ .data.Catalog.searchStore.elements[] | {"id": .title, "price": .price.totalPrice.fmtPrice} ] | map(select(.price.originalPrice != "0")) | map(select(.price.discountPrice == "0")) | .[] | .id' >> ./data/TodoDiscord.txt
