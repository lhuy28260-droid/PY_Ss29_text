from abc import ABC, abstractmethod

class BaseCharacter(ABC):
    def __init__(self, name: str, base_hp: int | float, attack: int | float):
        self._name = name
        self.__base_hp = float(base_hp)
        self._attack = float(attack)
        self._buffs: list[str] = []

    @property
    def name(self):
        return self._name

    @property
    def base_hp(self):
        return self.__base_hp

    @property
    def attack(self):
        return self._attack

    @abstractmethod
    def attack_enemy(self) -> float:
        raise NotImplementedError

    def apply_attack_buff(self, percent: float) -> None:
        self._attack *= 1 + percent / 100
        self._buffs.append(f"+{percent}% ATK")

    def __add__(self, other):
        if isinstance(other, BaseCharacter):
            return self.base_hp + other.base_hp
        return NotImplemented

    def __str__(self):
        return f"{self.name}: HP = {self.base_hp}, ATK = {self.attack}"

class MagicalStance:
    def __init__(self, magic_damage: float = 150.0):
        self._magic_damage = float(magic_damage)

    @property
    def magic_damage(self) -> float:
        return self._magic_damage

class Warrior(BaseCharacter):
    def __init__(self, name: str, base_hp: int | float, attack: int | float):
        super().__init__(name, base_hp, attack)

    def attack_enemy(self) -> float:
        return self.attack * 2.5

class Spellblade(Warrior, MagicalStance):
    def __init__(self, name: str, base_hp: int | float, attack: int | float, magic_damage: float = 150.0):
        Warrior.__init__(self, name, base_hp, attack)
        MagicalStance.__init__(self, magic_damage)

    def attack_enemy(self) -> float:
        physical_damage = Warrior.attack_enemy(self)
        return physical_damage + self.magic_damage

class VolcanoZone:
    def activate_buff(self, character):
        if hasattr(character, "apply_attack_buff"):
            character.apply_attack_buff(20)
            print("[Duck Typing]: Xác thực môi trường trận đấu thành công!")
            print("[Volcano Zone Effect]: Sức nóng dung nham kích hoạt! Gia tăng +20% sát thương cho Warrior!")
        else:
            print("[Duck Typing]: Môi trường không thể áp dụng hiệu ứng buff vào đối tượng này.")


def apply_battleground_effect(environment, character):
    environment.activate_buff(character)


def read_positive_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Giá trị phải lớn hơn 0. Vui lòng thử lại.")
                continue
            return value
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập số.")


def create_spellblade() -> Spellblade:
    print("--- KHỞI TẠO MA KIẾM SĨ SPELLBLADE ---")
    hp = read_positive_number("Nhập lượng máu cơ bản (HP): ")
    strength = read_positive_number("Nhập chỉ số sức mạnh (Strength): ")
    hero = Spellblade("Spellblade", hp, strength)
    total_hp = hero + hero

    print("\n[Thành công]: Khởi tạo nhân vật Spellblade thành công!")
    print("[MRO Architecture]: {}".format(" → ".join(cls.__name__ for cls in type(hero).mro())))
    print(f"[Overloading __add__]: Tổng HP tích lũy khi gộp đội hình: {total_hp}")
    return hero


def battle_with_spellblade(current_hero: Spellblade) -> None:
    print("--- THIẾT KẾ GIAO TRANH & DUCK TYPING ---")
    total_damage = current_hero.attack_enemy()
    print(f"[Đa hình] {current_hero.name} vung kiếm ma thuật gây tổng sát thương: {total_damage} DMG")

    arena = VolcanoZone()
    apply_battleground_effect(arena, current_hero)


def main():
    current_hero = None
    while True:
        print("\nRPG GAME CORE MENU")
        print("1. Khởi tạo Ma kiếm sĩ Spellblade & Xem cấu trúc MRO")
        print("2. Ra lệnh tấn công & Kích hoạt chiến trường (Duck Typing)")
        print("0. Thoát")
        choice = input("Chọn chức năng (0-2): ").strip()

        if choice == "1":
            current_hero = create_spellblade()
        elif choice == "2":
            if current_hero is None:
                print("[Lỗi]: Vui lòng khởi tạo nhân vật trước khi tiến hành giao tranh.")
            else:
                battle_with_spellblade(current_hero)
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
        


    


    