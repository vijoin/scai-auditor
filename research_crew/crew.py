from crewai import Crew, Process
from .agents import researcher, writer
from .tasks import research_task, write_task

# Forming the tech-focused crew with some enhanced configurations
def get_crew():
    return Crew(
            agents=[researcher, writer],
            tasks=[research_task, write_task],
            process=Process.sequential,  # Optional: Sequential task execution is default
            memory=True,
            cache=True,
            max_rpm=100,
            share_crew=True
            )