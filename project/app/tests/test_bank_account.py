from Models.Bank_models import BankAccount


class TestBankAccount:
    def test_bank_account_creation(self):
        bank_account = BankAccount('afa')
        assert bank_account.money == 0