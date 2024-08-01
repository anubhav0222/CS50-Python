import emoji

text = input("Input: ")
if ":thumbsup:" in text:
    text = text.replace(":thumbsup:", ":thumbs_up:")

if ":earth_asia:" in text:
    text = text.replace(":earth_asia:", "🌏")

print(emoji.emojize(text))
