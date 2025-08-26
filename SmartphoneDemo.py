class Smartphone:
    """Base class representing a smartphone"""
    
    def __init__(self, brand, model, storage, battery_capacity):
        # Encapsulation: using private attributes
        self._brand = brand
        self._model = model
        self._storage = storage  # in GB
        self._battery_capacity = battery_capacity  # in mAh
        self._battery_level = 100  # percentage
        self._is_powered_on = False
    
    # Getter methods (encapsulation)
    def get_brand(self):
        return self._brand
    
    def get_model(self):
        return self._model
    
    def get_battery_level(self):
        return self._battery_level
    
    def power_on(self):
        if self._battery_level > 5:
            self._is_powered_on = True
            print(f"{self._brand} {self._model} is now powered on! 📱")
        else:
            print("Battery too low to power on! ⚠️")
    
    def power_off(self):
        self._is_powered_on = False
        print(f"{self._brand} {self._model} is now powered off.")
    
    def make_call(self, number):
        if self._is_powered_on and self._battery_level > 2:
            print(f"📞 Calling {number}...")
            self._battery_level -= 2
            return True
        return False
    
    def send_message(self, number, message):
        if self._is_powered_on and self._battery_level > 1:
            print(f"💬 Sending message to {number}: '{message}'")
            self._battery_level -= 1
            return True
        return False
    
    def charge(self, minutes):
        charge_amount = minutes * 0.5  # 0.5% per minute
        self._battery_level = min(100, self._battery_level + charge_amount)
        print(f"🔋 Charging... Battery now at {self._battery_level:.1f}%")
    
    def display_info(self):
        status = "On" if self._is_powered_on else "Off"
        print(f"\n📱 {self._brand} {self._model}")
        print(f"💾 Storage: {self._storage}GB")
        print(f"🔋 Battery: {self._battery_level:.1f}% ({self._battery_capacity}mAh)")
        print(f"⚡ Status: {status}")


# Inheritance: GamingPhone extends Smartphone
class GamingPhone(Smartphone):
    """Specialized class for gaming smartphones"""
    
    def __init__(self, brand, model, storage, battery_capacity, gpu_model, cooling_system):
        super().__init__(brand, model, storage, battery_capacity)
        self._gpu_model = gpu_model
        self._cooling_system = cooling_system
        self._game_mode = False
    
    def enable_game_mode(self):
        self._game_mode = True
        print("🎮 Game mode enabled! Enhanced performance activated.")
    
    def disable_game_mode(self):
        self._game_mode = False
        print("🎮 Game mode disabled.")
    
    def play_game(self, game_name):
        if self._is_powered_on and self._battery_level > 10:
            print(f"🎯 Playing {game_name}...")
            battery_drain = 5 if self._game_mode else 8
            self._battery_level -= battery_drain
            return True
        return False
    
    # Method overriding (polymorphism)
    def display_info(self):
        super().display_info()
        print(f"🎮 GPU: {self._gpu_model}")
        print(f"❄️ Cooling: {self._cooling_system}")
        print(f"🎯 Game Mode: {'Enabled' if self._game_mode else 'Disabled'}")


# Inheritance: BusinessPhone extends Smartphone
class BusinessPhone(Smartphone):
    """Specialized class for business smartphones"""
    
    def __init__(self, brand, model, storage, battery_capacity, security_level, has_stylus):
        super().__init__(brand, model, storage, battery_capacity)
        self._security_level = security_level
        self._has_stylus = has_stylus
        self._meeting_mode = False
    
    def schedule_meeting(self, time, participants):
        if self._is_powered_on:
            print(f"📅 Meeting scheduled for {time} with {len(participants)} participants")
            return True
        return False
    
    def enable_meeting_mode(self):
        self._meeting_mode = True
        print("🤝 Meeting mode enabled. Notifications silenced.")
    
    def take_notes(self, note):
        if self._has_stylus:
            print(f"📝 Note taken: {note}")
            return True
        print("❌ Stylus not available for taking notes")
        return False
    
    # Method overriding (polymorphism)
    def display_info(self):
        super().display_info()
        print(f"🔒 Security Level: {self._security_level}")
        print(f"✏️ Stylus: {'Available' if self._has_stylus else 'Not Available'}")
        print(f"🤝 Meeting Mode: {'Enabled' if self._meeting_mode else 'Disabled'}")


# Demo for Activity 1
def demo_smartphones():
    print("=" * 50)
    print("ACTIVITY 1: SMARTPHONE CLASS DEMO")
    print("=" * 50)
    
    # Create different smartphone objects
    regular_phone = Smartphone("Samsung", "Galaxy S23", 256, 5000)
    gaming_phone = GamingPhone("ASUS", "ROG Phone 7", 512, 6000, "Adreno 740", "Vapor Chamber")
    business_phone = BusinessPhone("Google", "Pixel 8 Pro", 128, 5050, "Titan M2", True)
    
    # Demonstrate regular smartphone
    regular_phone.power_on()
    regular_phone.make_call("123-456-7890")
    regular_phone.send_message("123-456-7890", "Hello from OOP!")
    regular_phone.charge(30)
    regular_phone.display_info()
    
    print("\n" + "-" * 30)
    
    # Demonstrate gaming phone (inheritance)
    gaming_phone.power_on()
    gaming_phone.enable_game_mode()
    gaming_phone.play_game("Call of Duty Mobile")
    gaming_phone.display_info()
    
    print("\n" + "-" * 30)
    
    # Demonstrate business phone (inheritance)
    business_phone.power_on()
    business_phone.enable_meeting_mode()
    business_phone.schedule_meeting("2:00 PM", ["Alice", "Bob", "Charlie"])
    business_phone.take_notes("Project deadline: Friday")
    business_phone.display_info()
    # ✅ Entry point to actually run the demo
if __name__ == "__main__":
    demo_smartphones()

    