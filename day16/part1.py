# Time complexity: 
def function1(rules, nearby_tickets):
    error_rate = 0
    for ticket in nearby_tickets:
        if not is_valid_ticket(rules, ticket):
            error_rate += ticket
    return error_rate

def is_valid_ticket(rules, ticket):
    for i in range(0, len(rules), 2):
        if ticket in range(rules[i], rules[i + 1] + 1):
            return True
    return False

