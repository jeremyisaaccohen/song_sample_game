import requests
import argparse
from bs4 import BeautifulSoup
from selenium import webdriver


parser = argparse.ArgumentParser()
# parser.add_argument('Song')
# parser.add_argument('Artist')
parser.parse_args()
def rapidapi():
	querystring = {"text_format":"dom"}
	headers = {
		"X-RapidAPI-Key": "609d857248msha834b1ce9713354p138f30jsn8fd004b5a141",
		"X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
	}
	url = "https://genius-song-lyrics1.p.rapidapi.com/songs/2396871"
	response = requests.request("GET", url, headers=headers, params=querystring)
	print(response.text)


def geniusapi():

	client_id = "UiJtUoqoOlqLxD7kVUhoCGQxIofdfnFjI4LFck0ARMAwOnvXSlHVagtMIEFeRSl0"
	client_access_token = "FIeY8XZp0nPVK7o49zvY8ibot9xSJzpTzfy3PFe_yIVf-uEZSHYvMRIQq_8pB-qb"
	client_access_secret = "YGzLXsgNL1to2qs5Jg1bmaUu7HswxopfzolQwCodSjpsQyrvAcx6kHqOfeuporgEpSrNrFQQq9dvz1nh2HK4tA"

	search_term = "sing about me i'm dying of thirst"
	# search_term = input("fucking give me a song pussy : \n")
	# search_term = "thought about you vince"
	# search_term = "you aint alone alabama shakes"
	# search_term = "rigamortis kendrick"
	SAMPLES_URL = {"relationships_index_url" : "https://genius.com/Kendrick-lamar-sing-about-me-im-dying-of-thirst-sample" } 

	genius_search_url = f"https://api.genius.com/search?q={search_term}&access_token={client_access_token}"
	headers = {"User-Agent": "PostmanRuntime/7.30.0"}
	response = requests.request("GET", genius_search_url, headers=headers)
	json_data = response.json()


	relationships_index_url = json_data["response"]["hits"][0]["result"]["relationships_index_url"]
	print("\n\n", relationships_index_url, "\n\n")

	samples_search = requests.request("GET", relationships_index_url, headers=headers)
	# print(samples_search.json())
	soup = BeautifulSoup(samples_search.text, "html.parser")
	# print(soup.prettify())

	sample_class_section="RelationshipListshared__RelationshipListSection-sc-1ulnidt-2 dBbpTG"
	divs = soup.find_all("div","RelationshipListshared__RelationshipListSongRow-sc-1ulnidt-0 esFNYV")
	testdivs = soup.find_all("section", sample_class_section)

	# for div in soup.find_all("section", sample_class_section):
		# print(div.text)
	# for div in divs:
		# print(div, "\n")
	# soup.find_all(<main class="songRelationshipsPage__MainContent-sc-19wb1u0-0 XQkWY">)
	songcard = "SongCard__CardContents-sc-1bjj0ja-2 jLGCix"
	# first = soup.find(section=songcard)
	# print(first)
	# for div in soup.find_all("div", songcard):
		# print(div.text)

	# for div in soup.find_all("a", "SongCard__Title-sc-1bjj0ja-3 dOlxKO"):
	# 	print(div.text)

	print("\n\n\n")

	def get_only_samples():
		for div in soup.find("section", sample_class_section):
			for inner in div.find_all("a","SongCard__Title-sc-1bjj0ja-3 dOlxKO"):
				yield inner.text

	samples = get_only_samples()
	print(next(samples))
	print(next(samples))
	print(next(samples))
	#class="SongCard__Title-sc-1bjj0ja-3 dOlxKO"
	# samples_json = samples_search.json()
	# for song in samples_json['response']['hits']:
		# print("l")
	





geniusapi()