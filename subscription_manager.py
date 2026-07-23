import datetime

class SubscriptionManager:
    """
    Manages user subscription tiers and enforces daily application quotas.
    """
    
    TIERS = {
        "FREE": {"price": 0, "daily_limit": 2, "interviews": 1},
        "PRO": {"price": 9.97, "daily_limit": 5, "interviews": 2},
        "EXPERT": {"price": 19.97, "daily_limit": 30, "interviews": 5}
    }

    def __init__(self):
        # In a real app, this data would persist in a database (e.g., PostgreSQL)
        self.user_subscriptions = {} # user_id -> tier
        self.daily_usage = {}        # (user_id, date) -> count

    def upgrade_user(self, user_id, tier):
        """Simulates a successful payment and tier upgrade."""
        if tier.upper() in self.TIERS:
            self.user_subscriptions[user_id] = tier.upper()
            return True, f"Successfully upgraded to {tier} tier."
        return False, "Invalid tier selection."

    def get_user_tier(self, user_id):
        return self.user_subscriptions.get(user_id, "FREE")

    def can_apply(self, user_id):
        """Checks if the user has remaining daily applications."""
        tier = self.get_user_tier(user_id)
        limit = self.TIERS[tier]["daily_limit"]
        
        today = datetime.date.today().isoformat()
        current_count = self.daily_usage.get((user_id, today), 0)
        
        if current_count < limit:
            return True, limit - current_count
        return False, 0

    def record_application(self, user_id):
        """Increments the daily application count for the user."""
        allowed, remaining = self.can_apply(user_id)
        if allowed:
            today = datetime.date.today().isoformat()
            self.daily_usage[(user_id, today)] = self.daily_usage.get((user_id, today), 0) + 1
            return True, remaining - 1
        return False, "Daily limit reached. Upgrade to send more resumes."

if __name__ == "__main__":
    # Demo the logic
    manager = SubscriptionManager()
    user = "user_123"
    
    print(f"Initial Tier: {manager.get_user_tier(user)}")
    
    # Try applying on Free tier
    for i in range(3):
        success, msg = manager.record_application(user)
        print(f"Application {i+1}: {success} ({msg})")
        
    # Upgrade to Pro
    success, msg = manager.upgrade_user(user, "PRO")
    print(f"\n{msg}")
    
    # Try applying on Pro tier
    for i in range(3, 7):
        success, msg = manager.record_application(user)
        print(f"Application {i+1}: {success} ({msg})")
