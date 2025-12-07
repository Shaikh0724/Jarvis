import webbrowser
import musiclibrary
import requests
from openai import OpenAI

newsapi = "df1b29df8efd4af2f4fa031b"

def aiprocess(command):
    client = OpenAI(api_key="sk-prrih7cuEYOYV5Z6Treal5RE5aPJxdJg2ItHZT3BlbkFJs9SNvWWvdQoNz0Y7pbnfDDOajg_XNM-ncMYMPXrt9eWnYdQZZbPPmexviy4HgzTiR85mGoipoA")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis."},
            {"role": "user", "content": command}
        ]
    )

    return response.choices[0].message.content

def processCommand(c):
    c_lower = c.lower()
    if "open google" in c_lower:
        webbrowser.open("https://google.com")
        return "Opening Google."
    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")
        return "Opening Facebook."
    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."
    elif "open linkedin" in c_lower:
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn."
    elif c_lower.startswith("play"):
        try:
            song = c_lower.split(" ", 1)[1]
            link = musiclibrary.music.get(song)
            if link:
                webbrowser.open(link)
                return f"Playing {song}."
            else:
                return f"Sorry, {song} is not in your music library."
        except IndexError:
            return "Please specify the song you want to play."
    elif "news" in c_lower:
        r = requests.get(f"https://newsapi.org/v2/top-headlinesapiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            headlines = [article['title'] for article in articles]
            return "Here are the top news headlines:\n" + "\n".join(headlines[:5])  # Top 5 headlines
        else:
            return "Sorry, I couldn't fetch the news right now."
    else:
        output = aiprocess(c)
        return output
