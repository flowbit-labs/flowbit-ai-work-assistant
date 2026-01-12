from rich.console import Console
from rich.panel import Panel
from planner import make_plan
from writer import rewrite_text
from review import end_of_day_review

console = Console()

def menu() -> str:
    console.print(Panel.fit("[bold]Flowbit AI Work Assistant[/bold]\nChoose a mode:", subtitle="Flowbit Labs"))
    console.print("1) Plan my day")
    console.print("2) Rewrite text (email / message / paragraph)")
    console.print("3) End-of-day review")
    console.print("4) Exit")
    return console.input("\n[bold]Select:[/bold] ").strip()

def run():
    while True:
        choice = menu()

        if choice == "1":
            console.print("\n[bold]Paste your tasks (one per line).[/bold] Finish with an empty line:\n")
            lines = []
            while True:
                line = input()
                if not line.strip():
                    break
                lines.append(line)
            tasks = "\n".join(lines)
            console.print("\n[bold]Generating your plan...[/bold]\n")
            output = make_plan(tasks)
            console.print(Panel(output, title="Your Plan", subtitle="Keep it realistic."))

        elif choice == "2":
            text = console.input("\nPaste the text you want rewritten:\n")
            goal = console.input("Goal (clarity / shorten / persuasive / friendly) [default: clarity]: ").strip() or "clarity"
            tone = console.input("Tone (professional / friendly / confident) [default: professional and friendly]: ").strip() or "professional and friendly"
            console.print("\n[bold]Rewriting...[/bold]\n")
            output = rewrite_text(text=text, goal=goal, tone=tone)
            console.print(Panel(output, title="Rewritten Text"))

        elif choice == "3":
            console.print("\n[bold]Wins today (finish with empty line):[/bold]")
            wins_lines = []
            while True:
                line = input()
                if not line.strip():
                    break
                wins_lines.append(line)
            wins = "\n".join(wins_lines)

            console.print("\n[bold]Open loops / unfinished (finish with empty line):[/bold]")
            open_lines = []
            while True:
                line = input()
                if not line.strip():
                    break
                open_lines.append(line)
            open_loops = "\n".join(open_lines)

            console.print("\n[bold]Creating your wrap-up...[/bold]\n")
            output = end_of_day_review(wins=wins, open_loops=open_loops)
            console.print(Panel(output, title="End-of-Day Review", subtitle="Close the day cleanly."))

        elif choice == "4":
            console.print("\nGoodbye 👋")
            break
        else:
            console.print("\nPlease choose 1–4.\n")

if __name__ == "__main__":
    run()
