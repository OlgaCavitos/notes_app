
class BracketsValidator:
    def __init__(self):
        self._opens = "([{<"
        self._closes = ")]}>"
        self._text = None
        self._message = ""

    def _is_balanced(self):
        stack = []
        errors = []
        for symbol_position, symbol in enumerate(self._text):
            if symbol in self._opens:
                stack.append((symbol_position, symbol))
            elif symbol in self._closes:
                position = self._closes.index(symbol)
                if stack and self._opens[position] == stack[-1][1]:
                    stack.pop()
                else:
                    errors.append(symbol_position)

        if errors or stack:
            errors.extend(pos for pos, _ in stack)
            self._set_message("Unbalanced brackets", sorted(errors))
            raise ValidationError(self._message, idx=sorted(errors))

    def _set_message(self, base_text: str, errors: list) -> None:
        result = ", ".join(f"at {error}" for error in errors)
        self._message = f"{base_text}: {result}"

    def _mark_errors(self, indexes):
        print(self._text)
        marker = "".join("^" if i in indexes else " " for i in range(len(self._text)))
        print(marker)
        print()

    def validate(self, text):
        self._text = text
        try:
            self._is_balanced()
        except ValidationError as e:
            self._mark_errors(e.idx)
            raise e
        return True



class ValidationError(Exception):
    def __init__(self, message, *, idx):
        self.idx = idx
        super().__init__(message)

if __name__ == "__main__":
    text = "}"
    validator = BracketsValidator()
    try:
        validator.validate(text)
    except ValidationError as e:
        print("Validation failed:", e)

