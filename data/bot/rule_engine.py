def rule_based_response(text):
    if "refund" in text.lower():
        return "To request a refund, please visit your order history."
    elif "human" in text.lower():
        return "I'll connect you with a support agent."
    return None
