class IndexError(Exception):
    def __init__(
            self,
            ssl_name: str,
            current_index: int,
            got_index: int
    ) -> None:
        self.message = (f"IndexError: The maximum index of a {ssl_name} (singly linked list) is {current_index}. "
                        f"You are trying to get the {got_index}th index.")

    def __str__(self) -> str:
        return self.message
