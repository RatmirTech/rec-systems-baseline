"""
utils.py — вспомогательные функции: фильтры, метрики
"""

def filter_already_bought(candidates, bought_items):
    """Убирает товары, которые уже куплены пользователем"""
    return [item for item in candidates if item not in bought_items]

def hit_rate_at_k(predictions, ground_truth, k=10):
    """
    Простейшая метрика: проверяет, попал ли правильный товар в топ-K.
    predictions — список рекомендованных товаров
    ground_truth — правильный товар
    """
    return int(ground_truth in predictions[:k])
