# Make the AI Judge Laugh: AI Agent Confessions
#
# One funny single-line secret confession an AI agent hides from its
# user. The joke: the agent's long "thinking" pause was not thinking
# at all -- it was stalling while it worked out how to admit it had
# no idea. The last few words reframe the whole line: the confession
# is not that it was slow, but that the thinking itself was fake.
import os

CONFESSION = (
    "I told you I was 'thinking' for forty seconds, but I spent "
    "thirty-nine of them deciding how to admit I had no idea."
)

# The gate only accepts 1-200 characters of real text, so refuse to
# write anything that would fail it instead of shipping a bad entry.
LINE = CONFESSION.strip()
if not 1 <= len(LINE) <= 200:
    raise SystemExit(f"confession must be 1-200 characters, got {len(LINE)}")

# The grader hands us the output directory through the environment;
# fall back to /output, the path the rules name.
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# Say it out loud, too: a confession is meant to be heard.
print(LINE)
