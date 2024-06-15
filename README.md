# SCAI: PoC Phase 1

## Langchain Smart Contract Auditor Crew

This project utilizes CrewAI to build a collaborative agent crew for smart contract audits. The crew leverages the power of Langchain to combine individual agent expertise and achieve a comprehensive security assessment.

**Features:**

* **Smart Contract Code Analysis:** 
    * The crew can read and understand Solidity smart contract code.
* **Automated Tool Integration:**
    * The crew can interact with various static analysis tools to identify potential vulnerabilities. (e.g., Slither, Mythril)
* **Self-Directed Analysis:**
    * Crew agents can analyze the code for vulnerabilities beyond those identified by automated tools.
* **Vulnerability Report Generation:**
    * The crew collaborates to create a comprehensive report documenting identified vulnerabilities, their severity, and potential impact.

**Crew Composition:**

* **Code Reader Agent:** Analyzes the smart contract code and extracts relevant information.
* **Static Analysis Agent:** Communicates with and retrieves findings from automated tools.
* **Vulnerability Analyst Agent:** Applies its expertise to identify vulnerabilities not caught by automation.
* **Report Compiler Agent:** Integrates findings from all agents and generates a human-readable report.

**Technology Stack:**

* CrewAI: [https://www.youtube.com/watch?v=2ZsG3PV91cg](https://www.youtube.com/watch?v=2ZsG3PV91cg)
* Langchain: [https://www.pinecone.io/learn/series/langchain/langchain-intro/](https://www.pinecone.io/learn/series/langchain/langchain-intro/)
    * (Specific libraries/frameworks for agent communication and analysis will depend on chosen implementation)

**Getting Started:**

1. **Prerequisites:**
    * A CrewAI account and familiarity with Langchain concepts.
    * Installation of any required libraries for the chosen static analysis tools. (Instructions might vary depending on the tools).
2. **Clone the Repository:**
    ```bash
    git clone https://github.com/vijoin/scai-auditor.git
    ```
3. **Configure Agent Communication:**
    * Update the configuration files within the `crew` directory to specify communication channels between agents and any necessary API keys for static analysis tools.
4. **Run the Audit:**
    * (Specific instructions will depend on your chosen implementation, but likely involve running a script that initiates the Crew workflow).

## How to run

```bash
python -m .venv venv
source .venv/bin/activate
pip install -r requirements.txt
```

* create `.env` file with your apikeys. See [example](.env.example).

then `python run.py`