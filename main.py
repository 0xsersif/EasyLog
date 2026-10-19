import sys


RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def read_log_file(path):
	error_count = 0
	warning_count = 0
	use_color = sys.stdout.isatty()

	try:
		with open(path, "r", encoding="utf-8", errors="replace") as log_file:
			for line in log_file:
				text = line.rstrip("\r\n")
				upper_text = text.upper()
				has_error = "ERROR" in upper_text
				has_warning = "WARN" in upper_text

				if has_error:
					error_count += 1
				if has_warning:
					warning_count += 1

				if has_error:
					label = "[ERROR] "
					color = RED
				elif has_warning:
					label = "[WARN] "
					color = YELLOW
				else:
					print(text)
					continue

				if use_color:
					print(f"{color}{label}{text}{RESET}")
				else:
					print(f"{label}{text}")
	except OSError as error:
		print(f"Could not read log file: {error}", file=sys.stderr)
		return

	print("\nSummary:")
	print(f"ERROR lines: {error_count}")
	print(f"WARN lines: {warning_count}")


def main():
	path = input("Path to log file: ").strip()
	read_log_file(path)


if __name__ == "__main__":
	main()
