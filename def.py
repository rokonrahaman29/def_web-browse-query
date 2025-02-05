def browse_web(query):
    """Browse the web and fetch real-time information using SerpAPI."""
    try:
        if not SERPAPI_API_KEY:
            speak("SerpAPI key is missing. Please check your .env file.")
            return

        params = {
          "q": query,
          "api_key": SERPAPI_API_KEY
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        if "organic_results" in results and results["organic_results"]:
            search_results = []
            
            for i, result in enumerate(results["organic_results"][:3]):  # Limit to top 3
                title = result.get("title", "").strip()
                snippet = result.get("snippet", "").strip()
                link = result.get("link", "").strip()
                
                if title:
                    clean_title = "".join(e for e in title if e.isalnum() or e.isspace())  # Remove special characters
                    search_results.append(f"{i+1}: {clean_title}. {snippet}.")
            
            if search_results:
                speak("Here are some search results: " + " ".join(search_results))
            else:
                speak("Sorry, I couldn't find relevant information.")

        elif "answer_box" in results:
            answer = results["answer_box"].get("answer", None)
            if answer:
                clean_answer = re.sub(r'[^A-Za-z0-9\s *!@#$%^&,./;',"<>?/:[]{}", '', answer)  # Remove special characters
                speak(f"Here's the answer: {clean_answer}")
            else:
                speak("I couldn't find a direct answer.")

        else:
            speak("Sorry, I couldn't find any relevant information.")

    except Exception as e:
        speak(f"Failed to browse the web: {str(e)}")
