import argparse
from pathlib import Path
from agent.kernel import AgentKernel

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists() or path.suffix != ".java":
        print("[ERROR] invalid input")
        return

    code = path.read_text(encoding="utf-8")

    agent = AgentKernel()
    result = agent.run(code)

    print("[RESULT]")
    print("status:", result["status"])
    print("confidence:", result["confidence"])
    print("final_output:")
    print(result["final_output"])

if __name__ == "__main__":
    main()
