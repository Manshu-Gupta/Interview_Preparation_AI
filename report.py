import json
import os
import sys

def load_memory(memory_file="memory.json"):
    """Safely reads the local memory JSON file."""
    if not os.path.exists(memory_file):
        print(f"\n[!] Error: Memory file '{memory_file}' not found.")
        print("    Please run an interview session first to generate data.\n")
        sys.exit(1)
        
    try:
        with open(memory_file, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"\n[!] Error reading memory file: {e}\n")
        sys.exit(1)

def generate_terminal_report():
    """Parses local memory data and builds a clean terminal performance summary."""
    memory = load_memory()
    scores = memory.get("scores", {})
    history = memory.get("history", [])

    print("\n" + "=" * 46)
    print("      AI INTERVIEW AGENT: PERFORMANCE REPORT      ")
    print("=" * 46)

    if not scores:
        print("\n  [i] No interview history metrics recorded yet.")
        print("=" * 46 + "\n")
        return

    # 1. Overall Metrics
    total_questions = len(history)
    print(f"\n  Total Questions Answered : {total_questions}")
    
    all_scores = [s for topic_scores in scores.values() for s in topic_scores]
    if all_scores:
        avg_overall = sum(all_scores) / len(all_scores)
        print(f"  Overall Average Score    : {avg_overall:.2f} / 10.00")
    
    print("\n" + "-" * 46)
    print(f"  {'TOPIC':<25} | {'AVERAGE SCORE':<15}")
    print("-" * 46)

    # 2. Topic Breakdown
    weak_topics = []
    for topic, topic_scores in scores.items():
        if not topic_scores:
            continue
        avg = sum(topic_scores) / len(topic_scores)
        print(f"  {topic:<25} | {avg:>5.2f} / 10.00")
        
        if avg < 7.0:
            weak_topics.append((topic, avg))

    print("-" * 46)

    # 3. Focus Areas / Weak Topics
    print("\n  TARGET FOCUS AREAS (Score < 7.0)")
    print("  " + "." * 42)
    if weak_topics:
        for topic, avg in weak_topics:
            print(f"  • {topic:<23} (Needs Work: {avg:.2f}/10)")
    else:
        print("  🎉 None! Candidate meets standard baselines across all tracked domains.")

    print("=" * 46 + "\n")

if __name__ == "__main__":
    generate_terminal_report()