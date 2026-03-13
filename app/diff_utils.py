import difflib

def compare_versions(old, new):

    old_lines = old.splitlines()
    new_lines = new.splitlines()

    diff = difflib.ndiff(old_lines, new_lines)

    added = []
    removed = []

    for line in diff:
        if line.startswith("+ "):
            added.append(line[2:])
        elif line.startswith("- "):
            removed.append(line[2:])

    return {
        "added": added,
        "removed": removed
    }