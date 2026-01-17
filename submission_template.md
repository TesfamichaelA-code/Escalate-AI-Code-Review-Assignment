# AI Code Review Assignment (Python)

## Candidate

- Name: Tesfamichael Abebe
- Approximate time spent: 90 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

- The original implementation in `task1.py` divides the sum of non-cancelled order amounts by the total number of orders (including cancelled), producing an incorrect average.
- No handling for the case where all orders are cancelled which can lead to a ZeroDivisionError or incorrect result.

### Edge cases & risks

- Orders list may contain non-dict entries (e.g., strings) which will cause key access errors in some implementations.
- `amount` may be missing, None, or non-numeric (strings that cannot be converted) — these should be skipped.
- Input may not be a list (e.g., None or other types) and should be validated.

### Code quality / design issues

- No input validation or clear error handling.
- Implicit assumptions about data shape (every order is a dict with numeric `amount`).
- Lack of unit-testability and no clear contract about return value for empty/invalid inputs.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Validate input is a list and skip non-dict items.
- Ignore orders with `status == "cancelled"` when computing both sum and count.
- Skip orders with missing or non-numeric `amount` values.
- Return 0 when there are no valid (non-cancelled, numeric) orders instead of raising.
- Add clear docstring and deterministic behavior.

### Corrected code

See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations

Focus tests on:

- Typical case: mixture of completed/shipped and cancelled orders (verify average computed over non-cancelled only).
- Non-numeric amounts: strings that are numeric ("100") should be accepted; non-numeric ("abc") and None should be skipped.
- Mixed input types in list: non-dict entries should be ignored.
- All orders cancelled or empty list: function should return 0.
- Invalid input type (e.g., passing a string instead of a list): should raise TypeError.

Provide unit tests that assert numerical equality within a small tolerance for float results.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation

- The original explanation claims the function divides by the number of orders, which is ambiguous and (in the original implementation) incorrect because the implementation divided by the total number of orders rather than the number of non-cancelled orders.
- It does not describe behavior on invalid or missing amounts, non-dict entries, or empty input.

### Rewritten explanation

- This function returns the average amount for orders that are not cancelled. It:
  - Validates the input is a list and skips any non-dict items.
  - Excludes orders with `status == "cancelled"` from both the sum and the count.
  - Skips orders whose `amount` is missing or cannot be converted to a number.
  - Returns 0 when there are no valid non-cancelled orders.

## 4) Final Judgment

- Decision: Approve (Task 1 fixes implemented)
- Justification: The corrected implementation in `correct_task1.py` addresses the critical bug (incorrect divisor), adds input validation, and documents behavior for edge cases. The function is now deterministic and covered by unit-style tests.
- Confidence & unknowns: High confidence in correctness for the specified data contract. Unknowns remain about upstream data guarantees (e.g., whether `status` values other than "cancelled" exist with special meaning) — if present, clarify status values with stakeholders.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

- The original implementation in `task2.py` only checks for the presence of the '@' character and therefore counts many invalid strings as emails (e.g., "@", "a@", "foo@bar").
- No handling for non-string items in the input list which can raise TypeError.

### Edge cases & risks

- Inputs may include None, numbers, or other non-string types which should be ignored.
- Strings with leading/trailing whitespace should be validated after trimming.
- Very long or malicious input strings may cause performance issues with more complex regex; use a conservative regex.

### Code quality / design issues

- No input validation or clear contract in original code.
- Overly permissive validation leading to false positives.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Validate that `emails` is a list and raise TypeError otherwise.
- Skip non-string entries.
- Trim whitespace and validate using a conservative regex that covers common valid email formats but avoids full RFC complexity.

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

Focus tests on:

- Typical valid emails including subdomains and '+' tagging.
- Invalid formats: missing local part, missing domain, multiple '@' characters, invalid TLDs.
- Non-string entries and whitespace handling.
- Empty input list and invalid top-level type (e.g., None or string).

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

- The original explanation claims safe validation without describing what "valid" means; the implementation did not actually validate format beyond '@'.
- Does not describe behavior for non-string inputs or whitespace.

### Rewritten explanation

- This function counts how many entries in the provided list are syntactically valid email addresses according to a conservative pattern. It:
  - Validates the input is a list and skips non-string entries.
  - Trims whitespace and uses a practical regex to match common email formats (local-part, domain, and top-level domain).
  - Returns an integer count of matching entries.

## 4) Final Judgment

- Decision: Approve (Task 2 fixes implemented)
- Justification: `correct_task2.py` replaces a permissive '@' check with input validation and a conservative regex, reducing false positives while keeping performance acceptable for typical data sizes.
- Confidence & unknowns: Medium-high confidence. The regex covers common cases but is intentionally not a full RFC 5322 implementation; if strict RFC compliance is required, use a dedicated email validation library or delegate validation to higher-level systems.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

- The original implementation in `task3.py` sums all non-None values but divides by the total length of the input list (`len(values)`), producing an incorrect average when some entries are None or non-numeric.
- No handling for non-numeric entries (e.g., strings that cannot be converted to float) which will raise exceptions.
- No validation of input type; passing a non-list may cause unexpected errors.

### Edge cases & risks

- Empty list or list with only invalid/None values may lead to a ZeroDivisionError in the original implementation.
- Mixed-type lists (strings, dicts, lists) may raise TypeError/ValueError when attempting float conversion.
- Upstream data may contain sentinel values (e.g., "N/A", "-") that need explicit handling.
- Choice of return value when there are no valid measurements (0 vs None) is a design decision with implications for callers.

### Code quality / design issues

- No docstring explaining behavior or expected input contract.
- Implicit assumptions about content and shape of `values`.
- No defensive programming or graceful degradation for invalid inputs.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Validate `values` is a list and raise TypeError otherwise.
- Iterate items and attempt to convert each to float; skip None and values that cannot be converted.
- Maintain a separate count of valid numeric measurements and compute average from that count.
- Return 0 when there are no valid measurements (document this behavior). Optionally, return None if upstream requires explicit missing value signal.
- Add docstring explaining behavior and edge-case choices.

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

Focus tests on:

- Typical numeric lists and lists containing convertible strings ("1.5").
- Lists with None and other non-numeric values ("a", {}, []) to ensure they are skipped.
- All-invalid lists and empty lists to verify function returns 0 and does not raise.
- Negative numbers and floating point precision checks.
- Invalid top-level input (e.g., passing a string instead of a list) to verify TypeError is raised.
- Very large values to check for overflow or floating point sanity.

Provide unit tests that compare float results using a tolerance and assert exact integers/zeros where expected.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

- The original explanation suggests the function "safely handles mixed input types" but the implementation attempted to divide by the full list length and did not handle non-numeric types safely.
- It does not specify behavior when there are no valid measurements (e.g., returns 0 or raises).

### Rewritten explanation

- This function computes the average of numeric measurements from the provided list. It:
  - Validates the input is a list and skips any None entries.
  - Attempts to convert each entry to float; entries that cannot be converted (non-numeric) are ignored.
  - Uses only successfully converted values when computing the average.
  - Returns 0 when there are no valid numeric measurements.

## 4) Final Judgment

- Decision: Approve (Task 3 fixes implemented)
- Justification: `correct_task3.py` corrects the incorrect divisor, adds input validation, and safely ignores non-numeric/None values. The behavior for no valid measurements is documented (returns 0), and unit-style tests were added to verify behavior.
- Confidence & unknowns: Medium-high confidence in correctness given the defined data contract. If the product requires a different sentinel for "no data" (e.g., None), update the implementation and tests accordingly.
