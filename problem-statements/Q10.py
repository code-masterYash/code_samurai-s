def organize_scores(scores: list[int], descending: bool) -> list[int]:
    
    if descending:
        return sorted(scores, reverse=True)
    else:
        return sorted(scores)
