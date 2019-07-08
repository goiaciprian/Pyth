from win10toast import ToastNotifier

title = "STIC Connected"
msg = " An Mass Storage device has been connected."

if __name__ == "__main__":
    notification = ToastNotifier()
    notification.show_toast(title, msg)
