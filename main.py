import google.generativeai as palm
import asyncio
from pyppeteer import launch
import config
from googletrans import Translator

async def scrape_reviews(url):
    reviews = []
    browser = await launch({"headless": True, "args": ["--window-size=800,3200"], "executablePath": "C:/Program Files/Google/Chrome/Application/chrome.exe"})
    page = await browser.newPage()
    await page.setViewport({"width": 800, "height": 3200})
    await page.goto(url)
    await page.waitForSelector(".jftiEf")

    elements = await page.querySelectorAll(".jftiEf")
    for element in elements:
        try:
            await page.waitForSelector(".w8nwRe")
            more_btn = await element.querySelector(".w8nwRe")
            await page.evaluate("button => button.click()", more_btn)
            await page.waitForTimeout(5000)
        except:
            pass

        snippet = await element.querySelector(".MyEned")
        if snippet:
            text = await page.evaluate("selected => selected.textContent", snippet)
            reviews.append(text)

    await browser.close()
    return reviews

def summarize(reviews, model):
    prompt = "I collected some reviews of a place I was considering visiting. Can you summarize the reviews for me? The reviews are down below:\n"
    for review in reviews:
        prompt += "\n" + review

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,  # A previsibilidade do texto gerado
        max_output_tokens=800,
    )

    return completion.result

def main():
    # Configurar a API Palm
    palm.configure(api_key=config.API_KEY)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    if not models:
        print("No suitable models found for text generation.")
        return

    model = models[0].name
    print("We will be using model:", model)

    # Entrada do usuário
    url = input("Enter a URL from Google Maps:")

    # Coletar reviews
    reviews = asyncio.get_event_loop().run_until_complete(scrape_reviews(url))

    if not reviews:
        print("No reviews found.")
        return

    # Traduzir reviews para inglês
    translator = Translator()
    translated_reviews = []
    for review in reviews:
        try:
            translated = translator.translate(review, dest='en').text
            translated_reviews.append(translated)
        except Exception as e:
            print(f"Translation error for review: {review}. Error: {e}")

    if not translated_reviews:
        print("No translated reviews available.")
        return

    # Resumir as reviews
    result = summarize(translated_reviews, model)
    print(result)

if __name__ == "__main__":
    main()
