def create_bar(percentage, length=50) -> str:
    filled = int(length * percentage // 100)
    return "█" * filled + "░" * (length - filled)
