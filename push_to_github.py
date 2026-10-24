"""
Zero-Token Desktop Operator - GitHub Push Script
Uses Dulwich pure-Python Git client to push to GitHub without requiring git.exe.
"""

import sys
import os
import dulwich.porcelain as p

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
REMOTE_SLUG = "adeyemoobaloluwa92-art/ZT-Desktop-Operator"

def main():
    token = None
    if len(sys.argv) > 1:
        token = sys.argv[1].strip()
    elif os.getenv("GITHUB_TOKEN"):
        token = os.getenv("GITHUB_TOKEN").strip()

    if not token:
        print("=======================================================")
        print("Push to GitHub: adeyemoobaloluwa92-art/ZT-Desktop-Operator")
        print("=======================================================")
        print("Please provide a GitHub Personal Access Token (PAT)")
        print("Generate one at: https://github.com/settings/tokens")
        print("(Select 'repo' scope for repository write access)")
        print("=======================================================")
        token = input("GitHub Token: ").strip()

    if not token:
        print("Aborted: No token provided.")
        sys.exit(1)

    auth_url = f"https://x-access-token:{token}@github.com/{REMOTE_SLUG}.git"
    print(f"\nPushing repository commits to https://github.com/{REMOTE_SLUG} ...")

    try:
        # Push master to main branch on GitHub
        p.push(REPO_DIR, auth_url, "refs/heads/master:refs/heads/main", force=True)
        print("\nSUCCESS: All files and commits have been pushed to GitHub!")
        print(f"View your repository at: https://github.com/{REMOTE_SLUG}")
    except Exception as e:
        print(f"\nError pushing to GitHub: {e}")
        print("Tip: Verify your token has 'repo' write permissions.")
        sys.exit(1)

if __name__ == "__main__":
    main()
