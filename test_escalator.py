from src.escalator import should_escalate

print(should_escalate("I need a refund immediately", 0.9))
print(should_escalate("How do I reset password?", 0.9))
print(should_escalate("Unknown issue", 0.2))