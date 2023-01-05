SONG=$()

REQ=$(curl --request GET \
        --url 'https://genius-song-lyrics1.p.rapidapi.com/search?q=Sing%20About%20Me%2C%20I'\''m%20Dying%20of%20Thirst&per_page=10&page=1' \
        --header 'X-RapidAPI-Host: genius-song-lyrics1.p.rapidapi.com' \
        --header 'X-RapidAPI-Key: 609d857248msha834b1ce9713354p138f30jsn8fd004b5a141')



SAMPLE_PAGE=$(echo $REQ | jq '.response.hits[0].result.relationships_index_url')
echo $SAMPLE_PAGE

# curl https://genius.com/Kendrick-lamar-sing-about-me-im-dying-of-thirst-sample | grep My\ Romance

#beautifulsoup to parse html
