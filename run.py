from dotenv import load_dotenv
from research_crew.crew import get_crew

load_dotenv()

if __name__ == "__main__":
    crew = get_crew()
    crew.kickoff(inputs={'topic': 'AI in healthcare'})