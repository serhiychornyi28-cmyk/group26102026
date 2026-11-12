def concatenate_strings(string_1: str, string_2: str) -> str:
    #    через пробіл (лишні прибирає) і повертає нову стрічку

    return (string_1.strip() + ' ' + string_2.strip()).strip()

class TestBankAccount:
    def clean_name(name: str) -> str:
        return name
