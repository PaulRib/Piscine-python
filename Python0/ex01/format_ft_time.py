import datetime as dt
import time


def format_ft_time():
	second = time.time()
	seconds = f"{second:,.6f}"
	science = f"{second:.2e}"
	print("Seconds since January 1, 1970:", seconds, "or", science, "in scientific notation")
	print(dt.datetime.today().strftime('%b %d %Y'))


if __name__ == "__main__":
	format_ft_time()